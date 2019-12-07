class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insertFront(self, key, value):
        new_node = Node(key, value)
        old_first = self.head.next
        new_node.prev = self.head
        old_first.prev = new_node
        new_node.next = old_first
        self.head.next = new_node
        self.size += 1
        return new_node
    
    def removeLast(self):
        to_remove = self.tail.prev
        to_remove.prev.next = self.tail
        self.tail.prev = to_remove.prev
        self.size -= 1
        return to_remove.key
    
    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.dll = DoublyLinkedList(capacity)

    def get(self, key: int) -> int:
        if key in self.map:
            node_to_remove = self.map[key]
            # Remove the node from the dll
            self.dll.deleteNode(node_to_remove)
            # Remove the node from the map
            del(self.map[key])
            # Add it to the front
            new_node = self.dll.insertFront(node_to_remove.key, node_to_remove.val)
            self.map[key] = new_node
            return node_to_remove.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            # Update the value of the existing node and move it to the front
            node_to_update = self.map[key]
            # Remove the node from the dll
            self.dll.deleteNode(node_to_update)
            # Remove the node from the map
            del(self.map[key])
            # Add it to the front
            new_node = self.dll.insertFront(node_to_update.key, value)
            self.map[key] = new_node
        else:
            # Insert the node as a new node (and kick the last item if we're at the capacity limit)
            new_node = self.dll.insertFront(key, value)
            self.map[key] = new_node
            if self.dll.size > self.capacity:
                removed_key = self.dll.removeLast()
                del(self.map[removed_key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
