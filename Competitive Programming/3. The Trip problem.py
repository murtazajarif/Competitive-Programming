import math

while True:
    # Take the number of expenses as input from the user
    n = int(input("Enter number of expenses: "))
    
    # If n is zero, break the loop
    if n == 0:
        break

    # Create an empty list to hold expenses
    expenses = []
    
    # Initialize a variable to hold the total cost of all expenses
    total = 0
    
    # Loop through n times to get each expense from the user
    for i in range(n):
        # Get the expense and add it to the list and the total
        expense = float(input("Enter expenses: "))
        expenses.append(expense)
        total += expense

    # Calculate the average expense
    avg = total / n

    # Initialize a variable to hold the total exchange amount
    exchange = 0
    
    # Loop through all expenses to calculate the exchange amount
    for expense in expenses:
        # Calculate the difference between the expense and the average expense
        diff = expense - avg
        
        # If the expense is greater than the average expense, add the difference to the exchange
        if diff > 0:
            exchange += diff

    # Round the exchange down to two decimal places using the floor function of the math library
    exchange = math.floor(exchange * 100) / 100
    
    # Print the exchange amount in the format of a dollar sign and two decimal places
    print(f"${exchange:.2f}")
