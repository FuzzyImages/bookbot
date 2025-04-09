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
    return count


def character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_characters(char_dict):

    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    return chars_list


def generate_report(book, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
