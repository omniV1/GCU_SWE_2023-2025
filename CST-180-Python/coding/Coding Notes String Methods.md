![[Pasted image 20250922151039.png]]


![[Pasted image 20250922151058.png]]

![[Pasted image 20250922151316.png]]

![[Pasted image 20250922151333.png]]

![[Pasted image 20250922151341.png]]

![[Pasted image 20250922151353.png]]

# Python String Methods - Actually Understandable Guide

## The Big Picture First

Strings in Python are **immutable** - you can't change them. When you "modify" a string, you're actually creating a new one. Think of it like this: if you have a sticky note with "Hello" written on it, you can't erase and rewrite it - you have to get a new sticky note.

## 1. Finding Stuff in Strings

### The Simple Way: `in` operator

```python
text = "I love pizza"
if "pizza" in text:
    print("Found pizza!")  # This runs
```

Use `in` when you just want to know: "Is this substring somewhere in my string?"

### When You Need the Exact Location: `.find()`

```python
text = "I love pizza and more pizza"
position = text.find("pizza")
print(position)  # Output: 7 (first occurrence)

# If not found, returns -1
position = text.find("burgers")
print(position)  # Output: -1
```

**Key Point:** `.find()` returns a number (the index), not True/False!

- Found → returns the position (0, 1, 2, etc.)
- Not found → returns -1

This is why `if text.find("something"):` can fail! If "something" is at position 0, that's falsy in Python.

### Finding the LAST Occurrence: `.rfind()`

```python
text = "I love pizza and more pizza"
last_position = text.rfind("pizza")
print(last_position)  # Output: 22 (last occurrence)
```

### Counting Occurrences: `.count()`

```python
text = "banana"
count = text.count("a")
print(count)  # Output: 3
```

## 2. Replacing Stuff

### Basic Replace: `.replace(old, new)`

```python
text = "I hate broccoli"
new_text = text.replace("hate", "love")
print(new_text)  # Output: "I love broccoli"

# Original string is unchanged!
print(text)  # Still: "I hate broccoli"
```

**Remember:** You MUST store the result! `.replace()` doesn't change the original string.

### Replace Only Some Occurrences: `.replace(old, new, count)`

```python
text = "ha ha ha ha"
new_text = text.replace("ha", "he", 2)  # Replace first 2 only
print(new_text)  # Output: "he he ha ha"
```

## 3. Checking String Properties (True/False methods)

These all return `True` or `False`:

```python
text = "Hello123"
print(text.isalnum())    # True (letters + numbers only)
print(text.isdigit())    # False (not all digits)
print(text.islower())    # False (has uppercase H)
print(text.isupper())    # False (has lowercase letters)

text2 = "   \n  "
print(text2.isspace())   # True (only whitespace)

text3 = "Hello World"
print(text3.startswith("Hello"))  # True
print(text3.endswith("World"))    # True
```

## 4. Changing Case

```python
text = "Hello World"
print(text.lower())      # "hello world"
print(text.upper())      # "HELLO WORLD"
print(text.capitalize()) # "Hello world" (first letter only)
print(text.title())      # "Hello World" (each word capitalized)
```

## 5. Cleaning Up Whitespace

```python
text = "   hello world   "
print(text.strip())      # "hello world" (removes spaces from ends)
print(text)              # Still "   hello world   " (original unchanged)
```

## Common Patterns

### Reading User Input Safely

```python
name = input("Enter your name: ").strip().lower()
# This removes extra spaces AND makes it lowercase for easy comparison
```

### Checking if Something Was Found

```python
text = "Hello world"
position = text.find("world")
if position != -1:  # Found!
    print(f"Found at position {position}")
else:
    print("Not found")
```

### The Right Way to Check for Existence

```python
# Good - just checking if it exists
if "pizza" in text:
    do_something()

# Bad - unnecessarily complex
if text.find("pizza") != -1:
    do_something()
```

## Solving Your Homework Problems

### Problem Pattern: "Find and Replace"

```python
# Read inputs
target = input()
sentence = input()

# Check if target exists
if target in sentence:
    # Find the position
    index = sentence.find(target)  # or .rfind() for last
    
    # Do the replacement
    new_sentence = sentence.replace(target, "replacement")
    
    # Print results
    print(f"Found at index: {index}")
    print(new_sentence)
else:
    print("Not found")
```

### Key Debugging Tips

1. **Store method results:** `new_text = old_text.replace(...)`
2. **Check for -1:** `if position != -1:` not `if position:`
3. **Use the right method:** `in` for existence, `.find()` for position
4. **Remember immutability:** String methods return NEW strings

### Why Your Code Broke

- Using `.find()` in an `if` statement when the result could be 0
- Not storing the result of methods like `.replace()`
- Using commas in `print()` which adds extra spaces
- Forgetting that strings don't change - you need to save the new result

This way of thinking about strings - as immutable objects where methods return NEW strings - will make everything click!