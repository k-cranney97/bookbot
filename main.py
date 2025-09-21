def get_book_text(books):
    with open(books, encoding="utf-8") as book:
        return book.read() 
    
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()
