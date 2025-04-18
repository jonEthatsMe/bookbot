from stats import get_book_text
import sys


def main(): 
        if len(sys.argv) < 2:
                print ("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        else:
             print("Script is: ",sys.argv[0])   
        contents, charCount = get_book_text(sys.argv[1])
        print(contents)
        for key in charCount:
               print(key+":",charCount.get(key))

main()
