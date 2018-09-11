import random

class StackLinkedList():

    class Node():

        def __init__(self, data, next_=None):
            self.data = data
            self.next = next_


    def __init__(self):
        self.dummy = self.Node(None)
        self.size = 0

    def __str__(self):
        outstring = 'stack({})-> '.format(self.size)
        curr = self.dummy
        while curr.next:
            outstring += '{}-> '.format(curr.next.data)
        outstring += 'NULL'
        return outstring

    def __len__(self):
        return self.size

    def push(self, data):
        self.dummy.next = self.Node(data, self.dummy.next)

    def pop(self):
        if not self.dummy.next:
            raise Exception('empty stack!')
        else:
            temp = self.dummy.next.data
            self.dummy.next = self.dummy.next.next
            return temp

    def top(self):
        if not self.dummy.next:
            raise Exception('empty stack!')
        else:
            return self.dummy.next.data

    def is_empty(self):
        return self.size == 0


def main():
    pass

if __name__ == "__main__":
    main()

