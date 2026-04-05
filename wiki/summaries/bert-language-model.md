---
title: BERT Language Model
type: summary
sources: [sources/articles/1810.04805-BERT-Pre-training-of-Deep-Bidirectional-Transforme.md]
related: [wiki/concepts/pre-training-and-fine-tuning.md, wiki/concepts/self-supervised-learning.md]
created: 2026-04-05
updated: 2026-04-05
---

# BERT: Language Model Pre-training

## Summary

BERT (Bidirectional Encoder Representations from Transformers) by Devlin et al. (2018) demonstrated that pre-training a deep bidirectional Transformer on unlabeled text, then fine-tuning on task-specific data, achieves state-of-the-art results across NLP tasks.

## Key Innovation

**Bidirectional pre-training** — Unlike GPT (which predicts left-to-right), BERT reads context from both directions:

- Masked Language Modeling (MLM): Randomly mask 15% of tokens, predict them from surrounding context
- Next Sentence Prediction (NSP): Predict whether sentence B follows sentence A

This bidirectionality enables deeper understanding of language.

## Architecture

- **Base**: 12 layers, 768 hidden units, 110M parameters
- **Large**: 24 layers, 1024 hidden units, 340M parameters
- Trained on BookCorpus (800M words) + Wikipedia (2.5B words)

## Pre-training vs Fine-tuning

### Pre-training (Expensive, One-time)
- Unlabeled corpus
- Masked token prediction + sentence ordering
- Takes weeks on multi-GPU

### Fine-tuning (Cheap, Task-specific)
- Add task-specific layer (classification, Q&A, etc.)
- Train on labeled data for hours
- State-of-the-art with minimal data

## Results

**Performance gains across 11 NLP tasks:**
- GLUE benchmark: +7.7% improvement
- SQuAD reading comprehension: 93.2% F1
- CoLA linguistic acceptability: 72.3% (vs 59.9% previous)

## Impact

- Sparked "pre-train then fine-tune" era
- Showed benefits of bidirectional context
- Inspired RoBERTa, ALBERT, DistilBERT variants
- Foundation for modern transfer learning in NLP

## See Also

- [[Transformer Architecture]] — Technical foundation
- [[Pre-training and Fine-tuning]] — Training paradigm
- [[Scaling Laws]] — Relationship to model size
- [[GPT-2 Scaling Laws]] — Comparison with unidirectional approach

## Sources

- [BERT: Pre-training of Deep Bidirectional Transformers](https://arxiv.org/abs/1810.04805) — Devlin et al., 2018
