class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data = {}".format(self.data)

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

class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL Object: head = {}".format(self.head)

    def is_empty(self):
        """It returns True if Linked List is Empty. Otherwise, returns False."""
        return self.head is None

    def add_front(self, new_data):
        """Add a Node whose data is new_data to the front of the Linked List"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        pass

    def remove(self, data):
        pass
