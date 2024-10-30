class ABRNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None

    def printNode(self):
        print(self.value, end="(")

class ABR:
    osCounter = 0
    found = False
    rankedNode = None

    def __init__(self):
        self.root = None
        self.size = 0

    def insertNewValue(self, value):
        newNode = ABRNode(value)
        y = None
        x = self.root
        while x is not None:
            y = x
            if newNode.value < x.value:
                x = x.left
            else:
                x = x.right
        newNode.p = y
        if y is None:
            self.root = newNode
        elif newNode.value < y.value:
            y.left = newNode
        else:
            y.right = newNode
        self.size += 1
        return newNode

    def __preorderTreeWalk(self, x):
        if x is not None:
            x.printNode()
            self.__preorderTreeWalk(x.left)
            print(end=",")
            self.__preorderTreeWalk(x.right)
            print(end=")")
        else:
            print(end="-")

    def __inorderTreeWalkSelect(self, x, i):
        if x is not None:
            self.__inorderTreeWalkSelect(x.left, i)
            if(self.osCounter is i and not self.found):
                self.found = True
                self.rankedNode = x
            else:
                self.osCounter += 1
                self.__inorderTreeWalkSelect(x.right, i)

    def __inorderTreeWalkRank(self, x, node):
        if x is not None:
            self.__inorderTreeWalkRank(x.left, node)
            if x.value is node.value and not self.found:
                self.found = True
            elif not self.found:
                self.osCounter += 1
                self.__inorderTreeWalkRank(x.right, node)

    def display(self):
        self.__preorderTreeWalk(self.root)
        print("\n", end="")

    def OS_Select(self, i):
        self.osCounter = 1
        self.__inorderTreeWalkSelect(self.root, i)
        self.osCounter = 0
        self.found = False
        x = self.rankedNode
        self.rankedNode = None
        return x

    def OS_Rank(self, node):
        self.osCounter = 1
        self.__inorderTreeWalkRank(self.root, node)
        i = self.osCounter
        self.osCounter = 0
        self.found = False
        if i > self.size:
            i = 0
        return i