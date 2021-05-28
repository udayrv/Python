class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

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

    def get_previous(self):
        """Return the self.previous attribute."""
        return self.previous

    def set_previous(self, new_previous):
        """It will replace the existing self.previous value with new_previous parameter."""
        self.previous = new_previous

