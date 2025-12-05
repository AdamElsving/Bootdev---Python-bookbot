from stats import get_num_words

def get_book_text(file_path:str):

    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    print(f"Found {get_num_words(book_text)} total words")

main()