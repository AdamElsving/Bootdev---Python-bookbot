def get_num_words(text:str) -> int:
    return len(text.split())

def get_count_characters(text:str):
    lower_cased = text.lower()
    char_dict = {}

    for char in lower_cased:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def get_sorted_characters(char_counts):
    count_dicts = []
    
    for key, value in char_counts.items():
        count_dicts.append({"char": key, "num": value})

    count_dicts.sort(key=lambda dict: dict["num"], reverse=True)
    return count_dicts
