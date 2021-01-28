class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = TreeNode(data)






if __name__ == "__main__":
    AVL_tree = AVLTree()

