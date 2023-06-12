import sys

# loop through each line of input from the user
for line in sys.stdin:

    # parse the input sequence
    input_sequence = line.split()
    n = int(input_sequence[0])
    sequence = [int(x) for x in input_sequence[1:]]

    # use a set to keep track of absolute differences between successive elements
    absolute_differences = set()

    # loop through each pair of successive elements in the sequence
    for i in range(1, n):

        # compute the absolute difference between the two elements
        absolute_difference = abs(sequence[i] - sequence[i-1])

        # if the absolute difference is less than 1 or greater than n - 1, the sequence is not jolly
        if absolute_difference < 1 or absolute_difference > n - 1:
            print("Not jolly")
            break

        # if the absolute difference has not been seen before, add it to the set
        if absolute_difference not in absolute_differences:
            absolute_differences.add(absolute_difference)

    # if the loop completes without breaking, the sequence is jolly if all absolute differences are present
    else:
        if len(absolute_differences) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")
