import sys
from stats import get_num_words, get_char_counts, get_char_list

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    # print(f"Found {num_words} total words")
    char_counts = get_char_counts(book_text)
    # print(char_counts)
    char_list = get_char_list(char_counts)
    # print(char_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in char_list:
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")



main()