# Define the conversion table for LED digits
conversion_table = [
    ['-','|','|',' ','|','|','-'],   # 0
    [' ','|',' ',' ','|',' ',' '],   # 1
    ['-','|',' ','-',' ','|','-',],  # 2
    ['-','|',' ','-','|',' ','-',],  # 3
    [' ','|','|','-','|',' ',' '],   # 4
    ['-',' ','|','-','|',' ','-',],  # 5
    ['-',' ','|','-','|','|','-',],  # 6
    ['-','|',' ',' ','|',' ',' '],   # 7
    ['-','|','|','-','|','|','-',],  # 8
    ['-','|','|','-','|',' ','-',],  # 9
]

# Define a function to print an LED digit
def print_led_digit(s: int, digit: str) -> None:
    # Iterate over each row of the digit
    for i in range(2*s+3):
        # Iterate over each digit in the input string
        for j in range(len(digit)):
            # If we're on a horizontal line, print the top/bottom part of the digit
            if i % (s+1) == 0:
                # Print the left boundary of the digit
                print(" ", end="")
                # Print the vertical bars for the digit, repeated s times
                for k in range(s):
                    print(conversion_table[int(digit[j])][i//(s+1)*3], end="")
                # Print the right boundary of the digit
                print(" ", end="")
            # If we're on the top half of a vertical line, print the upper part of the digit
            if i > 0 and i < s+1:
                # Print the left boundary of the digit
                print(conversion_table[int(digit[j])][2], end="")
                # Print s spaces to represent the gap between the top and bottom halves
                print(" "*s, end="")
                # Print the right boundary of the digit
                print(conversion_table[int(digit[j])][1], end="")
            # If we're on the bottom half of a vertical line, print the lower part of the digit
            if i > s+1 and i < 2*s+2:
                # Print the left boundary of the digit
                print(conversion_table[int(digit[j])][5], end="")
                # Print s spaces to represent the gap between the top and bottom halves
                print(" "*s, end="")
                # Print the right boundary of the digit
                print(conversion_table[int(digit[j])][4], end="")
            # If we're not on the last digit, print a space to separate the digits
            if j != len(digit)-1:
                print(" ", end="")
        # Print a newline character to move on to the next row
        print()
    # Print an extra newline character to separate the LED digits
    print()

# Continuously prompt the user for input until they enter "0"
while True:
    # Read in a line of input, containing s and digit separated by a space
    s, digit = input().split()
    # If s is "0", break out of the loop
    if s == "0 0":
        break
    # Print the LED digit using the given s and digit
    print_led_digit(int(s), digit)