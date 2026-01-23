
# Python Notes – Data Types & Operators

---

## Special Operators in Python

Python provides **special operators**:

1. **Membership operators**
2. **Identity operators**

---

## Identity Operators

Identity operators are used to determine whether two variables refer to the **same object in memory**, not just equal values.

### Operators

* `is`
* `is not`

### Example

```python
x = 10
y = 10

x is y      # True (same object)
x is not y  # False
```

---

## Membership Operators

Membership operators are used to test whether a **value exists inside a sequence**.

### Applicable to:

* String
* List
* Tuple
* Set
* Dictionary

### Operators

* `in`
* `not in`

### Example

```python
x = "Hello World"
y = {1: 'a', 2: 'b'}

'H' in x          # True
'hello' not in x # True
1 in y            # True (checks keys)
'a' in y          # False
```

---

## Python Data Types

### Tuple

* Collection of **ordered and unchanged (immutable)** elements

```python
colors = ('red', 'blue', 'green')
```

---

### List

* Collection of **ordered and changeable (mutable)** elements

```python
fruits = ['apple', 'banana', 'cherry']
```

---

### Dictionary

* Collection of **key–value pairs**

```python
student = {
    "name": "Alex",
    "age": 20
}
```

---

## Operators

An **operator** is a symbol used to perform operations on data.

---

## Unary Operator

If an operator works on **only one operand**, it is called a **unary operator**.

### Example (Bitwise NOT)

```python
~6     # -7
~(-10) # 9
```

---

## Arithmetic Operators

Used to perform mathematical operations.

### Example

```python
x = 5
y = 6

x + y   # 11
x - y   # -1
x * y   # 30
x / y   # 0.8333
x // y  # 0
x % y   # 5
```

---

## Assignment Operators

Used to assign values to variables.

### Examples

```python
x = 5
x += 5   # x = x + 5
x -= 5   # x = x - 5
x *= 5   # x = x * 5
x /= 5   # x = x / 5
x %= 5   # x = x % 5
x **= 5  # x = x ** 5
x &= 5
x |= 5
x ^= 5
x >>= 5
x <<= 5
```

---

## Relational (Comparison) Operators

Used to compare two operands.
Result is always **True** or **False**.

### Operators

* `>`
* `<`
* `>=`
* `<=`
* `==`
* `!=`

### Example

```python
x = 5
y = 6

x > y    # False
x >= y   # False
x < y    # True
x <= y   # True
x == y   # False
x != y   # True
```

---

## Logical Operators

Used to combine multiple conditions.

### Operators

* `and`
* `or`
* `not`

### Example

```python
x = 5
y = 6

(x < y) and (x > 0)  # True
(x > y) or (x > 0)   # True
not(x > y)           # True
```

---

## Bitwise Operators

Bit-by-bit operations on integers.

### Operators

* `&`  (AND)
* `|`  (OR)
* `^`  (XOR)
* `~`  (NOT)
* `>>` (Right shift)
* `<<` (Left shift)

---

### Example

```python
5 & 3   # 1
5 | 3   # 7
5 ^ 3   # 6
5 << 1  # 10
5 >> 1  # 2
```

---