def num_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    character = {}
    for ch in text.lower():
        if ch in character:
            character[ch] += 1
        else:
            character[ch] = 1
    return character

def sort_on(dictionary):
    return dictionary["num"]

def sort_list(num_letters):
    ordered_list = []
    for char, num in num_letters.items():
        dictionary = {"char": char, "num": num}
        ordered_list.append(dictionary)
    ordered_list.sort(reverse = True, key=sort_on)
    return ordered_list






