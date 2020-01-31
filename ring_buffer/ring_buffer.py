from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length ==  0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif self.capacity > self.storage.length:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.capacity == self.storage.length:
            node = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if node == self.current:
                self.current = self.storage.tail

    def get(self):
        list_buffer_contents = []
        if len(self.storage) <= 0:
            return list_buffer_contents
        current = self.storage.tail
        list_buffer_contents.append(current.value)
        while current.prev:
            current = current.prev
            list_buffer_contents.append(current.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
