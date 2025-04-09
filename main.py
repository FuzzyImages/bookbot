from stats import *

def main():
    book = "books/frankenstein.txt"

    text = get_book_text(book)
    word_count(text)
    character_count(text)
    

if __name__ == "__main__":
    main()