# Codewars Solutions

A collection of solutions to Codewars programming challenges, showcasing problem-solving skills, algorithm implementation, and Python proficiency across various difficulty levels.

## Project Overview

This repository contains solutions to Codewars kata challenges, demonstrating the ability to solve diverse programming problems, from beginner fundamentals to advanced algorithmic challenges. Each solution includes the problem description and efficient implementation.

## Tech Stack

- **Python** - 100%

## About Codewars

[Codewars](https://www.codewars.com) is a coding challenge platform with challenges organized by difficulty levels:

- **8 kyu** - Beginner
- **7 kyu** - Elementary
- **6 kyu** - Intermediate
- **5 kyu** - Advanced
- **4 kyu** - Very Advanced
- **3 kyu** - Expert
- **2 kyu** - Master
- **1 kyu** - Sensei

## Repository Structure

```
Codewars-Solutions/
├── 8_kyu/
│   ├── hello_world.py
│   ├── arithmetic_operations.py
│   └── ...
├── 7_kyu/
│   ├── string_manipulation.py
│   ├── list_operations.py
│   └── ...
├── 6_kyu/
│   ├── algorithms.py
│   ├── regex_patterns.py
│   └── ...
├── 5_kyu/
│   └── ...
├── solutions/
│   └── (solution files organized by topic)
├── tests/
│   └── test_solutions.py
├── README.md
└── requirements.txt
```

## Challenge Categories

### Fundamentals (8-7 kyu)
- Basic arithmetic operations
- String manipulation
- List operations
- Conditional logic
- Loop structures
- Variable assignment

### Intermediate (6 kyu)
- Algorithm implementation
- Data structure manipulation
- Pattern matching
- Recursion
- Regular expressions
- Function composition

### Advanced (5 kyu and higher)
- Complex algorithms
- Dynamic programming
- Graph algorithms
- Optimization problems
- Advanced data structures

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/prellwitzdarian/Codewars-Solutions.git
cd Codewars-Solutions
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Sample Solutions

### 8 kyu: Sum of Positive Numbers

**Problem**: Return the sum of positive numbers in a list.

```python
def sum_positives(arr):
    """
    Sum all positive numbers in the array.
    
    Args:
        arr: List of integers
    
    Returns:
        Sum of positive numbers
    """
    return sum(x for x in arr if x > 0)

# Test cases
assert sum_positives([1, 3, -2, 5]) == 9
assert sum_positives([-1, -3, -2]) == 0
assert sum_positives([]) == 0
```

### 7 kyu: String Repeat

**Problem**: Repeat a string n times.

```python
def repeat_str(s, n):
    """
    Repeat string s exactly n times.
    
    Args:
        s: String to repeat
        n: Number of times to repeat
    
    Returns:
        Repeated string
    """
    return s * n

# Test cases
assert repeat_str("ab", 3) == "ababab"
assert repeat_str("x", 5) == "xxxxx"
```

### 6 kyu: Find the Odd One Out

**Problem**: Find the element in the array that occurs an odd number of times.

```python
def find_odd(arr):
    """
    Find the number that occurs an odd number of times.
    
    Args:
        arr: List of integers
    
    Returns:
        Integer occurring odd times
    """
    result = 0
    for num in arr:
        result ^= num  # XOR operation
    return result

# Test cases
assert find_odd([1, 2, 2, 3, 3, 3, 4, 4]) == 3
assert find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
```

### 5 kyu: Human Readable Time

**Problem**: Convert seconds to HH:MM:SS format.

```python
def format_duration(seconds):
    """
    Convert seconds to human-readable time format.
    
    Args:
        seconds: Total seconds
    
    Returns:
        Time in format like "1 hour, 2 minutes and 3 seconds"
    """
    if seconds == 0:
        return "0 seconds"
    
    units = [("year", 31536000), ("day", 86400), 
             ("hour", 3600), ("minute", 60), ("second", 1)]
    
    parts = []
    for unit, duration in units:
        value = seconds // duration
        if value > 0:
            plural = "s" if value > 1 else ""
            parts.append(f"{value} {unit}{plural}")
            seconds %= duration
    
    if len(parts) == 1:
        return parts[0]
    return ", ".join(parts[:-1]) + f" and {parts[-1]}"

# Test cases
assert format_duration(0) == "0 seconds"
assert format_duration(5) == "5 seconds"
assert format_duration(86461) == "1 day, 1 minute and 1 second"
```

## Problem-Solving Approaches

### 1. Brute Force
- Simple, straightforward solution
- May not be optimal for large inputs
- Good for understanding the problem

```python
def is_palindrome(s):
    return s == s[::-1]
```

### 2. Optimization
- More efficient algorithms
- Better time/space complexity
- Uses data structures wisely

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### 3. Built-in Functions
- Leverage Python's powerful standard library
- Cleaner and more readable code
- Often optimized in C

```python
def is_palindrome(s):
    return s == s[::-1]
```

## Testing Solutions

Run all tests:
```bash
pytest tests/ -v
```

Run specific test file:
```bash
pytest tests/test_8_kyu.py -v
```

Run with coverage:
```bash
pytest --cov=solutions tests/
```

## Common Topics

### String Manipulation
- Case conversion
- Character counting
- Pattern matching
- Substring operations
- String reversal

### List Operations
- Sorting and filtering
- Searching and indexing
- Merging and zipping
- List comprehensions
- Set operations

### Algorithms
- Fibonacci sequence
- Prime numbers
- Factorial calculations
- GCD/LCM
- Sorting algorithms

### Mathematics
- Number theory
- Combinatorics
- Geometry
- Statistics
- Modular arithmetic

## Tips for Solving Katas

1. **Read carefully**: Understand all requirements
2. **Edge cases**: Consider boundary conditions
3. **Test**: Verify with multiple test cases
4. **Optimize**: Look for more efficient solutions
5. **Refactor**: Clean up code for readability
6. **Learn**: Study other solutions after solving

## Performance Optimization

### Time Complexity Improvements
```python
# O(n²) - Naive approach
def find_duplicates_naive(arr):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                result.append(arr[i])
    return result

# O(n) - Optimized approach
def find_duplicates_optimized(arr):
    seen = set()
    result = []
    for num in arr:
        if num in seen and num not in result:
            result.append(num)
        seen.add(num)
    return result
```

### Space Complexity Awareness
```python
# High space usage
def count_frequency(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency

# Better space usage (if only need to iterate once)
from collections import Counter
def count_frequency(arr):
    return Counter(arr)
```

## Python Features Used

- List comprehensions
- Generator expressions
- Lambda functions
- Decorators
- Context managers
- String formatting
- Regular expressions
- Collections module
- Itertools
- Functools

## Learning Resources

### Recommended Kata Progression

1. Start with 8 kyu basics
2. Master string and list operations (7 kyu)
3. Learn algorithms and patterns (6 kyu)
4. Practice optimization (5 kyu)
5. Explore advanced topics (4 kyu+)

### External Resources

- [Python Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Algorithm Visualization](https://visualgo.net/)
- [Big O Complexity](https://www.bigocheatsheet.com/)

## Common Patterns

### Higher-Order Functions
```python
# Map, filter, reduce
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
evens = filter(lambda x: x % 2 == 0, numbers)
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
```

### Recursion
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Dynamic Programming
```python
def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Contributing

To add new solutions:

1. Create a file in appropriate difficulty folder
2. Include problem description
3. Add multiple solutions (when applicable)
4. Include comprehensive test cases
5. Add comments explaining approach

## Checklist for New Solutions

- [ ] Problem description included
- [ ] Solution is well-commented
- [ ] Multiple approaches shown (if applicable)
- [ ] Test cases included
- [ ] Edge cases handled
- [ ] Time complexity noted
- [ ] Space complexity noted

## Statistics

- **Total Solutions**: [Add count]
- **8 kyu**: [Add count]
- **7 kyu**: [Add count]
- **6 kyu**: [Add count]
- **5 kyu+**: [Add count]

## License

This project is provided as-is for educational purposes.

## Author

Created by Darian Prellwitz

## Codewars Profile

Visit my Codewars profile: [Profile Link]

---

**Last Updated:** April 2026

**Current Streak**: [Add info]

**All Solutions Count**: [Add count]
