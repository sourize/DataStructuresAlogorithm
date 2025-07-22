class Queue:
    def __init__(self, capacity=4):
        self._data = [None] * capacity
        self._front = 0
        self._size = 0
        self._capacity = capacity
    

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    

    def enqueue(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        avail = (self._front + self._size) % self._capacity
        self._data[avail] = value
        self._size += 1

    
    def dequeue (self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1

        if 0 < self._size < self._capacity // 4:
            self._resize(self._capacity // 2)
        return value
    

    def _resize(self, new_cap):
        old = self._data
        self._data = [None] * new_cap
        for i in range (self._size):
            self._data[i] = old[(self._front + i) % self._capacity]
        self._front = 0
        self._capacity = new_cap

    
    def __str__(self):
        elems = [str(self._data[(self._front + i) % self._capacity]) for i in range(self._size)]
        return "Queue front [" + ", ".join(elems) + "] rear"
    


if __name__ == "__main__":
    q = Queue()
    for x in range(5):
        print(f"Enqueue {x}")
        q.enqueue(x)
    print(q)
    print("Dequeue:", q.dequeue())
    print("After dequeue:", q)

        

        
