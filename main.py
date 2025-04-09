
def main():
    book = "books/frankenstein.txt"

    text = get_book_text(book)
    word_count(text)


def get_book_text(book):
    with open(book) as b:
        text = b.read() 
    return text


def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    print(f"{count} words found in the document")
    

if __name__ == "__main__":
    main()