def main():
    book = "books/frankenstein.txt"
    text = get_book(book)
    num_words = word_count(text)
    print(f"--- Begin report of {book} ---\n")
    print(f"There are {num_words} in this book.\n")
    character_report(count_characters(text))
    print(f"\nend report")


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


def character_report(character_dict):

    character_list = []

    for character in character_dict:
        if character.isalpha():
            new_char = {}
            new_char["character"] = character
            new_char["num"] = character_dict[character]
            character_list.append(new_char)

    character_list.sort(reverse=True, key=sort_on)

    for character in character_list:
        print(f"The '{character["character"]}' character was found {character["num"]} times")


def sort_on(dict):
    return dict["num"]


def test_type(text):
    print(type(text))


def get_book(book):

    with open(book) as f:
        text = f.read()
    return text


main()