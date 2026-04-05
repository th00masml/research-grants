---
title: Scaling Laws
type: concept
sources: [sources/articles/1902.01340-Language-Models-are-Unsupervised-Multitask-Learner.md, sources/articles/2203.02155-Training-language-models-to-follow-instructions-wi.md]
related: [wiki/summaries/gpt-2-scaling-laws.md, wiki/concepts/pre-training-and-fine-tuning.md]
created: 2026-04-05
updated: 2026-04-05
---

# Scaling Laws

## Core Insight

Language model performance follows predictable power-law relationships with:
1. **Model size** (parameters)
2. **Dataset size** (tokens)
3. **Compute budget** (FLOPs)

Performance doesn't plateau — it improves log-linearly with scale.

## Key Relationships

### Model Size
```
Loss ∝ N^(-α)  where α ≈ 0.07 to 0.1
```

Doubling model size → ~7-10% improvement

### Dataset Size
```
Loss ∝ D^(-β)  where β ≈ 0.09 to 0.12
```

Doubling training data → ~9-12% improvement

### Compute Allocation
Optimal ratio: **6x more tokens than parameters**
- Chinchilla scaling: allocate compute equally between model and data
- Previous convention (Kaplan et al.): underemphasized data

## Empirical Evidence

| Paper | Model | Size | Observation |
|-------|-------|------|-------------|
| Radford et al. 2019 | GPT-2 | 1.5B | Emergent few-shot abilities at scale |
| Brown et al. 2020 | GPT-3 | 175B | In-context learning, prompt engineering |
| Hoffmann et al. 2022 | Chinchilla | 70B | Same compute as Gopher (280B) with better scaling |

## Emergent Abilities

As models scale, unexpected behaviors emerge:

- **Few-shot learning** — Can perform tasks with just examples (no fine-tuning)
- **In-context learning** — Adapt behavior based on prompt
- **Reasoning** — Solve multi-step problems (chain-of-thought)
- **Code generation** — Write and debug code

These weren't explicitly trained for — they emerge from scale.

## Implications

1. **Compute is the bottleneck**, not architectural innovation
2. **Larger models are more efficient** (lower loss per compute)
3. **Data quality matters** — garbage in, garbage out
4. **Predict performance** — can extrapolate from small experiments

## Open Questions

- Do scaling laws hold beyond 10^24 FLOPs?
- Are there "phases" where different abilities emerge?
- How do scaling laws interact with RLHF fine-tuning?
- What is the theoretical limit?

## See Also

- [[GPT-2 Scaling Laws]] — Empirical demonstration
- [[InstructGPT and RLHF]] — Scaling with human feedback
- [[Transformer Architecture]] — Architecture that enabled scaling

## Sources

- [Language Models are Unsupervised Multitask Learners](https://arxiv.org/abs/1902.01340) — Radford et al., 2019 (GPT-2)
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — Ouyang et al., 2022
