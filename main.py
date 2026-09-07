import sys
from puncta import collapse_spaces, fix_punctuation_space
from caps import capitalize
from quotes import fix_quotes

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py input.txt output.txt")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]

    with open(input, "r", encoding="utf-8") as f:
        text = f.read()

    text = collapse_spaces(text)
    text = fix_quotes(text)
    text = fix_punctuation_space(text)
    text = capitalize(text)

    with open(output, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()