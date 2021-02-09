class Leftish_Tree:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.dist = 0


class Leftish_Heap:
    def __init__(self):
        self.root = None

    @staticmethod
    def merge_trees(h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h2.data < h1.data:
            h1, h2 = h2, h1
        if not h1.left:
            h1.left = h2
        else:
            h1.right = Leftish_Heap.merge_trees(h1.right, h2)
            if h1.left.dist < h1.right.dist:
                h1.left, h1.right = h1.right, h1.left
            h1.dist = h1.right.dist + 1
        return h1


    def insert_data(self, data):
        t = Leftish_Tree(data)
        return Leftish_Heap.merge_trees(self.root, t)

    def extract_min(self):
        l_tree = self.root.left
        r_tree = self.root.right
        del self.root
        return Leftish_Heap.merge_trees(l_tree, r_tree)

    def print_leftish_heap(self):
        if not self.root:
            return
        q = [self.root]
        while q:
            n = len(q)
            while n:
                node = q.pop(0)
                print("{0}({1}) ".format(node.data, node.dist), end=" ")
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                n -= 1
            print()




if __name__ == "__main__":
    l_heap = Leftish_Heap()
    l_heap.root = l_heap.insert_data(19)
    l_heap.root = l_heap.insert_data(27)
    l_heap.root = l_heap.insert_data(23)
    l_heap.root = l_heap.insert_data(20)
    l_heap.root = l_heap.insert_data(12)
    l_heap.root = l_heap.insert_data(15)
    l_heap.root = l_heap.insert_data(25)
    l_heap.root = l_heap.insert_data(4)
    l_heap.root = l_heap.insert_data(8)

    l_heap.root = l_heap.extract_min()
    l_heap.root = l_heap.insert_data(10)


    l_heap.print_leftish_heap()






