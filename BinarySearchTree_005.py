# TTC 39:19:06
# Need to raise exception!
import random

class BinarySearchTree(object):

    class Node(object):

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def preorder(self):
        if not self.root:
            return 'Empty!'
        else:
            return 'sz: ' + str(self.size) + ', ' + self._preorder(self.root)

    def _preorder(self, curr):
        if not curr:
            return ''
        else:
            curr_str = str(curr.data)
            left_str = self._preorder(curr.left)
            right_str = self._preorder(curr.right)
            return curr_str + ' ' + left_str + ' ' + right_str

    def inorder(self):
        if not self.root:
            return 'Empty!'
        else:
            return 'sz: ' + str(self.size) + ', ' + self._inorder(self.root)

    def _inorder(self, curr):
        if not curr:
            return ''
        else:
            curr_str = str(curr.data)
            left_str = self._inorder(curr.left)
            right_str = self._inorder(curr.right)
            return left_str + ' ' + curr_str + ' ' + right_str

    def postoder(self):
        if not self.root:
            return 'Empty!'
        else:
            return 'sz: ' + str(self.size) + ', ' + self._postorder(self.root)

    def _postorder(self, curr):
        if not curr:
            return ''
        else:
            curr_str = str(curr.data)
            left_str = self._postorder(curr.left)
            right_str = self._postorder(curr.right)
            return left_str + ' ' + right_str + ' ' + curr_str

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.size += 1

    def _insert(self, curr, data):
        if not curr:
            return self.Node(data)
        elif data < curr.data:
            curr.left = self._insert(curr.left, data)
        elif data > curr.data:
            curr.right = self._insert(curr.right, data)
        else:
            curr.data = data
        return curr

    def find(self, data):
        if not self.root:
            return None
        else:
            return self._get(self.root, data) is not None

    def get(self, data):
        if not self.root:
            return None
        else:
            return self._get(self.root, data)

    def _get(self, curr, data):
        if not curr:
            return None
        elif data < curr.data:
            return self._get(curr.left, data)
        elif data > curr.data:
            return self._get(curr.right, data)
        else:
            return curr

    def remove(self, data):
        if not self.root:
            print('Empty!')
        else:
            self.root = self._remove(self.root, data)

    def _find_min(self, curr):
        if not curr.left:
            return curr
        else:
            return self._find_min(curr.left)

    def _remove(self, curr, data):
        if not curr:
            return None
        elif data < curr.data:
            curr.left = self._remove(curr.left, data)
        elif data > curr.data:
            curr.right = self._remove(curr.right, data)
        else:
            if not curr.left:
                self.size -= 1
                return curr.right
            if not curr.right:
                self.size -= 1
                return curr.left
            else:
                temp = self._find_min(curr.right)
                curr.data = temp.data
                curr.right = self._remove(curr.right, temp.data)
        return curr

    def is_bst(self):
        min_val = float('-inf')
        max_val = float('inf')
        return self._is_bst(self.root, min_val, max_val)

    def _is_bst(self, curr, min_val, max_val):
        if not curr:
            return True
        else:
            curr_valid = min_val < curr.data < max_val
            left_valid = self._is_bst(curr.left, min_val, curr.data)
            right_valid = self._is_bst(curr.right, curr.data, max_val)
            return curr_valid and left_valid and right_valid

def main():
    data = random.sample(range(100), 10)
    print(data)
    bst = BinarySearchTree()
    for item in data:
        bst.insert(item)
    print(bst.inorder())
    print(bst.is_bst())
    select = random.sample(range(10), 1)
    print(data[select[0]])
    print(bst.find(data[select[0]]))
    print(bst.find(random.sample(range(100,1000), 1)[0]))
    for item in data:
        bst.remove(item)
        print(bst.inorder())


if __name__ == "__main__":
    main()

