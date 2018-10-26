'''
Binary search tree iterative level order traversal.

Interface and runtime/space:
- levelorder(root) -> O(n)/O(n)???

Time to implement:
- start         -> 15:42:40
- duration      -> ~6 minutes

'''
from collections import deque

class Node():

    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

def do_stuff(curr):
    assert curr, "curr should not be null"
    print("{}".format(curr.data))

def levelorder(root):
    assert root, "root should not be null"
    queue = deque()
    queue.append(root)
    while queue:
        curr = queue.popleft()
        do_stuff(curr)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    root = n4
    n4.left = n2
    n4.right = n6
    n2.left = n1
    n2.right = n3
    n6.left = n5
    n6.right = n7
    levelorder(root)

if __name__ == "__main__":
    main()
