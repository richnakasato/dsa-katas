# - Greater than 25 minutes
# - Could not implement "remove" without help!

class BinarySearchTree():

    class Node():

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, curr, data):
        if not curr:
            return self.Node(data)
        else:
            if data < curr.data:
                curr.left = self._insert(curr.left, data)
            elif data > curr.data:
                curr.right = self._insert(curr.right, data)
        return curr

    def preorder(self):
        if not self.root:
            print('Empty!')
        else:
            print('Preorder: ', end=' ')
            self._preorder(self.root)
            print()

    def _preorder(self, curr):
        if curr:
            print(str(curr.data), end=' ')
            self._preorder(curr.left)
            self._preorder(curr.right)

    def inorder(self):
        if not self.root:
            print('Empty!')
        else:
            print('Inorder: ', end=' ')
            self._inorder(self.root)
            print()

    def _inorder(self, curr):
        if curr:
            self._inorder(curr.left)
            print(str(curr.data), end=' ')
            self._inorder(curr.right)

    def postorder(self):
        if not self.root:
            print('Empty!')
        else:
            print('Postorder: ', end=' ')
            self._postorder(self.root)
            print()

    def _postorder(self, curr):
        if curr:
            self._postorder(curr.left)
            self._postorder(curr.right)
            print(str(curr.data), end=' ')

    def get(self, data):
        return self._get(self.root, data)

    def _get(self, curr, data):
        if curr:
            if data == curr.data:
                return curr
            elif data < curr.data:
                return self._get(curr.left, data)
            else:
                return self._get(curr.right, data)
        return curr

    def find(self, data):
        return self._get(self.root, data) is not None

    def _find_min(self, curr):
        if not curr.left:
            return curr
        else:
            return self._find_min(curr.left)

    def _find_successor(self, curr):
        return self._find_min(curr.right)

    def _find_max(self, curr):
        if not curr.right:
            return curr
        else:
            return self._find_max(curr.right)

    def _find_predecessor(self, curr):
        return self._find_max(curr.left)

    def remove(self, data):
        if not self.root:
            raise Exception('Empty!')
        else:
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
                    temp = self._find_successor(curr)
                    curr.data = temp.data
                    curr.right = self._remove(curr.right, temp.data)
        return curr


def main():
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    bst.inorder()
    bst.preorder()
    print(str(bst.find(80)))
    print(str(bst.find(90)))
    print(str(bst.find(10)))
    bst.remove(80)
    bst.remove(70)
    bst.remove(30)
    bst.inorder()
    bst.preorder()

if __name__ == '__main__':
    main()

