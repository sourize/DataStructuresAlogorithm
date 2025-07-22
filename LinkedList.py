class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
class SingleLinkedList:
    def __init__(self):
        self.head = None

    
    def insert_at_head(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node


    def insert_after(self, prev_node, val):
        if not prev_node:
            raise ValueError("Previous node must not be None")
        node = Node(val)
        node.next = prev_node.next
        prev_node.next = node

    
    def delete(self, val):
        curr, prev = self.head, None
        while curr and curr.val != val:
            prev, curr = curr, curr.next
        if not curr:
            return False
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
        return True
    


    def find(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None
    

    def __str__(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return "->".join(vals)
    


if __name__ == "__main__":
    l = SingleLinkedList()
    for v in [10, 20, 30]:
        l.insert_at_head(v)
    print("List:", l)
    key = int(input("Delete value? "))
    if l.delete(key):
        print("Deleted", key)
    else:
        print("Not found")
    print("Now:", l)