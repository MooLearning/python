# 35 — Stacks: Practice

Solve top to bottom (easy → hard). Attempt each problem yourself, then expand **Solution** to check.

## Exercise 1

Implement push, pop, and peek using a list.

*Hint: append/pop/[-1].*

<details>
<summary>✅ Solution</summary>

```python
st = []
st.append(1); st.append(2)
print(st[-1])      # peek -> 2
print(st.pop())    # 2
print(st)          # [1]
```

</details>

## Exercise 2

Reverse the string 'stack' using a stack.

*Hint: Push all, then pop all.*

<details>
<summary>✅ Solution</summary>

```python
def reverse(s):
    st = list(s)
    out = []
    while st:
        out.append(st.pop())
    return "".join(out)
print(reverse("stack"))  # kcats
```

</details>

## Exercise 3

Check if '(()())' has balanced parentheses.

*Hint: Push '(' , pop on ')'.*

<details>
<summary>✅ Solution</summary>

```python
def balanced(s):
    n = 0
    for c in s:
        if c == "(": n += 1
        elif c == ")":
            n -= 1
            if n < 0: return False
    return n == 0
print(balanced("(()())"))  # True
```

</details>

## Exercise 4

Use a stack to decide if 'abba' reads the same backward.

*Hint: Compare with popped half.*

<details>
<summary>✅ Solution</summary>

```python
def is_pal(s):
    st = list(s)
    for c in s:
        if c != st.pop(): return False
    return True
print(is_pal("abba"))  # True
```

</details>

## Exercise 5

Evaluate the RPN expression '5 1 2 + 4 * + 3 -'.

*Hint: Stack of operands.*

<details>
<summary>✅ Solution</summary>

```python
def rpn(tokens):
    st = []
    for t in tokens.split():
        if t in "+-*/":
            b, a = st.pop(), st.pop()
            st.append({"+":a+b,"-":a-b,"*":a*b,"/":a//b}[t])
        else:
            st.append(int(t))
    return st.pop()
print(rpn("5 1 2 + 4 * + 3 -"))  # 14
```

</details>

## Exercise 6

Find the next greater element for each item in [2,1,2,4,3].

*Hint: Monotonic stack.*

<details>
<summary>✅ Solution</summary>

```python
def next_greater(a):
    res = [-1] * len(a)
    st = []                      # holds indices, values decreasing
    for i, x in enumerate(a):
        while st and a[st[-1]] < x:
            res[st.pop()] = x
        st.append(i)
    return res
print(next_greater([2, 1, 2, 4, 3]))  # [4, 2, 4, -1, -1]
```

</details>

## Exercise 7

Implement a stack with a max() operation in O(1).

*Hint: Track maxes alongside.*

<details>
<summary>✅ Solution</summary>

```python
class MaxStack:
    def __init__(self):
        self.data = []; self.maxes = []
    def push(self, x):
        self.data.append(x)
        self.maxes.append(x if not self.maxes else max(x, self.maxes[-1]))
    def pop(self):
        self.maxes.pop(); return self.data.pop()
    def get_max(self):
        return self.maxes[-1]
s = MaxStack()
for x in [3, 1, 5, 2]: s.push(x)
print(s.get_max())  # 5
```

</details>

## Exercise 8

Decode '3[ab]2[c]' -> 'abababcc' using a stack.

*Hint: Push counts and partial strings.*

<details>
<summary>✅ Solution</summary>

```python
def decode(s):
    num = 0; cur = ""; stack = []
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num)); cur = ""; num = 0
        elif ch == "]":
            prev, k = stack.pop(); cur = prev + cur * k
        else:
            cur += ch
    return cur
print(decode("3[ab]2[c]"))  # abababcc
```

</details>

