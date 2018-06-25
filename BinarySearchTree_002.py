class BinarySearchTree():

    class Node():

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def inorder(self):
        if not self.root:
            print("Empty tree!")
        else:
            self._inorder(self.root)

    def _inorder(self, cur_node):
        if cur_node:
            self._inorder(cur_node.left)
            print(cur_node.data)
            self._inorder(cur_node.right)

    def insert(self, data):
        if not self.root:
            self.root = self.Node(data)
        else:
            self.root = self._insert(self.root, data)
        self.size += 1

    def _insert(self, cur_node, data):
        if not cur_node:
            return self.Node(data)

        if data <= cur_node.data:
            cur_node.left = self._insert(cur_node.left, data)
        else:
            cur_node.right = self._insert(cur_node.right, data)
        return cur_node

    def search(self, data):
        if not self.root:
            return False
        else:
            return self._search(self.root, data)

    def _search(self, cur_node, data):
        if not cur_node:
            return False
        elif data == cur_node.data:
            return True
        elif data < cur_node.data:
            return self._search(cur_node.left, data)
        else: # data > cur_node.data
            return self._search(cur_node.right, data)

    def find_min(self):
        if not self.root:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, cur_node):
        if not cur_node.left:
            return cur_node.data
        else:
            return self._find_min(cur_node.left)

    def find_max(self):
        if not self.root:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, cur_node):
        if not cur_node.right:
            return cur_node.data
        else:
            return self._find_max(cur_node.right)


def main():
    bst = BinarySearchTree()
    bst.inorder()
    bst.insert(15)
    bst.inorder()
    bst.insert(10)
    bst.inorder()
    bst.insert(20)
    bst.inorder()
    bst.insert(29)
    bst.inorder()
    bst.insert(7)
    bst.inorder()
    bst.insert(19)
    bst.inorder()
    bst.insert(8)
    bst.inorder()
    bst.insert(5)
    print('Final')
    bst.inorder()
    print(str(bst.search(99)))
    print(str(bst.search(10)))
    print(str(bst.search(5)))
    print(str(bst.search(20)))
    print(str(bst.search(1)))
    print(str(bst.find_min()))
    print(str(bst.find_max()))

if __name__ == "__main__":
    main()

