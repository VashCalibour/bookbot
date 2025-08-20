import sys

from stats import (
    word_count,
    character_count,
    sort_characters,

)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)
    number_of_words = word_count(book_contents)
    letter_count = character_count(book_contents)
    sorted_char_list = sort_characters(letter_count)
        
    print(f"{number_of_words} words found in the document")
    print(letter_count)
    print_report(book_path, number_of_words, sorted_char_list)

def get_book_text(filepath):
    with open(filepath) as text:
        file_contents = text.read()
    return file_contents

def print_report(book_path, number_of_words, sorted_char_list):
    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {number_of_words} total words")
    print("-------- Character Count ---------")
    for item in sorted_char_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ================")
    

main()
