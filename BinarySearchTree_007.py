'''
TTC: 34:32:43
- Messing up using self.data (wrong) vs. curr.data (correct)
- Anytime make a call to self._function (insert/remove), must set node = func
'''
import random

class BinarySearchTree:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self):
        if self.root:
            self._preorder(self.root)
            print()

    def _preorder(self, curr):
        if curr:
            print(str(curr.data), end=' ')
            self._preorder(curr.left)
            self._preorder(curr.right)

    def inorder(self):
        if self.root:
            self._inorder(self.root)
            print()

    def _inorder(self, curr):
        if curr:
            self._inorder(curr.left)
            print(str(curr.data), end=' ')
            self._inorder(curr.right)

    def postorder(self):
        if self.root:
            self_postorder(self.root)
            print()

    def _postorder(self, curr):
        if curr:
            self._inorder(curr.left)
            self._inorder(curr.right)
            print(str(curr.data), end=' ')

    def insert(self, data):
        if not self.root:
            self.size += 1
            self.root = self.Node(data)
        else:
            self.root = self._insert(self.root, data)

    def _insert(self, curr, data):
        if not curr:
            self.size += 1
            return self.Node(data)
        else:
            if data < curr.data:
                curr.left = self._insert(curr.left, data)
            else:
                curr.right = self._insert(curr.right, data)
            return curr

    def get(self, data):
        if self.root:
            return self._get(self.root, data)
        else:
            return None

    def _get(self, curr, data):
        if not curr:
            return None
        else:
            if data < curr.data:
                return self._get(curr.left, data)
            elif data > curr.data:
                return self._get(curr.right, data)
            else:
                return curr

    def find(self, data):
        return self.get(data) != None

    def remove(self, data):
        if not self.root:
            raise Exception('Tree is empty!')
        else:
             self.root = self._remove(self.root, data)

    def _remove(self, curr, data):
        if not curr:
            return None
        else:
            if data < curr.data:
                curr.left = self._remove(curr.left, data)
            elif data > curr.data:
                curr.right = self._remove(curr.right, data)
            else:
                if not curr.left:
                    self.size -= 1
                    return curr.right
                elif not curr.right:
                    self.size -= 1
                    return curr.left
                else:
                    temp = self._find_min(curr.right)
                    curr.data = temp.data
                    curr.right = self._remove(curr.right, temp.data)
            return curr

    def _find_min(self, curr):
        if not curr.left:
            return curr
        else:
            return self._find_min(curr.left)


def main():
    datas = random.sample(range(100), 10)
    print(datas)

    bst = BinarySearchTree()

    print('insert')
    for data in datas:
        print(data)
        bst.insert(data)
        bst.inorder()
        print(len(bst))

    print('remove')
    for data in datas:
        print(data)
        bst.remove(data)
        bst.inorder()
        print(len(bst))

if __name__ == "__main__":
    main()

