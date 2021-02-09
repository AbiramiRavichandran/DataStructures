from typing import List


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def is_heap(root: Node = None):
    if not root:
        return True
    q = [root]
    flag = True
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
            if not flag or node.data < node.left.data:
                return False
        else:
            flag = False
        if node.right:
            q.append(node.right)
            if not flag or node.data < node.right.data:
                return False
        else:
            flag = False
    return True

def is_heap(arr: List[int]):
    i = len(arr) - 1
    while i > 0:
        p = (i - 1) // 2
        if arr[p] < arr[i]:
            return False
        i -= 1
    return True




if __name__ == "__main__":
    root = Node(10)
    root.left = Node(9)
    root.right = Node(8)
    root.left.left = Node(7)
    root.left.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(4)
    root.left.left.left = Node(3)
    root.left.left.right = Node(2)
    root.left.right.left = Node(1)

    #print(is_heap(root))
    print(is_heap([90, 15, 10, 7, 12, 2]))
