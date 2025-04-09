from stats import *

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    
    word_count_result = word_count(text)
    char_count_dict = character_count(text)
    
    # Call the new function to get sorted list of character dictionaries
    sorted_chars = sort_characters(char_count_dict)
    
    # Pass the sorted list to generate_report
    generate_report(book, word_count_result, sorted_chars)

if __name__ == "__main__":
    main()