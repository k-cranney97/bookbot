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

