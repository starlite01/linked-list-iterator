from typing import Optional, Self


class LinkedListIndexError(IndexError):
    ...


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional[Self] = None


class LinkedListIterator:
    def __init__(self, llist: "LinkedList") -> None:
        self.current_node = llist.head

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> Node:
        if self.current_node is None:
            raise StopIteration
        node_to_return = self.current_node
        self.current_node = self.current_node.next
        return node_to_return


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, node: Node) -> Node:
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        return node

    def __getitem__(self, index: int) -> Node:
        for i, node in enumerate(self):
            if i == index:
                return node
        raise LinkedListIndexError

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)


linked_list = LinkedList()
for i in range(7):
    linked_list.append(Node(i))

for node in linked_list:
    print(node.data)

nodes_data = [node.data for node in linked_list]
squad_nodes_data = list(map(lambda node: node.data ** 2, linked_list))
print(nodes_data, squad_nodes_data, sep="\n")

