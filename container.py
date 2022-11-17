from matrix import Matrix


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Container:
    def __init__(self):
        self.start_node = None
        self.size = 0

    def add(self, data):
        if self.start_node is None:
            self.start_node = Node(data)
        else:
            n = self.start_node
            while n.next is not None:
                n = n.next
            n.next = Node(data)
            n.prev = n

        self.size += 1

    def read_from(self, stream):
        while line := stream.readline():
            item = Matrix.create_from(stream, line)
            self.add(item)

    def write_to(self, stream):
        stream.write(f'Container contains {self.size} elements\n')

        if self.start_node != None:
            n = self.start_node
            while n is not None:
                n.data.write_to(stream)
                n = n.next

    def clear(self):
        self.start_node = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return str(self.start_node)
