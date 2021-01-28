class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_threaded = False

def get_leftmost(root):
    while root and root.left:
        root = root.left
    return root

def in_order(root):
    if not root:
        return
    cur = get_leftmost(root)

    while cur:
        print(cur.data, end=" ")

        if cur.is_threaded:
            cur = cur.right
        else:
            cur = get_leftmost(cur.right)





def create_threaded(root):
    if not root:
        return
    if root.left is None and root.right is None:
        return root
    if root.left:
        l = create_threaded(root.left)
        l.right = root
        l.is_threaded = True
    if root.right:
        return create_threaded(root.right)
    return root

def create_threaded_queue(root):
    if not root:
        return
    in_order_arr = []
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            in_order_arr.append(current)
            current = current.right
        else:
            break

    while in_order_arr:
        node = in_order_arr.pop(0)
        if node.right is None and in_order_arr:
            node.right = in_order_arr[0]
            node.is_threaded = True



if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    create_threaded_queue(root)
    in_order(root)