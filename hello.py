class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item from the stack without removing it. Raise an error if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)

# Example usage:
if __name__ == "__main__":
    stack = Stack()
    
    print("Is the stack empty?", stack.is_empty())
    
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print("Stack after pushing 1, 2, and 3:", stack)
    
    print("Top item is:", stack.peek())
    
    print("Popped item is:", stack.pop())
    
    print("Stack after popping an item:", stack)
    
    print("Current size of the stack:", stack.size())
    
    print("Is the stack empty?", stack.is_empty())