def get_book_test(filepath):
    with open(filepath) as f:
        return f.read()

def num_of_words(filepath):
    words_list = get_book_test(filepath).split()
    word_count = 0
    for word in words_list:
        word_count +=1
    
    return word_count


def char_appereance(filepath):
    char_dict = {}
    words = get_book_test(filepath)
    for char in words.lower():
        if char.isalpha():
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1
    
    return char_dict

def sort_on(item):
    return item[1]

def dict_sort(dict_char):
    sorted_items = sorted(dict_char.items(), reverse=True, key=sort_on)
    return dict(sorted_items)