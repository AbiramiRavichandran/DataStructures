class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVL:

    def add_child(self, root, data):

        # step1 : normal BST insert
        if root is None:
            return Node(data)

        if data < root.data:
             root.left = self.add_child(root.left, data)

        else:
             root.right = self.add_child(root.right, data)

        #step2 : update the height of ancestor
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        #step 3 : get balance factor
        balance = self.get_balance(root)

        #step 4 : if node is unbalanced, try following 4 cases

        # case 1 : Left Left
        if balance > 1 and data < root.left.data:
            return self.right_rotate(root)

        # case 2 : Right Right
        if balance < -1 and data > root.right.data:
            return self.left_rotate(root)

        # case 1 : Left Right
        if balance > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # case 1 : Right Left
        if balance < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)


        return root

    def left_rotate(self, root):
        x = root.right
        y = x.left

        x.left = root
        root.right = y

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def right_rotate(self, root):
        x = root.left
        y = x.right

        x.right = root
        root.left = y

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)



    def in_order_traversal(self, root):
        elements = []

        if root.left:
            elements += self.in_order_traversal(root.left)

        elements.append(root.data)

        if root.right:
            elements += self.in_order_traversal(root.right)

        return elements





if __name__ == "__main__":
    elements = [10,20,30,40,50]
    MyTree = AVL()
    root = None

    for i in range(len(elements)):
        root = MyTree.add_child(root, elements[i])

    print("In order traversal gives this sorted list:", MyTree.in_order_traversal(root))
    print(root.left.height, root.right.height)
# print("Height: ", numbers_tree.get_maxdepth())
# numbers_tree.del_node(23)
# print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
# print("Height: ", numbers_tree.get_maxdepth())
# numbers_tree.del_node(9)
# print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
# print("Height: ", numbers_tree.get_maxdepth())
