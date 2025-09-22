from stats import num_of_words
from stats import count_letters
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    num_letters = count_letters(text)
    print(f"{num_words} words found in the document")
    print(num_letters)


def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

main()
