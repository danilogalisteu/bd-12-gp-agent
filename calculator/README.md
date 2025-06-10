# Calculator App

A simple calculator application that evaluates arithmetic expressions provided as command-line arguments.

## Functionality

The calculator supports the following operations:

*   Addition (+)
*   Subtraction (-)
*   Multiplication (*)
*   Division (/)

It evaluates expressions in infix notation, respecting operator precedence (multiplication and division have higher precedence than addition and subtraction).

## Usage

To use the calculator, run the `main.py` file with the expression as a command-line argument:

```bash
python main.py "expression"
```

For example:

```bash
python main.py "3 + 5"
```

```bash
python main.py "10 * 2 - 4 / 2"
```

## Example

Input:

```bash
python main.py "1 + 2 * 3"
```

Output:

```
Expression: 1 + 2 * 3
Result: 7.0
```

## Error Handling

The calculator provides error messages for invalid expressions, such as:

*   Invalid tokens
*   Not enough operands for an operator

## Limitations

*   The expression must be in infix notation with space-separated tokens.
*   No explicit expression size limit other than available memory.

## Dependencies

*   This application requires Python 3.
