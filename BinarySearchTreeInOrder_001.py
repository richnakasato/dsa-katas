'''
Binary search tree iterative in order traversal.

Interface and run times:
- inorder(root) -> O(n)

Time to implement:
- start         -> ???
- duration      -> ???

'''
class Node():

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def do_stuff(curr):
    assert curr, "curr should not be null"
    print("{} ".format(curr.data))

def inorder(root):
    assert root, "root should not be null"
    stack = list()
    curr = root
    done = False
    while not done:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            if stack:
                curr = stack.pop()
                do_stuff(curr)
                curr = curr.right
            else:
                done = True

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
    inorder(root)

if __name__ == "__main__":
    main()
