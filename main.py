from stats import get_num_words, get_count_characters

def get_book_text(file_path:str):

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words\n")

    character_count = get_count_characters(book_text)
    print(character_count)

main()