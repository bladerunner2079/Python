

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_Linked_List:
    def __init__(self):
        self.head = None

    ###
    # Add node to the end of the list
    def append(self, data):
        # Check if list is empty
        if self.head is None:
            new_node = Node(data)
            # Ensuring that new node points to None
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur_node = self.head
            # Looking for the last node
            while cur_node.next:
                cur_node = cur_node.next
            # Pointing next to new node which allows to append all data inputs
            cur_node.next = new_node
            # Assigning previous node pointer to new node
            new_node.prev = cur_node
            # Pointing new node to None
            new_node.next = None

    ###
    # Add node to the beginning of the list
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            # Previous pointer of current head to point to new node
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
    ###
    # Print the list
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    ###
    # Add a new node after given node
    def add_after_node(self, key, data):
        cur_node = self.head
        while cur_node:
            # Checking if there is more then on node in the list and if the head is key
            if cur_node.next is None and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                # Pointing next to current node pointer to new node
                nxt = cur_node.next
                cur_node.next = new_node
                # Pointing new nodes pointer to the next node
                new_node.next = nxt
                # Pointing previous nodes of current nodes to the current node
                new_node.prev = cur_node
                nxt.prev = new_node
            cur_node = cur_node.next

    ###
    # Add new node before given node
    def add_before_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.prev is None and cur_node.data == key:
                self.prepend(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                prev_node = cur_node.prev
                prev_node.next = new_node
                cur_node.prev = new_node
                new_node.net = cur_node
                new_node.prev = prev_node
            cur_node = cur_node.next

    ###
    # Delete node based on key
    def delete(self, key):
        cur_node = self.head
        while cur_node:
        # Case_1 delete node which is head of the list and only one node in the list
            if cur_node.data == key and cur_node == self.head:
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return
                # Case_2 delete head node when there is more than one node in the list
                else:
                    # Storing the following node in memory
                    nxt = cur_node.next
                    cur_node.next = None
                    nxt.prev = None
                    cur_node = None
                    self.head = nxt
                    return
                # Case_3 delete node from the middle of the list
            elif cur_node.data == key:
                if cur_node.next:
                    nxt = cur_node.next
                    prev_node = cur_node.prev
                    prev_node.next = nxt
                    nxt.prev = prev_node
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
                # Case_4 delete tail node
                else:
                    prev_node = cur_node.prev
                    prev_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next

    ###
    # Delete node
    def delete_node(self, node):
        cur_node = self.head
        while cur_node:
        # Case_1 delete node which is head of the list and only one node in the list
            if cur_node == node and cur_node == self.head:
                if not cur_node.next:
                    cur_node = None
                    self.head = None
                    return
                # Case_2 delete head node when there is more than one node in the list
                else:
                    # Storing the following node in memory
                    nxt = cur_node.next
                    cur_node.next = None
                    nxt.prev = None
                    cur_node = None
                    self.head = nxt
                    return
                # Case_3 delete node from the middle of the list
            elif cur_node == node:
                if cur_node.next:
                    nxt = cur_node.next
                    prev_node = cur_node.prev
                    prev_node.next = nxt
                    nxt.prev = prev_node
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
                # Case_4 delete tail node
                else:
                    prev_node = cur_node.prev
                    prev_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next

    ###
    # Reverse list
    def reverse(self):
        tmp =None
        cur_node = self.head
        while cur_node:
            tmp = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = tmp
            cur_node = cur_node.prev
        if tmp:
            self.head = tmp.prev

    ###
    # Remove duplicates
    def remove_duplicates(self):
        cur_node = self.head
        seen = dict()
        while cur_node:
            if cur_node.data not in seen:
                seen[cur_node.data] = 1
                cur_node = cur_node.next
            else:
                nxt = cur_node.next
                self.delete_node(cur_node)
                cur_node = nxt

    ###
    # Looking for pairs which sum is equal to the input
    def pairs_with_sum(self, sum_val):
        pairs = list()
        # Setting to pointers which will crate pairs by having p as main pointer and q will move throughout the list
        p = self.head
        q = None
        while p:
            # Pointing q pointer to the next node from the head
            q = p.next
            while q:
                # Checking if sum of p and q nodes are equal to input
                if p.data + q.data == sum_val:
                    pairs.append("(" + str(p.data) + "," + str(q.data)+ ")")
                q = q.next
            p = p.next
        return pairs

double_linked_list = Double_Linked_List()

double_linked_list.append(1)
double_linked_list.append(2)
double_linked_list.append(3)
double_linked_list.append(4)
double_linked_list.append(5)

print(double_linked_list.pairs_with_sum(5))
double_linked_list.print_list()
