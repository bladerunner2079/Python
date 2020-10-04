# Push refers to concept of item being put on the top of the stack
# Concept pop-in refers to the item being put to the bottom of the stack
# Stack is defined as concept from which operation is conducted in different matrix

# Stack data structure
""""""
"D"
"C"
"B"
"A"

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")

# print(s.get_stack())


