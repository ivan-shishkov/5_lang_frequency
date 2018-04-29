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


def print_most_frequent_words(words_counter):
    print()
    print('{:^40}'.format('Most frequent words in text'))
    print('{:-<40}'.format(''))
    print('| {:^24} | {:^9} |'.format('Word', 'Count'))
    print('{:-<40}'.format(''))

    for word, count in words_counter:
        print('| {:24} | {:^9} |'.format(word, count))
        print('{:-<40}'.format(''))


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filename',
        help='an analyzed text file in UTF-8 encoding',
        type=str,
    )

    command_line_arguments = parser.parse_args()

    return command_line_arguments


def main():
    command_line_arguments = parse_command_line_arguments()

    filename = command_line_arguments.filename

    try:
        text = load_text_data(filename)
    except UnicodeDecodeError:
        sys.exit('text file has invalid format')

    if text is None:
        sys.exit('file not found')

    if not text:
        sys.exit('file is empty')

    print_most_frequent_words(
        words_counter=get_ten_most_frequent_words(text),
    )


if __name__ == '__main__':
    main()
