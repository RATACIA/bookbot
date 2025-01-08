import re

def count_char(text):
    char_count={}
    for char in re.findall(r'[a-z]',text.lower()):
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count
    
# end def
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        char_count = count_char(file_contents)
        char_count_sorted = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
        print ('--- Begin report of books/frankenstein.txt ---')
        print(f"{len(words)} words found in the document")
        for char,count in char_count_sorted:
            print(f"The '{char}' character was found {count} times")

main()