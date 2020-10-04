

# A binary tree is tree data structure in which each node has at most two children,
# which referred to as the left child and right child
# Up-node is root
# Value refers to the value, wish to store in the node
# Tree Traveral: Process of visiting, checking and or updating each node in a tree, data structure, onces.


class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

class Queue(object):
    def __init__(self):
        self.items = []

    ###
    # Insert element into the queue
    def enqueue(self, item):
        self.items.insert(0, item)

    ###
    # Return item from the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    ###
    # Checks if queue is empty
    def is_empty(self):
        return len(self.items) == 0

    ###
    # Shows nodes which are stored in the queue
    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    ###
    # Counts number of items in the queue
    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "pre_order":
            return self.pre_order_print(tree.root, "")
        if traversal_type == "in_order":
            return self.in_order_print(tree.root, "")
        if traversal_type == "post_order":
            return self.post_order_print(tree.root, "")
        if traversal_type == "level_order":
            return self.level_order_print(tree.root)
        if traversal_type == "reverse_level_order":
            return self.reverse_level_order_print(tree.root)
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False
    ###
    # Root > Left > Right
    def pre_order_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    ###
    # Left > Root > Right
    def in_order_print(self, start, traversal):
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    ###
    # Left > Right > Root
    def post_order_print(self, start, traversal):
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        # Used to show the node content
        traversal = ""

        while len(queue) > 0:
            # See the first node and store in the queue as a string
            traversal += str(queue.peek()) + "-"
            # Check for the left and right children
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            # Return level order traversal
        return traversal

    def reverse_level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            # Remove node from the queue
            node = queue.dequeue()
            # Add new node to the queue
            stack.push(node)
            # Check new added nodes children
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        # Pop all of the items from queue and print them from traversal string
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
        return traversal

    ###
    # Calculate height of the tree
    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    ###
    # Calculating size of the tree/ number of nodes
    def size(self):
        if self.root is None:
            return 0
        stack = Stack()
        stack.push(self.root)
        size = 1

        # Checking children and if found incrementing size number by 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

    def size_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.size_recursive(node.left) + self.size_recursive(node.right)

# Building tree
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("pre_order"))
print(tree.print_tree("post_order"))
print(tree.print_tree("in_order"))
print(tree.print_tree("level_order"))
print(tree.print_tree("reverse_level_order"))
print(tree.height(tree.root))
print(tree.size_recursive(tree.root))

#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7