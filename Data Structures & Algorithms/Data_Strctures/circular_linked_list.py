

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

class Circular_Linked_List:
    def __init__(self):
        self.head = None

    ###
    # Adding node to the end of the list
    def append(self, data):
        # Checking if list contains any nodes
        if not self.head:
            self.head = Node(data)
            # Pointing head to itself
            self.head.next = self.head
        else:
            new_node = Node(data)
            # Searching for node which points to the head of the list
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            # Point new node ot the head of the list
            cur_node.next = new_node
            new_node.next = self.head

    ###
    # Adding node to the beginning of the list
    def prepend(self, data):
        # Adding new node to the list and pointing it to the head of the list
        new_node = Node(data)
        cur_node = self.head
        new_node.next = self.head
        # Checking if list contains any nodes
        if not self.head:
            new_node.next = new_node
        else:
            # Looking for node first node
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        # Setting new node as the head of the list
        self.head = new_node

    ###
    # Printing list
    def print_list(self):
        cur_node = self.head
        # While cur_node is not null continue to print out each nodes data
        while cur_node:
            print(cur_node.data)
            # Looping though the entire list
            cur_node = cur_node.next
            # Breaking from the loop as it is a circular list and it would continue printing nodes in infinity
            if cur_node == self.head:
                break

    ###
    # Remove nodes from the list based on key
    def remove(self, key):
        # Checking if key is the head node
        if self.head.data == key:
            cur_node = self.head
            # Loop though the list and look for the node which points to the head
            while cur_node.next != self.head:
                cur_node = cur_node.next
                # Point last node in the list to the next of head node
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            # Setting points
            cur_node = self.head
            prev_node = None
            # Looping through the list and looking or the last node which points to the head
            while cur_node.next != self.head:
                # Moving points though the lust
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node.data == key:
                    # Re-point previous pointer to the current.next as current is being deleted
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next

    ###
    # Remove nodes from the list
    def remove_node(self, node):
        if self.head == node:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = self.head.next
            self.head = self.head.next
        else:
            cur_node = self.head
            prev_node = None
            while cur_node.next != self.head:
                prev_node = cur_node
                cur_node = cur_node.next
                if cur_node == node:
                    prev_node.next = cur_node.next
                    cur_node = cur_node.next

    ###
    # Over-write len function to calculate the length of the list
    def __len__(self):
        cur_node = self.head
        count = 0
        # Looping though the list and counting nodes
        while cur_node:
            count += 1
            cur_node = cur_node.next
            # When node which points to the head is found, break the loop
            if cur_node == self.head:
                break
        return count

    ###
    # Split list
    def split_list(self):
        # Size calculates all of nodes in the list
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size//2
        count = 0
        prev_node = None
        cur_node = self.head
        # Calculating nodes to the mid point and changing pointer so it splits into two lists
        while cur_node and count < mid:
            count += 1
            prev_node = cur_node
            cur_node = cur_node.next
        # Make up first list by pointing mid point to head
        prev_node.next = self.head

        split_circular_linked_list = Circular_Linked_List()
        # While pointers are not pointing to the head, construct second list
        while cur_node.next != self.head:
            split_circular_linked_list.append(cur_node.data)
            cur_node = cur_node.next
        # Capturing last node into the second list
        split_circular_linked_list.append(cur_node.data)

    ###
    # Josephus problem
    def josephus_circle(self, step):
        cur_node = self.head
        # While length of the list is greater than 1, continue to loop though the list and remove nodes based on step
        while len(self) > 1:
            count = 1
            while count != step:
                cur_node = cur_node.next
                count += 1
            print("Killed: " + str(cur_node.data))
            self.remove_node(cur_node)
            cur_node = cur_node.next

    ###
    # Checking logic of the list
    def list_logic(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False


circular_linked_list = Circular_Linked_List()
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)
circular_linked_list.append(4)

single_linked_list = Single_Linked_List()
single_linked_list.append(1)
single_linked_list.append(2)
single_linked_list.append(3)
single_linked_list.append(4)

print(circular_linked_list.list_logic(circular_linked_list))
print(circular_linked_list.list_logic(single_linked_list))