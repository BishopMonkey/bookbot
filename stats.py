def word_count(book_string):
    num_words = len(book_string.split())
    lower_num_words = book_string.lower()
    char_counts = {}
    for char in lower_num_words:
        char_counts[char] = char_counts.get(char, 0) + 1
    return (num_words, char_counts)

def sort_char_count(char_counts):
    sorted_list = [{"char": char, "num": num} for char, num in char_counts.items()]
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return (sorted_list)