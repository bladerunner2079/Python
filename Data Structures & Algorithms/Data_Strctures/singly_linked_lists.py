
# Linked lists are made of nodes(box) which contains two components data and next
# Data component simply contains data
# Next is pointer which points to next node(box) in chain
# Start of the list refers to head
# Last component of the list called null(none)

# Insertion
# Adding new element to the end of the list

####
# Creating classes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    ###
    # Print Linked-list
    def print_list(self):
        cur_node = self.head
        # Loop though the nodes and print out their data names
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    ###
    # Append last node to the linked-list
    def append(self, data):
        new_node = Node(data)
        # First, check if linked-list is empty
        if self.head is None:
            # If linked_list is empty add new node as head
            self.head = new_node
            return

        # If linked-list is not empty, add new node to the end of the linked-list
        last_node = self.head
        # Loop though the linked-list and look for the node which points to null
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    ###
    # Add new node to the beginning of the linked-list
    def prepend(self, data):
        new_node = Node(data)
        # Point new node to current node head and move head to new node
        new_node.next = self.head
        self.head = new_node

    ####
    # Insert in-between the nodes of the linked-list
    def insert_after_node(self, prev_node, data):
        # Checking if the previous node is in the list
        if not prev_node:
            print("Previous node is not in the linked-list")
            return
        # Else
        new_node = Node(data)
        new_node = prev_node.next
        prev_node.next = new_node

    ####
    # Delete node
    # Deleting head node
    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            # Move head to the next node
            self.head = cur_node.next
            # Deleting node
            cur_node = None
            return

    # Deleting node which is not the head
        prev_node = None
        while cur_node and cur_node.data != key:
            # Setting previous node as current node
            prev_node = cur_node
            cur_node = cur_node.next
        # Checking if current node is in the list
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    ###
    # Delete node based on index position of the linked-list
    def delete_node_at_pos(self, pos):
        cur_node = self.head
        # Checking if current node is the head, if yes moving it to the following node
        if pos == 0:
            cur_node = cur_node.next
            cur_node = None
            return

        prev_node = None
        count = 1
        while cur_node and count != pos:
            # Keeps tracks of nodes which have been checked/looped though
            prev_node = cur_node
            cur_node = cur_node.next
            count += 1
        # Checking if the position exist
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    ###
    # Calculate the length of the linked-list by using iterative method
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            # Moving head to the following node
            cur_node = cur_node.next
        return count

    ###
    # Calculate the length of the linked-list by using recursive method
    def len_recursive(self, node):
        # Checking if there is nodes in the linked-list
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    ###
    # Swap nodes
    def swap_nodes(self, key_1, key_2):
        # Checking if the nodes to be swapped are the same
        if key_1 == key_2:
            return

        prev_node_1 = None
        cur_node_1 = self.head
        # Select first head to be swapped
        while cur_node_1 and cur_node_1.data != key_1:
            # Keep track of the nodes which have been checked
            prev_node_1 = cur_node_1
            cur_node_1 = cur_node_1.next

        ## Same as above for the second key
        prev_node_2 = None
        cur_node_2 = self.head
        while cur_node_2 and cur_node_2.data != key_2:
            prev_node_2 = cur_node_2
            cur_node_2 = cur_node_2.next
        if not cur_node_1 or not cur_node_2:
            return

        if prev_node_1:
            # If node has a previous node, point it to the first current node
            prev_node_1.next = cur_node_2
            # Otherwise current node is head and pointer will point to next node
        else:
            self.head = cur_node_2

        ## Same as above
        if prev_node_2:
            prev_node_2.next = cur_node_1
        else:
            self.head = cur_node_1
        # Swapping nodes
        cur_node_1.next, cur_node_2.next = cur_node_2.next, cur_node_1.next

    ###
    # Print node data
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name +":" + node.data)

    ### Flip over linked-list
    ## Iterative method
    def reverse_iterative(self):
        prev_node = None
        cur_node = self.head
        while cur_node:
            nxt = cur_node.next
            # Moving current node to the previous
            cur_node.next = prev_node
            # Using function to see updating procedure
            self.print_helper(prev_node, "Prev")
            self.print_helper(cur_node, "Cur")
            self.print_helper(nxt, "Nxt")
            print("\n")
            prev_node = cur_node
            cur_node = nxt
        # Moving head to the last node
        self.head = prev_node

    ## Recursive method
    def reverse_recursive(self):
        def _reverse_recursive(cur_node, prev_node):
            if not cur_node:
                return prev_node
            nxt = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = nxt
            return _reverse_recursive(cur_node, prev_node)

        self.head = _reverse_recursive(cur_node=self.head, prev_node=None)

    ###
    # Merge two linked_lists in sort order
    def merge_sorted(self, linked_list):
        p = self.head
        q = linked_list.head
        s= None
        # Checking if p or q linked-lists do exist
        if not p:
            return q
        if not q:
            return p
        # Checking if p and q linked-lists are None
        if p and q:
            # Checking which data point has a lesser node
            if p.data <= q.data:
                # Setting head as lesser node
                s = p
                # Move p in-front of lesser node
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    ###
    # Remove duplicates
    def remove_duplicates(self):
        cur_node = self.head
        prev_node = None
        dup_values = dict()

        while cur_node:
            if cur_node.data in dup_values:
                # If duplicate node value is found remove it from the linked-list and Re-point pointer to the next node
                prev_node.next = cur_node.next
                cur_node = None
            else:
                # if unique node value is found add it to the dic
                dup_values[cur_node.data] = 1
                prev_node = cur_node
            cur_node = prev_node.next

    ###
    # Select nth to last
    # Method 1
    def print_nth_to_last(self, n):
        # Calculate total length of the linked-list
        total_len = self.len_iterative()
        cur_node = self.head
        # Loop though the linked-list and look for n
        while cur_node:
            if total_len == n:
                print(cur_node.data)
                return cur_node
            # Decrement by 1 from total length
            total_len -= 1
            cur_node = cur_node.next
        if cur_node is None:
            return

    # Method 2
    #     p = self.head
    #     q = self.head
    #     count = 0
    #     # Looping thought the list and moving q index to null
    #     while q and count < n:
    #         q = q.next
    #         count += 1
    #     # if selected node is not found
    #     if not q:
    #         print( str(n) + "is greater than the number of nodes in linked-list")
    #         return
    #
    #     # while p and q indexes are not null keep moving along the linked-list
    #     while p and q:
    #         p = p.next
    #         q = q.next
    #     return p.data

    ####
    # Count node data occurrences
    def count_occurences_iterative(self, data):
        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                count += 1
            cur_node = cur_node.next
        return count

    def count_occurences_recursive(self,node, data):
        # If data element is not found
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    ###
    # Rotate linked-list
    def rotate(self, k):
        p = self.head
        q = self.head

        prev_node = None
        count = 0
        while p and count < k:
            prev_node = p
            p = p.next
            q = q.next
            count += 1
        p = prev_node

        while q:
            prev_node = q
            q = q.next
        q = prev_node

        # Pointing last node to the head/ Moving to the beginning of the list
        q.next = self.head

        # Moving head of the list to the p
        self.head = p.next
        p.next = None

    ###
    # Palindrome
    # Method 1
    def is_palendrome(self):
        s = ""
        p = self.head
        while p:
            # Cancatenate node data to the s
            s += p.data
            p = p.next
        # Reverse the string
        return s == s[:: -1]

        # # Method 2
        # p = self.head
        # s = []
        # while p:
        #     # Adding string to the list
        #     s.append(p.data)
        #     p = p.next
        #     p = self.head
        # while p:
        #     # Storing popped element in the data list
        #     data = s.pop()
        #     if p.data != data:
        #         return False
        #     p = p.next
        # return True

        ## Method 3
        # p = self.head
        # q = self.head
        # prev_node = []
        #
        # i = 0
        # while q:
        #     prev_node.append(q)
        #     q = q.next
        #     i += 1
        # q = prev_node[i-1]
    ###
    # Move tail to head
    def move_tail_to_head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

    ###
    # Sum of two list
    def sum_two_lists(self, llists):
        p = self.head
        q = llists.head

        sum_llist = Linked_List()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                g = 0
            else:
                g = q.data
            s = i + g + carry
            if s > 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()