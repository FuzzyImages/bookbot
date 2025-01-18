def main():
    book = "books/frankenstein.txt"
    text = get_book(book)
    num_words = word_count(text)
    print("--- Begin report of {book} ---\n")
    print(f"There are {num_words} in this book.")
    print(f"report")


def word_count(text):

    words = text.split()
    return(len(words))


def test_type(text):
    print(type(text))


def get_book(book):

    with open(book) as f:
        text = f.read()
    return text

main()