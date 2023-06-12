
    # Input the number of test cases
num_test_cases = int(input("Enter the number of test cases: "))
    
    # Iterate through each test case
for _ in range(num_test_cases):
    n = int(input("Enter the value of n: "))  # Input the value of n for each test case
    start_ = 1
    end_ = 1
    ollie_wins = True
    while end_ < n:
        if ollie_wins:
            start_ = end_ + 1
            end_ = end_ * 9
        else:
            start_ = end_ + 1
            end_ = end_ * 2
        ollie_wins = not ollie_wins
        
    # Print the result for each test case
    if ollie_wins:
        print("Ollie wins.")
    else:
        print("Stan wins.")
