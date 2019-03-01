import random, math

def binary_search(numbers, look):
    """Binary Search algorithm"""
    
    # Split the start
    start = 0
    mid = len(numbers) // 2
    end = len(numbers) - 1
    found = -2

    def check_val(_start, _mid, _end):
        """Checks if the value is equal"""
        if numbers[_start] == look: # is the start found?
            return _start
        elif numbers[_end] == look: # is the end found?
            return _end
        elif numbers[_mid] == look: # is the middle found?
            return _mid
        elif _mid == _end or _mid == _start: # Is there no middle?
            return -1
        else:
            return -2 # Nothing found

    while 1: # Start looping
        found = check_val(start, mid, end) # do the check
        if found > -2:
            break
        
        # Split the list.
        if numbers[mid] > look: # Split from the start, to middle.
            end = mid # Set end to middle
            mid = int(end / 2) # Find the new middle
        else:
            start = mid # Set start to middle
            mid = int(start + ((end - mid) / 2)) # Find the new middle

    return found

# make da numbers
_numbers = sorted([random.randint(1, 10) for n in range(10)])

# Printing
print(_numbers, binary_search(_numbers, 8))
