def words(f):
    return f.split()

def count_words(w):
    return len(words(w))


def count_letters(words):
    letters = dict()
    for word in words:
        word = word.lower() 
        for item in word:
            if item in letters:
                letters[item] += 1
            else:
                letters[item] = 1
    return letters

def print_char_report(letters_dict):
    sorted_letters_list = sorted(letters_dict.items(), key=lambda x:x[1], reverse=True)
    for each_tuple in sorted_letters_list:
        if each_tuple[0].isalpha():
            print(f"The '{each_tuple[0]}' character was found {each_tuple[1]} times")


file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()
    # print(file_contents)
    words = words(file_contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{len(words)} words found in the document")
    print()
    print()
    letters_dict = count_letters(words)
    print_char_report(letters_dict)
    