class Vector:

    def __init__(self, d):
        '''Create d-dimensional vector of Zeros'''
        self._coords = [0]*d

    def __len__(self):
        '''returns the dimension of the vector'''
        return len(self._coords)
    
    def __getitem__(self, j):
        '''Return jth coordinate of vector'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set jth coordinate of vector to given value'''
        self._coords[j] = val

    def __add__(self, other):
        '''Return sum of two vectors.'''
        if len(self) != len(other):     # relies on __len__ method
            raise ValueError("Dimensions must be same")
        result = Vector(len(self))       # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords

    def __ne__(self, other):
        '''Return True if vector differs from other'''
        return not self == other    # rely on existing __eq__ definition

    def __str__(self):
        '''Produce string representation of vector.'''
        return '<'+str(self._coords)[1:-1]+'>'  # adapt list representation


#Implementation

test_vector = Vector(5)
test_vector[1] = 12
test_vector[3] = 16
test_vector[-1] = 18
print(test_vector[4])

u = test_vector + test_vector
print(u)

total = 0
for entry in test_vector:
        total += entry
print(total)