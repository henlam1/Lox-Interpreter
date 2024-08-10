# Lox Interpreter

## Description
This project is a Lox interpreter written in Python. It can parse and execute Lox files. This project was made by following the craftinginterpreters book

## Table of Contents
- Installation
- Usage
- Running Tests

## Installation
Clone the repository:

```git clone https://github.com/henlam1/Lox-Interpreter.git```

## Usage
Run the main file

```python main.py <command> <path_to_file>```

- &lt;command&gt; : An argument that is tokenize, parse, or evaluate
- &lt;path_to_file&gt; : Path to the Lox file you want to interpret

Example usage

```python main.py parse test_files/parsing/arithmetic/mul_div.lox```

## Running Tests
To run the tests, use the following command

```pytest```
