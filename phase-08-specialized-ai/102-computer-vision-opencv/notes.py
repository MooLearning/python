# ======================================================================
# 102 — Computer Vision with OpenCV  |  notes.py
# Run:  python notes.py
# Heavily commented, runnable examples. Edit freely and re-run!
# ======================================================================

# Requires: opencv-python
# Install:  pip install opencv-python

# ----------------------------------------------------------------------
# Example 1: Represent an image and convert to grayscale (pure Python)
# ----------------------------------------------------------------------
print("\n--- Example 1: Represent an image and convert to grayscale (pure Python) ---")
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

# ----------------------------------------------------------------------
# Example 2: Thresholding, brightness, and flip
# ----------------------------------------------------------------------
print("\n--- Example 2: Thresholding, brightness, and flip ---")
gray = [[50, 120, 200],
        [30, 128, 255],
        [90, 60, 180]]

# Threshold: pixels >= 128 become white (255), else black (0)
def threshold(img, t=128):
    return [[255 if v >= t else 0 for v in row] for row in img]
print("thresholded:")
for row in threshold(gray):
    print(" ", row)

# Increase brightness by 40 (clamped to 255)
def brighten(img, amount):
    return [[min(255, v + amount) for v in row] for row in img]
print("brighter:", brighten(gray, 40)[0])

# Flip horizontally (mirror each row)
print("flipped:", [row[::-1] for row in gray][0])

# ----------------------------------------------------------------------
# Example 3: Box blur (smoothing) and OpenCV
# ----------------------------------------------------------------------
print("\n--- Example 3: Box blur (smoothing) and OpenCV ---")
def box_blur(img):
    # average each pixel with its 8 neighbors (interior pixels only)
    h, w = len(img), len(img[0])
    out = [row[:] for row in img]
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            total = sum(img[i+di][j+dj] for di in (-1, 0, 1) for dj in (-1, 0, 1))
            out[i][j] = total // 9
    return out

img = [[10, 10, 10, 10, 10],
       [10, 90, 90, 90, 10],
       [10, 90, 90, 90, 10],
       [10, 90, 90, 90, 10],
       [10, 10, 10, 10, 10]]
print("blurred center row:", box_blur(img)[2])

try:
    import cv2
    import numpy as np
    arr = np.array(img, dtype="uint8")
    print("cv2 Gaussian blur center:", cv2.GaussianBlur(arr, (3, 3), 0)[2].tolist())
    print("cv2 Canny edges shape:", cv2.Canny(arr, 50, 150).shape)
except ImportError:
    print("OpenCV not installed — run: pip install opencv-python")

print("\nDone! Tip: change values above and run again to learn by experiment.")
