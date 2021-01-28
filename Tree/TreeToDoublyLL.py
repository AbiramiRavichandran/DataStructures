class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_node(data):
    new_node = Node(data)
    if construct_doubly_ll.root:
        new_node.right = construct_doubly_ll.root
        construct_doubly_ll.root.left = new_node

    construct_doubly_ll.root = new_node

def construct_doubly_ll(tree):
    if not tree:
        return None
    construct_doubly_ll(tree.right)
    add_node(tree.data)
    construct_doubly_ll(tree.left)









if __name__ == "__main__":
    tree = Node(10)
    tree.left = Node(12)
    tree.right = Node(15)
    tree.left.left = Node(25)
    tree.left.right = Node(30)
    tree.right.left = Node(36)

    construct_doubly_ll.root = None

    construct_doubly_ll(tree)


    itr = construct_doubly_ll.root

    while itr:
        print(itr.data, end=" ")
        itr = itr.right


