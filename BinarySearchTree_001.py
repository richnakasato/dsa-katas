class BinarySearchTree():

    class Node():

        def __init__(self, key, val, left=None, right=None, parent=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.parent = parent

        def __str__(self):
            return "key: " + str(self.key) + ", val: " + str(self.val)


    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, val):
        if not self.root:
            self.root = self.Node(key, val)
        else:
            self._insert(key, val, self.root)
        self.size += 1

    def _insert(self, key, val, cur_node):
        if key < cur_node.key:
            if cur_node.left:
                self._insert(key, val, cur_node.left)
            else:
                cur_node.left = self.Node(key, val, parent=cur_node)
        else:
            if cur_node.right:
                self._insert(key, val, cur_node.right)
            else:
                cur_node.right = self.Node(key, val, parent=cur_node)

    def find(self, key):
        if self.root:
            return self._find(key, self.root)
        else:
            return None

    def _find(self, key, cur_node):
        if not cur_node:
            return None
        elif cur_node.key == key:
            return cur_node.val
        elif cur_node.key > key:
            return self._find(key, cur_node.left)
        else:
            return self._find(key, cur_node.right)

    def remove(self):
        pass

    def preorder(self):
        if self.root:
            self._preorder(self.root)
        else:
            raise Exception("Empty tree!")

    def _preorder(self, cur_node):
        print(cur_node)
        if cur_node.left:
            self._preorder(cur_node.left)
        if cur_node.right:
            self._preorder(cur_node.right)

    def inorder(self):
        if self.root:
            self._inorder(self.root)
        else:
            raise Exception("Empty tree!")

    def _inorder(self, cur_node):
        if cur_node.left:
            self._inorder(cur_node.left)
        print(cur_node)
        if cur_node.right:
            self._inorder(cur_node.right)

    def postorder(self):
        if self.root:
            self._postorder(self.root)
        else:
            raise Exception("Empty tree!")

    def _postorder(self, cur_node):
        pass


def main():
    bst = BinarySearchTree()
    bst.insert(3, "C")
    bst.insert(1, "A")
    bst.insert(5, "B")
    bst.inorder()
    bst.preorder()

if __name__ == "__main__":
    main()

