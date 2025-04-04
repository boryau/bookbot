from stats import num_of_words, char_appereance,dict_sort
import sys

def main():
    if len(sys.argv) <2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_words = num_of_words(filepath) 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_dict = char_appereance(filepath)
    sorted_dict= dict_sort(char_dict)

    for key in sorted_dict:
        print(f"{key}: {sorted_dict[key]}")


    print("============= END ===============")

main()