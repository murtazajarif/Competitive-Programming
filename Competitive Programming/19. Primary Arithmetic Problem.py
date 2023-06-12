# Enter the number of test cases
test_cases = int(input("Enter the number of test cases: "))

# Iterate over the test cases
for _ in range(test_cases):
    # Enter 2 numbers
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    # Set carry and counter as 0
    carry = 0
    carry_count = 0

    # Perform the addition and carry calculationN
    while num1 > 0 and num2 > 0:
        # Adding digits and carry
        add = (num1 % 10) + (num2 % 10) + carry
        num1 //= 10
        num2 //= 10

        # If addition is greater than 9, update carry and carry count
        if add > 9:
            carry = add % 10
            carry_count += 1
            add %= 10

    # Print the carry count for the current test case
    print("Carry Count:", carry_count)
