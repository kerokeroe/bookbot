
    
def get_num_words(file):
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
    return len(words)

def get_char_num(file):
    characters ={}
    with open(file) as f:
        file_contents = f.read()
        for character in file_contents:
            if character.lower() not in characters:
                characters[character.lower()] = 1
            else: 
                characters[character.lower()] += 1
    return characters

def sort_on(character):
    return character["count"]

def sort(characters):
    sorted_chars = []
   
    for character in characters:
        if character.isalpha():
            sorted_chars.append({"character": character, "count": characters[character]})

    sorted_chars.sort(reverse=True, key=sort_on)
    
    return sorted_chars
