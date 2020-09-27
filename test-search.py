# import class from binary_search.py
from binary_search import binSearch

def main():
    # a random list - feel free to enter your own values here!
    # note: values must be entered in ascending order
    myList = [1, 2, 5, 6, 9, 19, 28, 54, 65, 100]
    
    # create an object with which to search, using the list as an input
    searcher = binSearch(myList)

    # search for a random value in the list
    print(searcher.find(5))

    # search for a value that is not in the list
    print(searcher.find(596))



if __name__ == '__main__':
    main()