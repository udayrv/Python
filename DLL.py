class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data = {}".format(self.data)

    def get_data(self):
        """It will return the self.data attribute."""
        return self.data
    
    def set_data(self, new_data):
        """It will replace the existing self.data value with new_data parameter."""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute."""
        return self.next

    def set_next(self, new_next):
        """It will replace the existing self.next value with new_next parameter."""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute."""
        return self.previous

    def set_previous(self, new_previous):
        """It will replace the existing self.previous value with new_previous parameter."""
        self.previous = new_previous


class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        """Traverses the linked list and returns an integer value representing the number of 
        nodes in the linked list.
        
        The time complexity is O(n) because every node in the Linked List has to be visited 
        in order to calculate the size of the Linked List."""

        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the Linked list and returns True if the data searched for is present in one
        of the nodes. Otherwise, it returns False.
        
        The time complexity is O(n), because in the worst case we have to go through all the
        Nodes for searching the data."""

        if self.head is None:
            return "Linked List is empty. There are no nodes to search"

        current = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        
        return False

    def add_front(self, data):
        """Add a Node whose data is new_data to the front of the Linked List"""
        temp = DLLNode(data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        """It removes the first occurence of the node that contains the data argument as it's
        self.data attribute. Returns Nothing.
        
        The time complexity is O(n), because in the worst case, we have to visit every node in the
        Linked List before finding the one we wanted to remove."""

        if self.head is None:
            return "Linked list is empty. No Nodes to remove."

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
                print("A node with data value {} is removed.".format(data))
            else:
                if current.get_next() is None:
                    return "There is no node in the Linked List with that data value."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())