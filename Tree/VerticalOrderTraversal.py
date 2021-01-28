class Node:
    max = 0
    min = 0
    map = {}

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0

    def top_view(self):
        queue = []
        hd = 0
        m = {}


        queue.append(self)

        while queue:
            root = queue[0]
            hd = root.hd
            if hd not in m:
                m[hd] = root.data

            if root.left:
                queue.append(root.left)
                root.left.hd = hd - 1
            if root.right:
                queue.append(root.right)
                root.right.hd = hd + 1

            queue.pop(0)

        for i in sorted(m.keys()):
            print(m[i], end=" ")






    def get_vertical_order(self, hd):

        try:
            Node.map[hd].append(self.data)
        except:
            Node.map[hd] = []
            Node.map[hd].append(self.data)

        if self.left:
            self.left.get_vertical_order(hd - 1)
        if self.right:
            self.right.get_vertical_order(hd + 1)



    def print_vertical_order_hash(self):
        self.get_vertical_order(0)

        for index, key in enumerate(sorted(Node.map)):
            for value in Node.map[key]:
                print(value, end=" ")
            print()


    # O(n^2)
    def print_vertical_order(self, line_no, hd):
        if line_no == hd:
            print(self.data, end=" ")

        if self.left:
            self.left.print_vertical_order(line_no, hd-1)
        if self.right:
            self.right.print_vertical_order(line_no, hd+1)

    # O(n^2)
    def get_max_and_min(self, hd):

        if hd < Node.min:
            Node.min = hd
        if hd > Node.max:
            Node.max = hd

        if self.left:
            self.left.get_max_and_min(hd-1)
        if self.right:
            self.right.get_max_and_min(hd+1)


    # O(n^2)
    def vertical_order(self):

        self.get_max_and_min(0)

        for i in range(Node.min, Node.max+1):
            self.print_vertical_order(i, 0)
            print()








if __name__ == "__main__":
    # root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)
    # root.right.left.right = Node(8)
    # root.right.right.right = Node(9)
    # print(max, min)
    #
    # print
    # "Vertical order traversal is"
    # root.vertical_order()
    # root.print_vertical_order_hash()

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print("Following are nodes in top",
          "view of Binary Tree")
    root.top_view()

