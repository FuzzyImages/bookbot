
def main():
    book = "books/frankenstein.txt"

    get_book_text(book)


def get_book_text(book):
    with open(book) as b:
        text = b.read() 
    print(text)


if __name__ == "__main__":
    main()