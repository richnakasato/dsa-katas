class SinglyLinkedList():

    class Node():

        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return_string = 'linked-list: '
        curr = self.root
        while curr:
            return_string = return_string + str(curr.data) + ' '
            curr = curr.next
        return return_string

    def __len__(self):
        return self.size

    def insert_iter(self, data):
        if not self.root:
            self.root = self.Node(data)
        else:
            curr = self.root
            while curr.next:
                curr = curr.next
            curr.next = self.Node(data)

    def insert(self, data):
        self.root = self._insert(self.root, data)
        self.size += 1

    def _insert(self, curr, data):
        if not curr:
            return self.Node(data)
        else:
            curr.next = self._insert(curr.next, data)
            return curr

    def find(self, data):
        if not self.root:
            raise Exception('Empty!')
        else:
            return self._find(self.root, data)

    def _find(self, curr, data):
        if not curr:
            return False
        else:
            if data == curr.data:
                return True
            else:
                return self._find(curr.next, data)

    def remove_iter(self, data):
        if not self.root:
            raise Exception('Empty!')
        else:
            curr = self.root
            if data == curr.data:
                self.root = curr.next
            else:
                prev = None
                while curr:
                    if data == curr.data:
                        prev.next = curr.next
                        break
                    prev = curr
                    curr = curr.next

    def remove(self, data):
        if not self.root:
            raise Exception('Empty!')
        else:
            self.root = self._remove(self.root, data)

    def _remove(self, curr, data):
        if not curr:
            return None
        if curr:
            if data == curr.data:
                self.size -= 1
                return curr.next
            else:
                curr.next = self._remove(curr.next, data)
                return curr

    def reverse_iter(self):
        if self.root and self.root.next:
            prev = None
            curr = self.root
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            self.root = prev

    def reverse(self):
        if not self.root:
            raise Exception('Empty!')
        else:
            self.root = self._reverse(self.root, None)

    def _reverse(self, curr, prev):
        if not curr:
            return prev
        else:
            next_node = curr.next
            curr.next = prev
            return self._reverse(next_node, curr)

    def pop_head(self):
        if self.root:
            ret_val = self.root
            self.remove(self.root.data)
            return ret_val.data
        else:
            return self.root


def main():
    ll = SinglyLinkedList()
    ll.insert(8)
    ll.insert(6)
    ll.insert(4)
    ll.insert(2)
    ll.insert(0)
    ll.insert(9)
    ll.insert(7)
    ll.insert(5)
    ll.insert(3)
    ll.insert(1)
    print(ll)
    ll.reverse()
    print(ll)
    ll.reverse_iter()
    print(ll)
    print(str(ll.find(9)))
    print(str(ll.find(19)))
    print(str(ll.find(10)))
    ll.remove(7)
    ll.remove(19)
    ll.remove(1)
    print(ll)
    print(len(ll))
    ll.remove_iter(0)
    ll.remove_iter(4)
    ll.remove_iter(8)
    ll.remove_iter(3)
    ll.remove_iter(33)
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    #print(str(ll.pop_head()))
    print(ll)


if __name__ == "__main__":
    main()

