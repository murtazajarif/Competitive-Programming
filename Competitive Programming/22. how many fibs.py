# Initialize the first two Fibonacci numbers.
f1 = 1
f2 = 2

# Get the input from the user.
while True:
    a, b = map(int, input().split())

    # If a and b are both 0, then the input is terminated.
    if a == 0 and b == 0:
        break

    # Initialize the count variable.
    count = 0

    # Iterate over the Fibonacci numbers until f > b.
    while f1 <= b:
        # If f is in the range [a, b], then increment the count variable.
        if a <= f1 <= b:
            count += 1

        # Calculate the next Fibonacci number.
        f3 = f1 + f2

        # Update the values of f1 and f2.
        f1, f2 = f2, f3

    # Print the number of Fibonacci numbers in the range [a, b].
    print(count)