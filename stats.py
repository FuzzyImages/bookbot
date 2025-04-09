## Refactored functions into its own script ##

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


def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    print(characters)
