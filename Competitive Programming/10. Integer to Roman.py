class Solution(object):
    def intToRoman(self, num):
        # Define a dictionary to map integer values to their corresponding Roman numerals
        rmap = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        # Define a list of integers in descending order to represent the subtractive notation sequence
        seq = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        # Initialize an empty list to store the Roman numerals
        so_far = []

        # Initialize an index to keep track of the current position in the subtractive notation sequence
        idx = 0

        # Iterate until the given number is reduced to 0
        while num > 0:
            # Check if the given number is greater than or equal to the current subtractive notation value
            if num >= seq[idx]:
                # If true, append the corresponding Roman numeral to the list
                so_far.append(rmap[seq[idx]])

                # Subtract the subtractive notation value from the given number
                num -= seq[idx]
            else:
                # If the given number is smaller than the current subtractive notation value,
                # move to the next subtractive notation value
                idx += 1

        # Return the Roman numeral representation as a string
        return "".join(so_far)
