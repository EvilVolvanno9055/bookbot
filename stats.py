def count_words(text):
    word_list = text.split()
    count = len(word_list)
    
    print(f"{count} words found in the document")

def letter_count(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    print(letter_dict)


