# Research Grants: Large Language Models Proposal Package

**Complete grant proposal suite for LLM research across 5 major funding agencies**

This repository contains comprehensive, ready-to-customize research proposals for Large Language Models (LLMs) targeting NSF, NIH, DOE, DARPA, and Taiwan's NSTC funding agencies.

---

## 📋 What's Included

### Core Materials

- **`core/research_narrative/`** - Master research narrative for LLM interpretability, alignment, efficiency, and knowledge integration
- **Research Architecture Diagram** - Visual schematic showing project structure and data flows

### Complete Agency-Specific Proposals

#### 🔵 NSF (National Science Foundation)
- **Project Summary** - Overview emphasizing Intellectual Merit and Broader Impacts
- **Project Description** (15 pages) - Detailed research narrative with 5 specific objectives
- **Budget Justification** ($1.2M/3 years) - Personnel, equipment, materials breakdown
- **Focus**: Fundamental AI research, education, workforce development

#### 🟢 NIH (National Institutes of Health) 
- **Specific Aims** (1 page) - Problem statement, central hypothesis, 4 research aims
- **Research Strategy** (12 pages) - Significance, Innovation, Approach for R01 mechanism
- **Focus**: Biomedical applications, clinical decision support, reliable healthcare AI

#### 🟠 DOE (Department of Energy)
- **Project Narrative** - Energy-focused materials discovery applications
- **Technical Approach** - Materials knowledge integration, experiment design, scaling
- **Focus**: Energy materials (batteries, catalysts, solar), cost-sharing requirements

#### 🔴 DARPA (Defense Advanced Research Projects Agency)
- **Technical Volume** - High-risk, high-reward research for intelligence operations
- **18-Month Timeline** with quarterly milestones and go/no-go criteria
- **Transition Planning** - Deployment, commercialization, dual-use applications
- **Focus**: Transformative innovation, national security impact, technical demonstrations

#### 🟣 NSTC (Taiwan - National Science and Technology Council)
- **CM03 Form** - Official proposal format with bilingual support
- **English + Traditional Chinese** - Both abstracts and full proposal translated
- **Focus**: Innovation, feasibility, preliminary data, industrial applications

---

## 📁 Project Structure

```
research-grants/
├── CLAUDE.md                          # Grant writing guidelines
├── README.md                          # This file
├── core/
│   └── research_narrative/
│       └── llm_research_master.md     # Master outline for all proposals
├── proposals/
│   ├── nsf/
│   │   ├── sections/
│   │   │   ├── project_summary.md     # NSF overview (1 page)
│   │   │   └── project_description.md # NSF detailed (15 pages)
│   │   ├── budgets/
│   │   │   └── budget_justification.md # Budget ($1.2M/3yr)
│   │   ├── figures/                    # [Ready for schematics]
│   │   └── templates/                  # [Customizable templates]
│   ├── nih/
│   │   ├── sections/
│   │   │   ├── specific_aims.md        # NIH Specific Aims (1 page)
│   │   │   └── research_strategy.md    # NIH Strategy (12 pages)
│   │   ├── budgets/                    # [Ready for modular budget]
│   │   └── figures/                    # [Data visualization ready]
│   ├── doe/
│   │   ├── sections/
│   │   │   └── project_narrative.md    # DOE narrative
│   │   └── budgets/                    # [Cost-share breakdown]
│   ├── darpa/
│   │   ├── sections/
│   │   │   └── technical_proposal.md   # DARPA technical volume
│   │   └── budgets/                    # [Phase-based budget]
│   └── nstc/
│       ├── sections/
│       │   └── cm03_proposal.md        # NSTC CM03 (bilingual)
│       └── budgets/                    # [Taiwan budget format]
└── [figures/                           # AI-generated schematics]
```

---

## 🚀 Quick Start

### 1. Choose Your Agency
- **NSF**: For fundamental research, education, broad impact
- **NIH**: For biomedical applications, clinical translation
- **DOE**: For energy/materials applications, cost-sharing ready
- **DARPA**: For high-risk, transformative breakthroughs
- **NSTC**: For Taiwan-based researchers, industrial impact

### 2. Customize Core Narrative
Edit `core/research_narrative/llm_research_master.md`:
- Replace [Relevant publications] with your papers
- Update team names and expertise
- Adjust preliminary data sections
- Customize institution names and resources

### 3. Adapt Agency-Specific Proposals
- Copy relevant agency folder (e.g., `proposals/nsf/`)
- Update institution-specific sections:
  - Your university name and F&A rate (NSF/NIH)
  - Department affiliations
  - Institutional resources and support letters
  - Collaborator information
- Customize figures and timelines
- Adjust budget to your institution's rates

### 4. Create Visuals
- **Research Architecture Diagram**: Already created - customize labels/flow
- **Gantt Charts**: Use timeline templates in each proposal
- **Figures**: Generate schematics for each research objective

### 5. Finalize & Submit
- Run compliance checker on formatting
- Obtain institutional signatures/commitments
- Submit to agency portal 48 hours before deadline

---

## 💡 Key Features

### ✅ Agency-Specific Approaches

| Agency | Format | Pages | Focus |
|--------|--------|-------|-------|
| NSF | Summary + Description | 1 + 15 | Merit review + broader impacts |
| NIH | Aims + Strategy | 1 + 12 | Significance/Innovation/Approach |
| DOE | Narrative | ~8-10 | Mission alignment + innovation |
| DARPA | Technical Volume | ~8-10 | Technical merit + transition |
| NSTC | CM03 Form | ~10-15 | Innovation + feasibility |

### ✅ Comprehensive Scope

- **Five Research Objectives** (Interpretability, Alignment, Efficiency, Knowledge Integration, Multimodal)
- **Realistic 3-Year Timeline** with quarterly milestones
- **Complete Budget Justification** ($1.2M NSF; scalable to other agencies)
- **Team Composition** (PI, Co-Is, postdocs, PhD students)
- **Preliminary Data** sections with placeholders
- **Risk Mitigation** strategies
- **Broader Impacts** (education, diversity, open science, societal benefit)
- **Transition Plans** (DARPA-specific, but useful for others)

### ✅ Flexible Templates

All proposals follow best practices but allow:
- Domain adaptation (materials, biomedical, security, etc.)
- Team reconfiguration
- Timeline adjustment
- Budget customization by institution

---

## 📊 Proposal Statistics

| Metric | NSF | NIH | DOE | DARPA | NSTC |
|--------|-----|-----|-----|-------|------|
| Project Description | 15 pp | 12 pp | 8-10 pp | 8-10 pp | 10-15 pp |
| Research Aims | 5 | 4 | 4 | 3 phases | 5 |
| Timeline | 3 years | 3 years | 3 years | 18 mo | 3 years |
| Budget Example | $1.2M | $900K/yr | $2.5M | varies | NT$38.2M |
| Word Count (total) | ~25K | ~18K | ~12K | ~10K | ~15K |

---

## 🎯 Research Topics

### Master Topic: Large Language Models for Knowledge Integration

**Core Problem**: LLMs lack interpretability, generate hallucinations, and struggle to integrate structured knowledge—limiting deployment in high-stakes domains.

**Solution**: 
1. Mechanistic interpretability to understand LLM reasoning
2. Alignment methods to reduce hallucinations
3. Efficient scaling for broader accessibility
4. Knowledge integration for domain expertise
5. Multimodal understanding for complex reasoning

**Applications**:
- Scientific discovery (literature synthesis, hypothesis generation)
- Healthcare & medicine (clinical decision support, drug discovery)
- Industrial applications (materials discovery, process optimization)

**Customization**: Replace LLM topic with your research focus:
- Computer vision, NLP, robotics, biology, chemistry, materials science, etc.

---

## 📝 Writing Tips

### 1. Customization Checklist
- [ ] Replace [PI Name] with your name
- [ ] Update [Institution] with your university
- [ ] Insert your publication list
- [ ] Add your preliminary results
- [ ] Update team information
- [ ] Adjust budget to your institution's rates
- [ ] Customize institutional support letters
- [ ] Update timeline to your schedule
- [ ] Add your specific aims/objectives
- [ ] Proofread for consistency

### 2. Common Edits

**For different research topics**:
- Replace "LLM" with your focal area
- Adjust "interpretability" to "safety," "efficiency," "generalization," etc.
- Customize application domains
- Update preliminary data to match your work
- Adjust timeline for your field's constraints

**For different team sizes**:
- NSF/NIH: Designed for 1-2 PIs + co-Is
- DARPA: Works for larger teams (add personnel)
- DOE: Scales well; add collaborating institutions

**For different budgets**:
- NSF: $1.2M example (easily scalable)
- NIH: ~$900K/year for R01 (adjust based on mechanism)
- DOE: $2.5M example (include cost-sharing)
- DARPA: Varies by program (follow BAA requirements)
- NSTC: NT$38.2M (~US$1.3M) example

---

## 🔗 Agency Links

- [NSF Grants](https://nsf.gov/funding/)
- [NIH NIAID](https://www.niaid.nih.gov/grants-contracts)
- [DOE EERE](https://www.energy.gov/eere/funding)
- [DARPA BAAs](https://www.darpa.mil/news-events/announcements)
- [NSTC/Taiwan](https://www.nstc.gov.tw/english/)

---

## 📚 Additional Resources

See `CLAUDE.md` for:
- Agency-specific requirements and review criteria
- Best practices for each section type
- Common mistakes to avoid
- Workflow timeline for proposal development
- References to specialized guidance documents

---

## ✨ Next Steps

1. **Choose an agency** that aligns with your research and institution
2. **Read the relevant proposal** in `proposals/[agency]/sections/`
3. **Customize the master narrative** with your research details
4. **Adapt the agency proposal** for your team and timeline
5. **Create supporting materials** (letters, CVs, figures)
6. **Follow agency submission guidelines** (formatting, fonts, margins)
7. **Submit 48 hours before deadline** to avoid portal issues

---

## 📞 Support

For detailed guidance on each section, refer to:
- `CLAUDE.md` - Comprehensive grant writing guide
- `proposals/[agency]/sections/` - Full proposal texts with explanations
- `core/research_narrative/` - Master narrative to adapt

---

**Good luck with your proposals!** 🎓

---

*Last updated: April 2026*
*Repository: th00masml/research-grants*
