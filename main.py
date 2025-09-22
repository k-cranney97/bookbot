from stats import num_of_words
from stats import count_letters
from stats import sort_list
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    num_letters = count_letters(text)
    sorted_list = sort_list(num_letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
