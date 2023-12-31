# Module to handle command-line arguments and options
import argparse
# Importing the sys module which contains exit function
import sys


def count_words(text):
    """Function counting words"""
    words = text.split()
    return len(words)


def count_lines(text):
    """Function counting lines"""
    lines = text.split("\n")
    return len(lines)


def count_characters(text):
    """Counting characters in input text"""
    return len(text)


def read_text_from_file(file_path):
    """Function reading text from a file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None


if __name__ == "__main__":  # run the following code only if the code is used as a script
    parser = argparse.ArgumentParser(description="My awesome word count tool")
    parser.add_argument("input_text", nargs="?",
                        help="The input text for word and line count")
    parser.add_argument("-l", "--lines", action="store_true",
                        help="Count number of lines")
    parser.add_argument("-c", "--characters",
                        action="store_true", help="Count characters")
    parser.add_argument("-f", "--file", help="Read input text from file")
    args = parser.parse_args()

    if args.file:
        input_text = read_text_from_file(args.file)
        if input_text is None:
            sys.exit(1)
    else:
        input_text = args.input_text

    if not args.lines and not args.characters:
        # If no specific option is provided, count all metrics
        word_count = count_words(input_text)
        line_count = count_lines(input_text)
        char_count = count_characters(input_text)

        print("Word count:", word_count)
        print("Line count:", line_count)
        print("Character count:", char_count)
    else:
        if args.lines:
            line_count = count_lines(input_text)
            print("Line count:", line_count)
        if args.characters:
            char_count = count_characters(input_text)
            print("Character count:", char_count)
