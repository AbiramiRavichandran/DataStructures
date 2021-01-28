class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data > data:
            self.left = self.left.insert(data) if self.left else Node(data)
        if self.data < data:
            self.right = self.right.insert(data) if self.right else Node(data)
        return self

def find_sum_pair(root, sum):
    if not root:
        return False
    if find_sum_pair(root.left, sum):
        return True
    if find_sum_pair.arr and (sum - root.data) in find_sum_pair.arr:
        print("Pair found : ({0},{1})".format(root.data, sum - root.data))
        return True
    else:
        find_sum_pair.arr.append(root.data)
    return find_sum_pair(root.right, sum)

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = Node(elements[0])

    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root

if __name__ == "__main__":
    elements = [15, 10, 20, 8, 12, 16, 25]
    root = build_tree(elements)
    find_sum_pair.arr = []
    find_sum_pair(root, 33)