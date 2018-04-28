import argparse
import os.path
import sys
import re
from collections import Counter


def load_text_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file:
        return file.read()


def get_ten_most_frequent_words(text):
    words = re.findall(r'[\w\']+', text.lower())
    return Counter(words).most_common(10)


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        help='a text file for analysis',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    filename = command_line_arguments.filename

    try:
        text_data = load_text_data(filename)
    except UnicodeDecodeError:
        sys.exit('text file has invalid format')

    if not text_data:
        sys.exit('file not found')


if __name__ == '__main__':
    main()
