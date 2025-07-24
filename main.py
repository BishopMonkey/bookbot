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
    with open("books/frankenstein.txt") as book:
        get_book_text(book)
    return

main()