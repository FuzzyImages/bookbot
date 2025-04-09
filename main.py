from stats import *
import sys

def main():

    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = args[1]
    text = get_book_text(book)
    
    word_count_result = word_count(text)
    char_count_dict = character_count(text)
    
    # Call the new function to get sorted list of character dictionaries
    sorted_chars = sort_characters(char_count_dict)
    
    # Pass the sorted list to generate_report
    generate_report(book, word_count_result, sorted_chars)

if __name__ == "__main__":
    main()