# 95 — Convolutional Neural Networks (CNN)

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

A **Convolutional Neural Network (CNN)** is built for images. Instead of connecting every pixel to every neuron, it slides small **filters (kernels)** across the image to detect local patterns (edges, textures), producing **feature maps**. **Pooling** layers downsample to shrink size and add invariance. Stacked conv+pool layers learn a hierarchy: edges → shapes → objects, with far fewer parameters than a dense net.

## Why it matters

CNNs revolutionized computer vision (classification, detection, segmentation, medical imaging). Weight sharing and locality make them efficient and translation-invariant — the right inductive bias for images.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install tensorflow
```

## Key concepts

- **Convolution** — Slide a kernel over the image; each position is a dot product.
- **Kernel/filter** — Small weight grid that detects a local pattern.
- **Feature map** — The output of applying a filter across the image.
- **Pooling** — Downsample (max/avg) to reduce size and add invariance.
- **Weight sharing** — The same kernel is reused everywhere — few parameters.
- **Hierarchy** — Early layers find edges; deeper layers find objects.

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
def conv2d(image, kernel):
    ih, iw = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])
    out = [[0.0] * (iw - kw + 1) for _ in range(ih - kh + 1)]
    for i in range(len(out)):
        for j in range(len(out[0])):
            out[i][j] = sum(image[i + a][j + b] * kernel[a][b]
                            for a in range(kh) for b in range(kw))
    return out

# image: dark left half, bright right half -> a vertical edge in the middle
image = [[0, 0, 0, 9, 9, 9] for _ in range(5)]
edge_kernel = [[-1, 0, 1],            # vertical-edge (Prewitt) filter
               [-1, 0, 1],
               [-1, 0, 1]]
feature_map = conv2d(image, edge_kernel)
print("feature map (high values mark the edge):")
for row in feature_map:
    print(" ", [round(v) for v in row])     # the edge column lights up
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ Convolution shrinks the image (output = input − kernel + 1); use padding='same' to preserve size.
- ⚠️ Feed images with a channel dimension (H×W×C); forgetting it causes shape errors.
- ⚠️ Normalize pixel values (e.g. /255) — raw 0–255 inputs slow training.
- ⚠️ Too many conv filters/dense units overfit small datasets — use dropout/augmentation.
- ⚠️ Pooling loses spatial precision; for segmentation you need it back (upsampling/U-Net).

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

