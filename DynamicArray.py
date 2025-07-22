class DynamicArray:
    def __init__(self, capacity=4):
        self._capacity = capacity
        self._count = 0
        self._data = [None] * capacity


    def __len__(self):
        return self._count
    
    
    def _resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range (self._count):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_cap



    def insert (self, index, value):
        if index < 0 or index > self._count:
            raise IndexError("Index out of Bounds")
        if self._count == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._count, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self._count += 1




    def delete (self, index):
        if index < 0 or index > self._count:
            raise IndexError("Index out of bounds")
        for i in range (index, self._count-1):
            self._data[i] = self._data[i+1]
        self._data[self._count-1] = None
        self._count -= 1



    def get (self, index):
        if index < 0 or index > self._count:
            raise IndexError("Index out of bounds")
        return self._data[index]
    
    
    
    def __str__(self):
        return "[" + ", ".join(str(self._data[i]) for i in range(self._count)) + "]"
    

if __name__ == "__main__":
    arr = DynamicArray()
    n = int(input("How many initial elements? "))
    for _ in range (n):
        val = input("Enter value: ")
        arr.insert(len(arr), val)
    print ("Array now: ", arr)
    idx = int(input("Delete at index? "))
    arr.delete(idx)
    print("After deletion:", arr)