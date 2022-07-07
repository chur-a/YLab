class CyclicIterator:
    
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.i = -1
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.iterable) - 1:
            self.i = -1
        self.i += 1
        return self.iterable[self.i]
                  
cyclic_iterator = CyclicIterator(range(3))
for i in cyclic_iterator:
    print(i)

