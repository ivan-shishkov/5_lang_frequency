import argparse


def load_data(filepath):
    pass


def get_most_frequent_words(text):
    pass


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


if __name__ == '__main__':
    main()
