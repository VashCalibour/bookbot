def word_count(book_contents):
    word_list = []
    words = book_contents.split()
    word_list = words
    return len(word_list)

def character_count(book_contents):
    pro_dictionary = {}
    lowercase_list = []
    for contents in book_contents:
        lowercase_string = contents.lower()
        lowercase_list.append(lowercase_string)
    for letters in lowercase_list:
        if letters in pro_dictionary:
            pro_dictionary[letters] += 1
        else:
            pro_dictionary[letters] = 1
    return pro_dictionary

def sort_on(d):
    return d["num"]
        
def sort_characters(letter_count):
    sorted_list = []
    for char in letter_count:
        sorted_list.append({"char": char, "num": letter_count[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    

