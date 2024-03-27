def main(): 
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_letters = count_letters(text)
    report_text(num_letters, num_words, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
def count_words(text):
        words = text.split()
        return len(words)

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
    print(f" --- Begin report of {path} ---")
    print(f"{words} words found in the book")
    print("")

    for item in letters_dict:
        print(f"The '{item['name']}' character was found {item['num']} times")

    print(" --- End of report ---") 

main()