import queue as Q

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def print_levels(root):
    if not root:
        return
    current = Q.PriorityQueue()
    next_ = Q.PriorityQueue()
    q = [root]
    current.put(root.data)
    while q:
        n = len(q)
        while n:
            node = q.pop(0)
            data = current.get()
            print(data, end=" ")
            if node.left:
                q.append(node.left)
                next_.put(node.left.data)
            if node.right:
                q.append(node.right)
                next_.put(node.right.data)
            n -= 1
        print()
        current, next_ = next_, current




if __name__ == "__main__":
    root = Node(7)
    root.left = Node(6)
    root.right = Node(5)
    root.left.left = Node(4)
    root.left.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(1)

    print_levels(root)