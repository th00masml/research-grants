---
title: Attention Mechanism
type: concept
sources: [sources/articles/1706.03762-Attention-Is-All-You-Need.md]
related: [wiki/summaries/transformer-architecture.md, wiki/concepts/transformer-architecture.md]
created: 2026-04-05
updated: 2026-04-05
---

# Attention Mechanism

## Core Concept

Attention allows a model to selectively focus on different parts of the input when processing each part of the output. Instead of compressing all input into a fixed-size vector, the model can dynamically "attend to" relevant information.

## How It Works

Given a query (Q), key (K), and value (V):

```
Attention(Q, K, V) = softmax(Q * K^T / sqrt(d_k)) * V
```

1. **Score** — Compare query to each key: `Q * K^T`
2. **Normalize** — Softmax produces weights (0 to 1)
3. **Output** — Weighted sum of values

## Multi-head Attention

Run multiple attention operations in parallel, each focusing on different aspects:

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) * W^O
```

Benefits:
- Different heads learn different relationships
- Some heads focus on syntax, others on semantics
- Robust and flexible

## Why It's Revolutionary

| Task | RNN | Attention |
|------|-----|-----------|
| Encoding long sequences | Degraded | Constant-time access |
| Parallelization | Sequential | Fully parallel |
| Interpretability | Black box | Attention weights are human-readable |
| Computational efficiency | O(n) steps | O(1) steps (parallel) |

## Types of Attention

- **Self-attention** — Query, key, value from same sequence
- **Cross-attention** — Query from one sequence, key/value from another
- **Masked attention** — Can't attend to future positions (causal)

## Applications

- [[Transformer Architecture]] — Foundation
- Sequence-to-sequence models (translation, summarization)
- Speech recognition
- Computer vision (Vision Transformers)

## See Also

- [[Transformer Architecture]] — Uses multi-head self-attention
- [[Scaling Laws]] — Attention enables efficient scaling

## Sources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017
