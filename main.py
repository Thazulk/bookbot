from stats import get_num_words
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = count_letters(text)
    # print(f"Found {num_words} total words")
    report_text(num_letters, num_words, book_path)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    counted_letters = {}
    low_text = text.lower()
    for letter in low_text:
        if letter in counted_letters:
            counted_letters[letter] += 1
        else:
            counted_letters[letter] = 1
    return counted_letters


def sort_on(dict):
    return dict["num"]


def report_text(letters, words, path):
    letters_dict = []

    for letter, num in letters.items():
        if letter.isalpha():
            letters_dict.append({"name": letter, "num": num})
    letters_dict.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for item in letters_dict:
        print(f"{item['name']}: {item['num']}")

    print("============= END ===============")


main()

