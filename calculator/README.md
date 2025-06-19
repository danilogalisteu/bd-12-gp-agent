# Calculator Application Documentation

## Introduction
The Calculator application is a Python-based command-line tool that evaluates arithmetic expressions. 

## Functionality
The calculator supports:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

It evaluates expressions in infix notation, respecting operator precedence (multiplication and division have higher precedence than addition and subtraction).

## Project Structure
```
calculator/
├── README.md          # Basic usage instructions
├── main.py            # Entry point
├── pkg/               # Core implementation
│   ├── calculator.py  # Expression evaluation logic
│   └── render.py      # Result formatting
└── tests.py           # Unit tests
```

## Core Functionality

### Calculator Class (`pkg/calculator.py`)
The `Calculator` class handles expression evaluation using the shunting-yard algorithm.

```python
class Calculator:
    def __init__(self):
        # Operator definitions with precedence
        self.operators = { ... }
        self.precedence = { ... }
    
    def evaluate(self, expression):
        # Main evaluation method
        ...
    
    def _evaluate_infix(self, tokens):
        # Implements shunting-yard algorithm
        ...
    
    def _apply_operator(self, operators, values):
        # Applies operators to operands
        ...
```

Key features:
- Supports +, -, *, / operations
- Follows standard operator precedence (* and / before + and -)
- Handles space-separated token expressions
- Converts tokens to floats for calculation

### Rendering Module (`pkg/render.py`)
Formats calculator output in a visually appealing box:

```python
def render(expression, result):
    # Creates formatted output box
    ...
```

Example output:
```
┌───────────┐
│ 3 + 5 * 2 │
│           │
│ =         │
│           │
│ 13.0      │
└───────────┘
```

### Main Entry Point (`main.py`)
Handles command-line input and output:

```python
def main():
    # Parses arguments and coordinates calculation
    ...
```

## Testing
The `tests.py` file contains comprehensive unit tests:

```python
class TestCalculator(unittest.TestCase):
    # Tests basic operations
    def test_addition(self): ...
    
    # Tests complex expressions
    def test_complex_expression(self): ...
    
    # Tests error handling
    def test_invalid_operator(self): ...
```

Test coverage includes:
- Basic arithmetic operations
- Operator precedence handling
- Complex nested expressions
- Error cases (invalid tokens, insufficient operands)
- Empty expression handling

## Usage
To use the calculator, run the `main.py` file with the expression as a command-line argument:

```bash
python main.py "expression"
```

Examples:
```bash
python main.py "3 + 5"
python main.py "10 * 2 - 4 / 2"
```

Input:
```bash
python main.py "1 + 2 * 3"
```

Output:
```
Expression: 1 + 2 * 3
Result: 7.0
```

Additional examples:
```bash
python main.py "5 + 3 * 2"      # Output: 11.0
python main.py "10 / 2 - 1"     # Output: 4.0
```

## Error Handling
The calculator provides error messages for:
- Invalid tokens
- Not enough operands for an operator
- Empty expressions (returns None without crashing)
- Division by zero (handled by Python's built-in exception)

## Limitations
1. Requires space-separated tokens (e.g., "3+5" won't work)
2. Only supports basic arithmetic operations
3. No support for parentheses or advanced functions
4. Limited to single-line expressions
5. Output formatting breaks with very long expressions
6. No explicit expression size limit other than available memory

## Dependencies
* This application requires Python 3.
