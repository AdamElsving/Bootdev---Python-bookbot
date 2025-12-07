from stats import get_num_words, get_count_characters, get_sorted_characters
import sys

def get_book_text(file_path:str):

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words\n")

    character_count = get_count_characters(book_text)
    character_dicts = get_sorted_characters(character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    for dict in character_dicts:
        if dict['char'].isalpha():  
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()