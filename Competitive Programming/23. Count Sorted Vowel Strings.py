def countVowelStrings():
    n = int(input("Enter the length of the strings: "))
    count = ((n+4)*(n+3)*(n+2)*(n+1)) // 24
    return count

result = countVowelStrings()
print("The number of valid strings: ", result)
