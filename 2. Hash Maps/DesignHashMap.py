class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Create a list of dummy items
        self.capacity = 100000
        self.map = [Item("dummy", "dummy") for i in range(self.capacity)]
        
    
    def hashIndex(self, key):
        return key % self.capacity
        

    def put(self, key, value):
        """
        value will always be non-negative.
        """
        idx = self.hashIndex(key)
        curr = self.map[idx]
        while curr.next:
            if key == curr.next.key:
                # Key exists, override
                curr.next.value = value
                return
            curr = curr.next
            
        # Item not yet in map
        itm = Item(key, value)
        curr.next = itm

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = self.hashIndex(key)
        curr = self.map[idx]
        while curr.next:
            if key == curr.next.key:
                # Key exists, return value
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = self.hashIndex(key)
        prev = self.map[idx]
        curr = prev.next
        while curr:
            if key == curr.key:
                # Key exists, remove
                prev.next = curr.next
            curr = curr.next
            prev = curr


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
