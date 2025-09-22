from stats import num_of_words
from stats import count_letters
from stats import sort_list
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    num_letters = count_letters(text)
    sorted_list = sort_list(num_letters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_list:
        char = dictionary["char"]
        num = dictionary["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

main()
