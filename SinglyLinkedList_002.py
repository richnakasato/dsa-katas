class SinglyLinkedList(object):

    class Node(object):

        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        ret_val = ''
        curr = self.head
        while curr:
            ret_val += str(curr.data) + ' '
            curr = curr.next
        return ret_val

    def __len__(self):
        return self.size

    def push_first(self, data):
        temp = self.Node(data)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def get_first(self):
        if not self.head:
            return None
        else:
            return self.head.data

    def pop_first(self):
        temp = None
        if self.head:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
        return temp.data

    def push_last(self, data):
        curr = self.head
        if curr:
            while curr.next:
                curr = curr.next
            curr.next = self.Node(data)
            self.size += 1


def main():
    sll = SinglyLinkedList()
    sll.push_first(8)
    sll.push_first(11)
    sll.push_first(27)
    print(len(sll))
    print(sll)
    print(sll.get_first())
    print(sll.pop_first())
    print(len(sll))
    print(sll)
    print(sll.pop_first())
    print(len(sll))
    print(sll)
    sll.push_last(99)
    sll.push_last(56)
    print(len(sll))
    print(sll)
    pass

if __name__ == "__main__":
    main()

