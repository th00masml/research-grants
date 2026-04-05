---
title: Transformer Architecture
type: summary
sources: [sources/articles/1706.03762-Attention-Is-All-You-Need.md]
related: [wiki/concepts/attention-mechanism.md, wiki/concepts/self-supervised-learning.md]
created: 2026-04-05
updated: 2026-04-05
---

# Transformer Architecture

## Summary

The Transformer is a neural network architecture introduced by Vaswani et al. (2017) that replaces recurrence and convolution entirely with attention mechanisms. It became the foundation for modern large language models and vision systems.

## Key Innovation

Instead of sequential processing (RNNs) or local receptive fields (CNNs), Transformers use **self-attention** to directly compute relationships between all positions in parallel. This enables:

- **Parallelizable training** — process entire sequences at once
- **Long-range dependencies** — direct connections between distant tokens
- **Scalability** — efficient computation on large datasets

## Architecture Layers

### Input & Embedding
- Token embedding + positional encoding
- Maps discrete tokens to continuous vectors

### Encoder Stack (Multi-layer)
1. **Multi-head self-attention** — parallel attention over all positions
2. **Feed-forward network** — position-wise dense layers
3. **Layer normalization & residual connections**

### Decoder Stack
- Masked self-attention (can't attend to future tokens)
- Cross-attention to encoder outputs
- Same FF and normalization layers

### Output
- Linear projection to vocabulary
- Softmax for next-token prediction

## Why It Works

| Property | RNN/CNN | Transformer |
|----------|---------|-------------|
| Parallelization | Sequential | Full parallel |
| Long-range deps | Diluted (distance) | Direct (1 step) |
| Computation | O(n) sequential | O(1) steps |
| GPUs | Underutilized | Highly efficient |

## Impact

- **2017+**: Became standard for NLP
- **2018**: BERT, GPT built on Transformers
- **2020+**: Vision Transformers, multimodal models
- **2022+**: Foundation for all major LLMs (GPT-3, PaLM, Llama)

## See Also

- [[Attention Mechanism]] — Core technical component
- [[BERT Language Model]] — First major application
- [[GPT-2 Scaling Laws]] — Showed power of scaling Transformers
- [[Vision Transformers]] — Non-NLP application

## Sources

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — Vaswani et al., 2017
