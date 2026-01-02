def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_dict = {}
    for char in text:
        if char.lower() in char_dict:
            char_dict[char.lower()] += 1
        else:
            char_dict[char.lower()] = 1
    return char_dict

def get_num_for_entry(entry):
    return entry["num"]

def get_char_list(char_dict):
    char_list = []
    for key in char_dict:
        if not key.isalpha():
            continue
        
        char_entry = {
            "char": key,
            "num": char_dict[key],
        }

        char_list.append(char_entry)
    
    char_list.sort(key = get_num_for_entry, reverse = True)

    return char_list