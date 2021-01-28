class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def are_isomorphic(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    return (are_isomorphic(t1.left,t2.left) and are_isomorphic(t1.right, t2.right)) or (are_isomorphic(t1.left,t2.right) and are_isomorphic(t1.right, t2.left))

if __name__ == "__main__":
    n1 = Node(1)
    n1.left = Node(2)
    n1.right = Node(3)
    n1.left.left = Node(4)
    n1.left.right = Node(5)
    n1.right.left = Node(6)
    n1.left.right.left = Node(7)
    n1.left.right.right = Node(8)

    n2 = Node(1)
    n2.left = Node(3)
    n2.right = Node(2)
    n2.right.left = Node(4)
    n2.right.right = Node(5)
    n2.left.right = Node(6)
    n2.right.right.left = Node(8)
    n2.right.right.right = Node(7)

    print(are_isomorphic(n1, n2))
