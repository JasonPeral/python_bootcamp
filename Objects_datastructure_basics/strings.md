- Strings are ordered sequences and because of that it means we can use INDEXING and SLICING to grab sub-sections of the string.
- Indexing notation uses [ bracket ] notation after the string (or variable assigned to the string)
- Indexing allows you to grab a single character within a string

---

### INDEXING

- Indexing use [ ] square brackets and a number index to indicate positions of what you wish to grab

For example:

```
String → H E L L O 
Index  → 0 1 2 3 4
```

- A good thing about Python is that there is reverse indexing so if we wanted to grab the last letter of a string but we don't know how long the string may be, we can use reverse indexing.

For example:

```
String → H   E  L    L  O 
Index  → 0  -4 -3 -2 -1
```

- We can just grab `-1` and it would be the last letter.

---

### SLICING

- Slicing allows you to grab a subsection of multiple characters, a ‘slice’ of the string.
- This has the following syntax:
    - `[START:STOP:STEP]`
    - `START` is a numerical index for the slice start.
    - `STOP` is the index you will go up to but NOT include.
    - `STEP` is the size of the jump you take.

---

### Practical Examples

#### Indexing

```python
#indexing
x = "testing"
# Grabbing the first letter indexing the first letter
print(x[0])
# Grabbing the last letter in the string without knowing how long the length of the string is
print(x[-1])
# Indexing the 3rd element of the string which should output the 't'
print(x[3])
```

#### Slicing

```python
#SLICING 
# slicing from the 3rd element to the end
print(x[3:])
# slicing from the start to the 5th element but not including the 5th element
print(x[:5])
# slicing a range 
print(x[2:5])
```

### STEP SIZE

```python
#STEP SIZE
#we can choose how many elements we want to step by 
#this is slicing through all elements 
#Output would be TSIG with our string being "testing"
print(x[::2])
#Python trick to reverse a string instead of creating a loop
#output: gnitset
print(x[::-1])
