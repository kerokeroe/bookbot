from stats import get_num_words, get_char_num, sort
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
        

def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        num = get_num_words(sys.argv[1])

        characters = get_char_num(sys.argv[1])
        sorted_chars = sort(characters)
    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num} total words")
        print("--------- Character Count -------")
    
        for char in sorted_chars:
            print(f"{char["character"]}: {char["count"]}")
        print("============= END ===============")
    
    
    
main()

