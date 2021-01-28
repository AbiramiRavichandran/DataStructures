class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def calculate_ways(root):
    if not root:
        return 0
    ways = 1

    q = []
    q.append(root)

    while q:
        node = q.pop(0)

        child_len = len(node.children)

        ways = ways * factorial(child_len)

        for i in range(child_len):
            q.append(node.children[i])

    return ways

def build_tree():
    root = TreeNode('A')
    B = TreeNode('B')
    K = TreeNode('K')
    D = TreeNode('D')
    E = TreeNode('E')
    I = TreeNode('I')

    K.add_child(TreeNode('N'))
    K.add_child(TreeNode('M'))

    B.add_child(K)
    B.add_child(TreeNode('J'))

    D.add_child(TreeNode('G'))
    E.add_child(TreeNode('C'))
    E.add_child(TreeNode('H'))
    I.add_child(TreeNode('L'))
    E.add_child(I)

    root.add_child(B)
    root.add_child(TreeNode('F'))
    root.add_child(D)
    root.add_child(E)

    return root


if __name__ == "__main__":
    root = build_tree()
    print(calculate_ways(root))