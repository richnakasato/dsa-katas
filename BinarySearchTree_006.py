# TTC - 38.49.54
# - need to remember where to adjust size when removing (only 2 places!)
# - spent way too much time working on preorder, inorder, and postorder pretty
# printing
# - need to implement isBST() function

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

    def __len__(self):
        return self.size

    def preorder(self):
        if not self.root:
            print("Empty!")
        else:
            print("(preorder) size: " + str(len(self)) + " -> ", end="")
            self._preorder(self.root)
            print()

    def _preorder(self, curr):
        if curr:
            print(str(curr.data), end=" ")
            self._preorder(curr.left)
            self._preorder(curr.right)

    def inorder(self):
        if not self.root:
            print("Empty!")
        else:
            print("(inorder) size: " + str(len(self)) + " -> ", end="")
            self._inorder(self.root)
            print()

    def _inorder(self, curr):
        if curr:
            self._inorder(curr.left)
            print(str(curr.data), end=" ")
            self._inorder(curr.right)

    def postorder(self):
        if not self.root:
            print("Empty!")
        else:
            print("(postorder) size: " + str(len(self)) + " -> ", end="")
            self._postorder(self.root)
            print()

    def _postorder(self, curr):
        if curr:
            self._postorder(curr.left)
            self._postorder(curr.right)
            print(str(curr.data), end=" ")

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, curr, data):
        if not curr:
            self.size += 1
            return self.Node(data)
        else:
            if data < curr.data:
                curr.left = self._insert(curr.left, data)
            elif data > curr.data:
                curr.right = self._insert(curr.right, data)
            else:
                curr.data = data
            return curr

    def get(self, data):
        if not self.root:
            return None
        else:
            return self._get(self.root, data)

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
        return self.get(data) is not None

    def remove(self, data):
        if not self.root:
            raise Exception("Empty!")
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
        else:
            if data < curr.data:
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
                    # replacement here, NOT ACTUAL DELETION!
                    successor = self._find_min(curr.right)
                    curr.data = successor.data
                    curr.right = self._remove(curr.right, successor.data)
            return curr

    def is_bst(self):
        if not self.root:
            return False
        else:
            return self._is_bst(self.root, float("-inf"), float("inf"))

    def _is_bst(self, curr, min, max):
        if not curr:
            return True
        else:
            curr_valid = min < curr.data < max
            left_valid = self._is_bst(curr.left, min, curr.data)
            right_valid = self._is_bst(curr.right, curr.data, max)
            return left_valid and curr_valid and right_valid

def main():
    data = random.sample(range(100), 10)
    print(data)
    bst = BinarySearchTree()
    for item in data:
        bst.insert(item)
    #bst.preorder()
    bst.inorder()
    #bst.postorder()
    print(bst.is_bst())
    #print(str(data[4]))
    #print(str(bst.get(data[4]).data))
    #print(str(bst.get(101)))
    #print(bst.find(data[4]))
    print(bst.find(900))
    for item in data:
        bst.remove(item)
        bst.inorder()

if __name__ == "__main__":
    main()

