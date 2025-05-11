def count_words(text):
    word_list = text.split()
    count = len(word_list)
    
    return count

def letter_count(text):
    letter_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def display_counts(letter_dict):
    letter_list = []
    for char, count in letter_dict.items():
        count_dict = {"char": char, "num": count}
        letter_list.append(count_dict)
    letter_list.sort(reverse=True, key=sort_on)
    for l in letter_list:
        char = l["char"]
        if char.isalpha():
            print(f"{char}: {l["num"]}")