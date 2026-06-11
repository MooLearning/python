# 102 — Computer Vision with OpenCV: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Convert RGB [100,150,200] to grayscale (luminosity).

*Hint: Weighted sum.*

<details>
<summary>✅ Solution</summary>

```python
p = [100, 150, 200]
print(round(0.299 * p[0] + 0.587 * p[1] + 0.114 * p[2]))  # 142
```

</details>

## Exercise 2

Threshold [50,130,200] at 128 to binary.

*Hint: Compare.*

<details>
<summary>✅ Solution</summary>

```python
print([255 if v >= 128 else 0 for v in [50, 130, 200]])  # [0,255,255]
```

</details>

## Exercise 3

Brighten [200,250,100] by 30, clamped to 255.

*Hint: min(255, v+30).*

<details>
<summary>✅ Solution</summary>

```python
print([min(255, v + 30) for v in [200, 250, 100]])  # [230,255,130]
```

</details>

## Exercise 4

Flip the row [1,2,3,4] horizontally.

*Hint: Reverse.*

<details>
<summary>✅ Solution</summary>

```python
print([1, 2, 3, 4][::-1])  # [4, 3, 2, 1]
```

</details>

## Exercise 5

What color order does OpenCV use?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**BGR** (Blue, Green, Red) — not RGB. Convert with `cv2.cvtColor(img,
cv2.COLOR_BGR2RGB)` before displaying with RGB-based tools.

</details>

## Exercise 6

Average the 3 values [60,90,120] (1-D blur).

*Hint: Mean.*

<details>
<summary>✅ Solution</summary>

```python
print(sum([60, 90, 120]) // 3)  # 90
```

</details>

## Exercise 7

How is a grayscale image indexed: [x,y] or [row,col]?

*Hint: Recall.*

<details>
<summary>✅ Solution</summary>

**[row, col]** = **[y, x]** — the first index is the row (vertical), the second is
the column (horizontal).

</details>

## Exercise 8

Invert a pixel value 200 (255 - v).

*Hint: Negative.*

<details>
<summary>✅ Solution</summary>

```python
print(255 - 200)  # 55
```

</details>

