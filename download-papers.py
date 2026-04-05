#!/usr/bin/env python3
"""
Paper Download Plugin for Wiki System

Downloads recent NLP papers from arXiv and adds them to sources/articles/.
Creates both PDF metadata files and markdown summaries.

Usage:
    python download-papers.py --query "transformer attention" --max 5
    python download-papers.py --category "cs.CL" --max 10 --days 30
"""

import os
import sys
import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
import time

ARXIV_API = "http://export.arxiv.org/api/query?"
SOURCES_DIR = Path(__file__).parent / "sources" / "articles"


def fetch_papers(query: str = None, category: str = "cs.CL", max_results: int = 5, days: int = 30):
    """Fetch papers from arXiv API."""

    # Build search query
    if query:
        search_query = f'all:"{query}" AND cat:{category}'
    else:
        search_query = f'cat:{category}'

    # Add date filter (last N days)
    cutoff_date = (datetime.utcnow() - timedelta(days=days)).strftime("%Y%m%d%H%M%S")
    search_query += f' AND submittedDate:[{cutoff_date}000000 TO 9999999999999999]'

    params = {
        'search_query': search_query,
        'start': 0,
        'max_results': max_results,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
    }

    url = ARXIV_API + urlencode(params)
    print(f"Fetching from: {url}\n")

    try:
        with urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching papers: {e}")
        return None


def parse_arxiv_xml(xml_content: str) -> list:
    """Parse arXiv XML response."""
    papers = []

    # Simple XML parsing (avoid external dependencies)
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(xml_content)
    except:
        print("Error parsing XML response")
        return []

    # arXiv uses atom namespace
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    for entry in root.findall('atom:entry', ns):
        paper = {}

        # Extract fields
        paper['title'] = entry.find('atom:title', ns).text.strip()
        paper['id'] = entry.find('atom:id', ns).text.split('/abs/')[-1]
        paper['authors'] = [
            author.find('atom:name', ns).text
            for author in entry.findall('atom:author', ns)
        ]
        paper['published'] = entry.find('atom:published', ns).text.split('T')[0]
        paper['summary'] = entry.find('atom:summary', ns).text.strip()

        # Get PDF link
        for link in entry.findall('atom:link', ns):
            if link.get('type') == 'application/pdf':
                paper['pdf_url'] = link.get('href')
                break
        else:
            # Construct PDF URL if not in links
            paper['pdf_url'] = f"https://arxiv.org/pdf/{paper['id']}.pdf"

        papers.append(paper)

    return papers


def create_metadata_file(paper: dict, filepath: Path):
    """Create metadata markdown file for a paper."""

    authors_str = ", ".join(paper['authors'][:3])
    if len(paper['authors']) > 3:
        authors_str += f", et al. ({len(paper['authors'])} total)"

    arxiv_url = f"https://arxiv.org/abs/{paper['id']}"

    content = f"""---
title: {paper['title']}
type: source
arxiv_id: {paper['id']}
published: {paper['published']}
authors: {json.dumps(paper['authors'])}
source_url: {arxiv_url}
pdf_url: {paper['pdf_url']}
added_to_wiki: {datetime.now().strftime('%Y-%m-%d')}
---

# {paper['title']}

**Authors:** {authors_str}
**Published:** {paper['published']}
**arXiv:** [{paper['id']}]({arxiv_url})

## Abstract

{paper['summary']}

## Download

- [PDF on arXiv]({paper['pdf_url']})
- [Full Paper on arXiv]({arxiv_url})

## Notes

_To be populated during wiki ingest_
"""

    filepath.write_text(content)
    print(f"✓ Created {filepath.name}")


def sanitize_filename(title: str, arxiv_id: str) -> str:
    """Create valid filename from paper title and ID."""
    # Use arxiv ID as base for uniqueness
    clean_title = "".join(c for c in title if c.isalnum() or c in (' ', '-'))
    clean_title = clean_title.replace(' ', '-')[:50]  # Max 50 chars
    return f"{arxiv_id.replace('/', '-')}-{clean_title}.md"


SAMPLE_PAPERS = [
    {
        "title": "Attention Is All You Need",
        "id": "1706.03762",
        "authors": ["Ashish Vaswani", "Noam Shazeer", "Parmar Aditya", "Jakob Uszkoreit", "Llion Jones", "Aidan N. Gomez", "Łukasz Kaiser", "Illia Polosukhin"],
        "published": "2017-06-12",
        "summary": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.",
        "pdf_url": "https://arxiv.org/pdf/1706.03762.pdf"
    },
    {
        "title": "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "id": "1810.04805",
        "authors": ["Jacob Devlin", "Ming-Wei Chang", "Kenton Lee", "Kristina Toutanova"],
        "published": "2018-10-11",
        "summary": "We introduce BERT, a new method of pre-training language representations which obtains state-of-the-art results on a wide array of Natural Language Processing (NLP) tasks. BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.",
        "pdf_url": "https://arxiv.org/pdf/1810.04805.pdf"
    },
    {
        "title": "Language Models are Unsupervised Multitask Learners",
        "id": "1902.01340",
        "authors": ["Alec Radford", "Jeffrey Wu", "Rewon Child", "David Luan", "Dario Amodei", "Ilya Sutskever"],
        "published": "2019-02-14",
        "summary": "Natural language processing tasks are typically approached with supervised learning on task-specific datasets. We demonstrate that language models begin learning these tasks without any explicit supervision when trained on a new dataset of Internet text assembled by common crawl. By analyzing word predictions on these tasks for increasing model capacity, we find that larger models begin to cross the threshold of intelligible generations when trained on sufficiently large and diverse data.",
        "pdf_url": "https://arxiv.org/pdf/1902.01340.pdf"
    },
    {
        "title": "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale",
        "id": "2010.11929",
        "authors": ["Alexey Dosovitskiy", "Lucas Beyer", "Alexander Kolesnikov", "Dirk Weissenborn", "Xiaohua Zhai", "Thomas Unterthiner", "Mostafa Dehghani", "Matthias Minderer", "Georg Heigold", "Sylvain Grangier"],
        "published": "2020-10-22",
        "summary": "While the Transformer architecture has become the de-facto standard for natural language processing tasks, its applications to computer vision remain limited. In vision, attention is either applied in conjunction with convolutional networks, or used to replace certain components while keeping their overall structure in place. We show that a pure transformer applied directly to sequences of image patches can perform very well on image classification tasks.",
        "pdf_url": "https://arxiv.org/pdf/2010.11929.pdf"
    },
    {
        "title": "Training language models to follow instructions with human feedback",
        "id": "2203.02155",
        "authors": ["Long Ouyang", "Jeff Wu", "Xu Jiang", "Diogo Almeida", "Carroll L. Wainwright", "Pamela Mishkin", "Chak Ming Lee", "Jie Tang", "William Askell", "Rupak Parikh"],
        "published": "2022-03-04",
        "summary": "Making language models bigger does not inherently make them better at following a user's intent. For example, larger models can be more sycophantic and exhibit undesired behaviors. In order to make language models more helpful, harmless, and honest, we fine-tune language models with human feedback, using reinforcement learning from human feedback (RLHF).",
        "pdf_url": "https://arxiv.org/pdf/2203.02155.pdf"
    }
]


def main():
    parser = argparse.ArgumentParser(
        description="Download NLP papers from arXiv and add to wiki"
    )
    parser.add_argument(
        '--query',
        type=str,
        default="transformer attention mechanism",
        help='Search query (default: "transformer attention mechanism")'
    )
    parser.add_argument(
        '--category',
        type=str,
        default="cs.CL",
        help='arXiv category (default: cs.CL for NLP)'
    )
    parser.add_argument(
        '--max',
        type=int,
        default=5,
        help='Max papers to download (default: 5)'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=180,
        help='Days back to search (default: 180)'
    )
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Use sample papers (for offline demo)'
    )

    args = parser.parse_args()

    # Create sources directory if it doesn't exist
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)

    if args.demo:
        print(f"📥 Using sample NLP papers (demo mode)...\n")
        papers = SAMPLE_PAPERS[:args.max]
    else:
        print(f"📥 Downloading recent NLP papers...")
        print(f"   Query: {args.query}")
        print(f"   Category: {args.category}")
        print(f"   Max results: {args.max}")
        print(f"   From last {args.days} days\n")

        # Fetch papers
        xml_content = fetch_papers(
            query=args.query,
            category=args.category,
            max_results=args.max,
            days=args.days
        )

        if not xml_content:
            print("❌ Failed to fetch papers. Try --demo for sample papers")
            return 1

        # Parse results
        papers = parse_arxiv_xml(xml_content)

        if not papers:
            print("❌ No papers found matching criteria")
            return 1

    print(f"Found {len(papers)} papers:\n")

    # Create files for each paper
    for paper in papers:
        filename = sanitize_filename(paper['title'], paper['id'])
        filepath = SOURCES_DIR / filename

        # Avoid overwriting
        counter = 1
        base_path = filepath
        while filepath.exists():
            filepath = base_path.parent / f"{base_path.stem}-{counter}.md"
            counter += 1

        create_metadata_file(paper, filepath)
        print(f"   {paper['title'][:60]}...")
        time.sleep(0.2)

    print(f"\n✅ Added {len(papers)} papers to sources/articles/")
    print(f"\nNext: Run 'Ingest sources/articles' to process into wiki")

    return 0


if __name__ == "__main__":
    sys.exit(main())
