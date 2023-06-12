class MyQueue(object):
    def __init__(self):
        self.items = []  # Initialize an empty list to store the items in the queue
    
    def peek(self):
        i = self.items.pop()  # Remove an item from the end of the list
        self.items.append(i)  # Append the item back to the end of the list
        return i  # Return the item
        
    def pop(self):
        return self.items.pop()  # Remove and return the item from the end of the list
        
    def put(self, value):
        self.items.insert(0, value)  # Insert the given value at the beginning of the list

queue = MyQueue()  # Create an instance of the MyQueue class
t = int(input())  # Read an integer t from the input
for line in range(t):
    values = map(int, input().split())  # Read a line of input and split it into a list of integers
    values = list(values)  # Convert the map object to a list
    if values[0] == 1:  # If the first element is 1, call the put method on queue with the second element
        queue.put(values[1])
    elif values[0] == 2:  # If the first element is 2, call the pop method on queue
        queue.pop()
    else:  # Otherwise, print the result of calling the peek method on queue
        print(queue.peek())
