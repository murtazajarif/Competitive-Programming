def ra(num):
    iterations = 1
    while True:
        # Reverse the digits of the number
        reversed = int(str(num)[::-1])

        # Add the reversed number to the original number
        num += reversed

        # Check if the result is a palindrome
        if str(num) == str(num)[::-1]:
            return iterations, num
        else:
            iterations += 1


# Get the number of test cases
num_cases = int(input("Enter the number of test cases: "))

for _ in range(num_cases):
    # Get the input number
    num = int(input("Enter the number: "))

    # Call the reverse_and_add function
    iterations, palindrome = ra(num)

    # Print the result
    print(iterations, palindrome)

