import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
imported_book = sys.argv[1]

def get_book_text(book):
    book_contents = book.read()
    from stats import word_count, sort_char_count
    num_words, char_count = word_count(book_contents)
    sorted_list = sort_char_count(char_count)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print(f"--------- Character Count -------")
    for letter in sorted_list:
        if letter["char"].isalpha() == True:
            print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")
    return

def main():
    with open(imported_book) as book:
        get_book_text(book)
        return
    return

main()