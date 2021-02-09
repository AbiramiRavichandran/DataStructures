#specific level order traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def print_specific_level_order_traversal(root):
    if not root:
        return
    print(root.data, end=" ")
    q = []
    if root.left:
        print(root.left.data, end=" ")
        print(root.right.data, end=" ")
        q.append(root.left)
        q.append(root.right)

    while q:
        first = q.pop(0)
        second = q.pop(0)

        if first.left:
            print("{0} {1} {2} {3}".format(first.left.data, second.right.data, first.right.data, second.left.data), end=" ")
            q.append(first.left)
            q.append(second.right)
            q.append(first.right)
            q.append(second.left)

def print_specific_level_order_traversal_2(root):
    if not root:
        return
    s = []
    q = [root.data]
    if root.left:
        s.append(root.left)
        s.append(root.right)

    while s:
        n = len(s)
        temp = []
        while n:
            first = s.pop(0)
            temp.append(first.data)
            second = s.pop(0)
            temp.append(second.data)

            if first.left:
                s.append(first.left)
                s.append(second.right)
                s.append(first.right)
                s.append(second.left)
            n -= 2
        temp.extend(q)
        q = temp

    print(q)




if __name__ == "__main__":
    # Perfect Binary Tree of Height 4
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    root.left.left.left.left = Node(16)
    root.left.left.left.right = Node(17)
    root.left.left.right.left = Node(18)
    root.left.left.right.right = Node(19)
    root.left.right.left.left = Node(20)
    root.left.right.left.right = Node(21)
    root.left.right.right.left = Node(22)
    root.left.right.right.right = Node(23)
    root.right.left.left.left = Node(24)
    root.right.left.left.right = Node(25)
    root.right.left.right.left = Node(26)
    root.right.left.right.right = Node(27)
    root.right.right.left.left = Node(28)
    root.right.right.left.right = Node(29)
    root.right.right.right.left = Node(30)
    root.right.right.right.right = Node(31)

    print_specific_level_order_traversal(root)
    print()
    print_specific_level_order_traversal_2(root)