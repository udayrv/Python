class Range:
    def __init__(self, start, stop = None, step = 1):
        if step == 0:
            raise ValueError("Step cannot be 0")
        if stop is None:
            start, stop = 0, start
        
        self._length = max(0, (stop - start + step -1)//step)
        self._start = start
        self._step = step

    def __getitem__(self, k):
        if k < 0:
            k += len(self)
        if not 0 <= k < self._length:
            raise IndexError("Index Out of Range")
        return self._start + k*self._step

#Implementation
for i in Range(10, 120, 10):
    print(i)