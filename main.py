from stats import count_words, letter_count

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def main(file_path) -> str:
    text = get_book_text(file_path)
    return text



text = main("books/frankenstein.txt")
count_words(text)
print(letter_count(text))