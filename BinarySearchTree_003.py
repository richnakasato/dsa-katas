class BinarySearchTree():

    class Node():

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None

    def preorder(self):
        if not self.root:
            print('Empty!')
        else:
            self._preorder(self.root)

    def _preorder(self, curr):
        if curr:
            print(curr.data, end=' ')
            self._preorder(curr.left)
            self._preorder(curr.right)

    def inorder(self):
        if not self.root:
            print('Empty!')
        else:
            self._inorder(self.root)
            print()

    def _inorder(self, curr):
        if curr:
            self._inorder(curr.left)
            print(curr.data, end=' ')
            self._inorder(curr.right)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, curr, data):
        if not curr:
            curr = self.Node(data)
        elif data < curr.data:
            curr.left = self._insert(curr.left, data)
        elif data > curr.data:
            curr.right = self._insert(curr.right, data)
        return curr

    def get(self, data):
        return self._get(self.root, data)

    def _get(self, curr, data):
        if not curr:
            return None
        elif data == curr.data:
            return curr
        elif data < curr.data:
            return self._get(curr.left, data)
        else:
            return self._get(curr.right, data)

    def find(self, data):
        return self.get(data) is not None

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, curr):
        if not curr:
            return None
        elif not curr.left:
            return curr
        else:
            return self._find_min(curr.left)

    def find_successor(self, node):
        if not node.right:
            return node
        else:
            return self._find_min(node.right)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, curr):
        if not curr:
            return None
        elif not curr.right:
            return curr
        else:
            return self._find_max(curr.right)

    def find_predecessor(self, node):
        if not node.left:
            return node
        else:
            return self._find_max(node.left)

    def remove(self, data):
        if self.root:
            self.root = self._remove(self.root, data)

    def _remove(self, curr, data):
        if curr:
            if data < curr.data:
                curr.left = self._remove(curr.left, data)
            elif data > curr.data:
                curr.right = self._remove(curr.right, data)
            else:
                if not curr.left:
                    return curr.right
                elif not curr.right:
                    return curr.left
                else:
                    successor = self.find_successor(curr)
                    curr.data = successor.data
                    curr.right = self._remove(curr.right, successor.data)
        return curr


def main():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(40)
    bst.insert(20)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)
    bst.inorder()
    print(str(bst.find(90)))
    print(str(bst.find(10)))
    print(str(bst.find(20)))
    print(str(bst.find(70)))
    print(str(bst.find_min()))
    print(str(bst.find_max()))
    print('test')
    temp = bst.get(50)
    print(bst.get(50))
    print(bst.root)
    print(str(bst.find_successor(temp).data))
    print(str(bst.find_predecessor(temp).data))
    bst.remove(50)
    bst.remove(40)
    bst.remove(20)
    bst.remove(70)
    bst.inorder()

if __name__ == "__main__":
    main()

