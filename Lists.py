class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedOrderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def display(self):
        if self.head is None:
            print('Lista vuota')
        else:
            tmp = self.head
            while tmp is not None:
                print(tmp.value, end=" ")
                tmp = tmp.next
            print('\n', end=" ")

    def insertNewValue(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        elif value <= self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            pos = self.head
            while pos.next is not None and pos.next.value < value:
                pos = pos.next
            newNode.next = pos.next
            pos.next = newNode
        self.size += 1
        return newNode

    def OS_Select(self, i):
        j = 1
        tmp = self.head
        while tmp is not None and j is not i:
            j += 1
            tmp = tmp.next
        return tmp

    def OS_Rank(self, node):
        tmp = self.head
        i = 1
        while tmp is not None and tmp.value is not node.value:
            tmp = tmp.next
            i += 1
        if tmp is None:
            i = 0
        return i

