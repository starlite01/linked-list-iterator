from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class LinkedListIterator:
    def __init__(self, linked_list: "LinkedList") -> None:
        self.current_node = linked_list.head

    def __iter__(self) -> "LinkedListIterator":
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

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)


l_list_1 = LinkedList()

for i in range(10):
    l_list_1.append(Node(i))

for node in l_list_1:
    print(node.data)
