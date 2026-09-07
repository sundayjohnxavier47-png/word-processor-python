# word-processor-python

A command-line tool written in Python that cleans up text: fixes punctuation spacing, normalizes quote spacing, collapses multiple spaces, and capitalizes the first letter of each sentence.

## Features

- Removes extra spaces before punctuation (`, . ! ? : ; /`) and ensures exactly one space after
- Collapses multiple consecutive punctuation marks correctly (e.g. `. . .` → `...`)
- Fixes spacing inside single and double quotes (e.g. `" hello "` → `"hello"`)
- Collapses multiple spaces between words into one
- Capitalizes the first letter of each sentence (after `. ! ?` or a new line)

## Usage

```bash
python3 main.py input.txt output.txt
```

Reads text from `input.txt`, applies all fixes, and writes the result to `output.txt`.

## Example

**Input:**
hello , world !
this is a test .

**Output:**
Hello, world!
This is a test.


## Project structure

- `main.py` — entry point, handles file I/O and calls the fix functions in sequence
- `puncta.py` — punctuation spacing and space-collapsing logic
- `caps.py` — sentence capitalization logic
- `quotes.py` — quote spacing logic

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

No external packages are required — everything uses Python's standard library.

## Notes

This is the Python version of [word-processor-go](https://github.com/sundayjohnxavier47-png/word-processor-go.git), built as a separate portfolio piece to demonstrate the same logic in a different language.