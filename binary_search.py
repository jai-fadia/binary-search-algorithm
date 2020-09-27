###################################################################################################
###                                     Author: Jai Fadia                                       ###
### This Python file is intended to display a basic implentation of the binary search algorithm ###
###                 Commented as thoroughly as possible to explain each step                    ###
###################################################################################################

class binSearch():
    def __init__(self, array):
        """
        Constructor function to initialize the object.

        Arguments:
        - array: the array (list) to be searched (note: must be in ascending order)
        """
        # note: binary search requires the input array to be sorted in ascending order
        self.array = array
    
    def find(self, value):
        """
        Function that uses a binary search algorithm to find and return the index of a value from a list.

        Arguments:
        - value: the value that is being searched for

        Returns the index of the value that was entered.
        """

        # the starting point of the algorithm is in the middle of the list
        # we will use the variable i to reference the current index
        i = int(len(self.array) / 2)

        # the upper and lower bounds of the search - these variables are updated as the algorithm progresses to narrow down the range between which we will be searching
        # upper initialized as the maximum index of the list
        upper = len(self.array)
        # lower initialized as the minimum index of the list
        lower = 0

        # initialize the output value of the list for each iteration of the algorithm
        out = None

        # initialize the while loop, keep looping through until 'value' equals the element in the list
        while out != value:
            # examine the element of index i
            out = self.array[i]

            if out == value:
                # return the index if out = value
                return f'Element {value} found at index {i}'
                break
            elif value > out:
                # update the lower bound and calculate the new midpoint between the upper and lower bounds for the next iteration
                lower = i
                i = int((upper + lower) / 2)
            elif value < out:
                # update the upper bound and calculate the new midpoint between the upper and lower bounds for the next iteration
                upper = i
                i = int((upper + lower) / 2)
            
            # break the loop if i = upper or i = lower - this scenario occurs when the value is not in the list
            if i == upper or i == lower:
                break
        
        return f'Element {value} not found in the list list.'