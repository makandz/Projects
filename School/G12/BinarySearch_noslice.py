import random, math

def binary_search(numbers, look):
    """Binary Search algorithm"""
    
    # Split at the start
    start = 0 # Start is beginning
    mid = len(numbers) // 2 # the middle
    end = len(numbers) - 1 # end
    found = -2 # temp not found

    # is it empty?
    if not numbers:
        return -1

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
        if found > -2: # is the value finally found
            break
        
        # Split the list.
        if numbers[mid] > look: # Split from the start, to middle. [left]
            end = mid # Set end to middle
            mid = int(end / 2) # Find the new middle
        else:
            start = mid # Set start to middle
            mid = int(start + ((end - mid) / 2)) # Find the new middle

    return found # final answer

# TEST CASES

# Find value in a decent sized list, looking for 7
nums = sorted([random.randint(1, 10) for n in range(20)])
print(nums, binary_search(nums, 7))

# Find value in an empty list, should not find
nums = []
print(nums, binary_search(nums, 1))

# Finding 1 in a very small list.
nums = [1]
print(nums, binary_search(nums, 1))

# Find a value at the end of a size 2 array.
nums = [1, 10]
print(nums, binary_search(nums, 10))

# Find exact center value.
nums = [1, 4, 10]
print(nums, binary_search(nums, 4))

# Find value in a decent sized list, looking for 7
nums = sorted([random.randint(1, 20) for n in range(100)])
print(nums, binary_search(nums, 7))
