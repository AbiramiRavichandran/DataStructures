class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_node(self, data):
        if self.next:
            self.next.add_node(data)
        else:
            self.next = LLNode(data)

    def print_ll(self):
        print(self.data, end=" ")
        if self.next:
            self.next.print_ll()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def in_order(self):

        if self.left:
            self.left.in_order()

        print(self.data, end=" ")

        if self.right:
            self.right.in_order()



def construct_tree(head):
    q = []
    root = None
    temp = head

    while temp:

        if not root:
            root = TreeNode(temp.data)
            q.append(root)
            temp = temp.next
        else:
            node = q.pop(0)
            node.left = TreeNode(temp.data)
            temp = temp.next
            q.append(node.left)
            if temp:
                node.right = TreeNode(temp.data)
                q.append(node.right)
                temp = temp.next

    return root









if __name__ == "__main__":

    list = [10, 12, 15, 25, 30, 36]
    head = LLNode(list[0])
    for i in range(1, len(list)):
        head.add_node(list[i])
        i += 1

    #head.print_ll()
    root = construct_tree(head)
    root.in_order()
