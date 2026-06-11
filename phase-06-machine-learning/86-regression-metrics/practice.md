# 86 — Regression Metrics: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Compute MAE for preds [2,4] vs truth [3,5].

*Hint: Mean abs error.*

<details>
<summary>✅ Solution</summary>

```python
t, p = [3, 5], [2, 4]
print(sum(abs(a - b) for a, b in zip(t, p)) / len(t))  # 1.0
```

</details>

## Exercise 2

Compute MSE for the same.

*Hint: Mean sq error.*

<details>
<summary>✅ Solution</summary>

```python
t, p = [3, 5], [2, 4]
print(sum((a - b) ** 2 for a, b in zip(t, p)) / len(t))  # 1.0
```

</details>

## Exercise 3

Compute RMSE when MSE=9.

*Hint: sqrt.*

<details>
<summary>✅ Solution</summary>

```python
print(9 ** 0.5)  # 3.0
```

</details>

## Exercise 4

Compute R^2 when SS_res=2, SS_tot=8.

*Hint: 1 - res/tot.*

<details>
<summary>✅ Solution</summary>

```python
print(1 - 2 / 8)  # 0.75
```

</details>

## Exercise 5

Which metric is most robust to outliers?

*Hint: Linear penalty.*

<details>
<summary>✅ Solution</summary>

**MAE** — it weights errors linearly, so a single huge error doesn't dominate like
it does in MSE/RMSE (which square the error).

</details>

## Exercise 6

What does a negative R^2 indicate?

*Hint: Worse than mean.*

<details>
<summary>✅ Solution</summary>

The model predicts **worse than simply using the mean** of the target. SS_res >
SS_tot, so 1 − SS_res/SS_tot < 0.

</details>

## Exercise 7

Compute MAPE for true=[100,200], pred=[110,180].

*Hint: Mean abs % error.*

<details>
<summary>✅ Solution</summary>

```python
t, p = [100, 200], [110, 180]
print(sum(abs(a - b) / a for a, b in zip(t, p)) / len(t))  # 0.1
```

</details>

## Exercise 8

Why prefer RMSE over MSE for reporting?

*Hint: Units.*

<details>
<summary>✅ Solution</summary>

**RMSE is in the same units as the target** (MSE is squared units), so it's directly
interpretable — e.g. 'off by ~3 dollars' rather than '9 dollars-squared'.

</details>

