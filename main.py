from stats import *
import sys


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main(file_path) -> str:
    text = get_book_text(file_path)
    return text


def report(filepath):
    text = main(filepath)
    wrd_count = count_words(text)
    display_dict = letter_count(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + filepath)
    print("----------- Word Count ----------")
    print(f"Found {wrd_count} total words")
    print("--------- Character Count -------")
    display_counts(display_dict)
    print("============= END ===============")


report(filepath)