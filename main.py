def main():
    book = "books/frankenstein.txt"
    text = get_book(book)
    num_words = word_count(text)
    print("--- Begin report of {book} ---\n")
    print(f"There are {num_words} in this book.")
    character_count = count_characters(text)
    print(character_count)
    
    print(f"report END")


def word_count(text):

    words = text.split()
    return(len(words))


def count_characters(text):

    characters = {}
    for character in text:
        character = character.lower()
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def test_type(text):
    print(type(text))


def get_book(book):

    with open(book) as f:
        text = f.read()
    return text

main()