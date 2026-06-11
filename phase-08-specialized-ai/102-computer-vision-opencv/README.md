# 102 — Computer Vision with OpenCV

> Part of the **Python + DSA + AI/ML** learning workspace.  Learning loop: **README → notes.py → practice.md**

## What is it?

**Computer vision** processes images, which are just grids of pixel values (grayscale = one number 0–255; color = three R/G/B channels). Basic operations: convert to **grayscale**, adjust brightness/contrast, **threshold** to binary, **blur** (smooth), detect **edges**, resize, and flip. **OpenCV** (`cv2`) is the standard library for reading images and running these operations fast.

## Why it matters

Vision powers face detection, OCR, medical imaging, self-driving, and AR. Understanding pixels and core operations (filters, thresholds, edges) is the foundation for CNNs and real-world image pipelines.

## Setup

This topic uses external libraries. Install them with:

```bash
pip install opencv-python
```

## Key concepts

- **Pixel grid** — An image is a 2-D (gray) or 3-D (color) array of intensities.
- **Grayscale** — Collapse RGB to one luminosity channel.
- **Thresholding** — Turn a gray image into black/white by a cutoff.
- **Blur / smoothing** — Average neighboring pixels to reduce noise.
- **Edge detection** — Find intensity changes (Sobel/Canny).
- **Channels** — Color images have R, G, B (OpenCV uses BGR order).

## Code example

A fully commented, runnable example (see `notes.py` for more):

```python
# A 2x3 RGB image as nested lists: each pixel is [R, G, B]
image = [
    [[255, 0, 0],   [0, 255, 0],   [0, 0, 255]],     # red, green, blue
    [[255, 255, 0], [0, 0, 0],     [255, 255, 255]], # yellow, black, white
]

def to_grayscale(img):
    # luminosity formula: 0.299R + 0.587G + 0.114B
    return [[round(0.299*p[0] + 0.587*p[1] + 0.114*p[2]) for p in row]
            for row in img]

gray = to_grayscale(image)
print("grayscale values:")
for row in gray:
    print(" ", row)
```

Run every example in this topic with:

```bash
python notes.py
```

## Common mistakes & gotchas

- ⚠️ OpenCV loads color as BGR, not RGB — convert before showing with matplotlib.
- ⚠️ Pixel values are 0–255 (uint8); arithmetic can overflow/wrap — clamp or use a wider dtype.
- ⚠️ Image arrays are indexed [row, col] = [y, x], which trips people up.
- ⚠️ Blurring/edge kernels can't fully process border pixels — handle padding.
- ⚠️ Resizing changes aspect ratio if you don't keep it; interpolation choice affects quality.

## Practice

Open [`practice.md`](practice.md) and solve the exercises (easy → hard). Try each one before revealing the solution.

