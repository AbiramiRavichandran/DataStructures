class Node:
    max_sum_result = float("-inf")

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def find_max(self):
        lmax = self.left.find_max() if self.left else 0
        rmax = self.right.find_max() if self.right else 0

        max_single = max(max(lmax, rmax) + self.data, self.data)
        max_top = lmax + rmax + self.data
        Node.max_sum_result = max(Node.max_sum_result, max_top)

        return max_single



if __name__ == "__main__":
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    root.find_max()
    print(Node.max_sum_result)





