class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBst(elements, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    root = Node(elements[mid])
    root.left = sortedArrayToBst(elements, start, mid-1)
    root.right = sortedArrayToBst(elements, mid + 1, end)

    return root

def get_height(root):
    if not root:
        return 0
    lheight = get_height(root.left)
    rheight = get_height(root.right)

    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

def isBalanced(root):
    if root is None:
        return True

    lh = get_height(root.left)
    rh = get_height(root.right)

    if abs(lh - rh) <= 1 and isBalanced(root.right) and isBalanced(root.left):
        return True
    return False


def inorder_traversal(root):
    nodes = []
    if root.left:
        nodes += inorder_traversal(root.left)

    nodes.append(root.data)

    if root.right:
        nodes += inorder_traversal(root.right)

    return nodes

if __name__ == "__main__":
    elements = [1,2,3,4,5,6,7,8]
    root = sortedArrayToBst(elements,0,len(elements)-1)
    print(inorder_traversal(root))
    print(get_height(root))
    print(isBalanced(root))
