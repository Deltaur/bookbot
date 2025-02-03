def open_book(book):
    with open(book) as f:
        file_contents = f.read()    
    return file_contents

def count_words(text):
    words = text.lower()
    chars = {}
    for word in words:
        for char in word:
            if char in chars: 
                chars[char] += 1
            else:
                chars[char] = 1
    return chars
    
def report(data):
    for letter in data:
        if letter.isalpha() == True: print(f"The '{letter}' character was found {data[letter]} times")
    print("--- End report ---")

def main():
    text = open_book("books/frankenstein.txt")
    data = count_words(text)
    print(report(data))
    
main()
