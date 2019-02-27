import random, math

# CONFIGURATION
amount = 1000
maximum = 100
look = 10

# Create and sort
numbers = [random.randint(1, 100) for n in range(amount)]
numbers.sort()

# Split the start
cur = [0, amount // 2, amount - 1] # start, middle, end

while 1: # Start looping
    if numbers[cur[0]] == look: # is the start found?
        print(cur[0])
        break
    elif numbers[cur[2]] == look: # is the end found?
        print(cur[2])
        break
    elif numbers[cur[1]] == look: # is the middle found?
        print(cur[1])
        break
    elif cur[1] == cur[2] or cur[1] == cur[0]: # Is there no middle?
        print("Failed to find the number.")
        break
    
    # Split the list.
    if numbers[cur[1]] > look: # Split from the start, to middle.
        cur[2] = cur[1] # Set end to middle
        cur[1] = int(cur[2] / 2) # Find the new middle
    else:
        cur[0] = cur[1] # Set start to middle
        cur[1] = int(cur[0] + ((cur[2] - cur[1]) / 2)) # Find the new middle

# Printing
print(numbers)
