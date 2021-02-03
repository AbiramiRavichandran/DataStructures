class Binomial_Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order = self.order + 1

    def print_tree(self):
        q = []
        q.append(self)
        while q:
            n = len(q)
            while n:
                node = q.pop(0)
                print(node.data, end=" ")
                if node.children:
                    q.extend(node.children)
                n -= 1
            print()



class Binomial_Heap:
    def __init__(self):
        self.heap = []

    def insert_data(self, data):
        new_heap = Binomial_Heap()
        new_heap.heap.append(Binomial_Tree(data))
        self.merge_heap(new_heap)

    def combine_roots(self, h):
        self.heap.extend(h.heap)
        self.heap.sort(key=lambda tree: tree.order)

    def merge_heap(self, h):
        self.combine_roots(h)
        if not self.heap:
            return
        i = 0
        while i < len(self.heap) - 1:
            current = self.heap[i]
            after = self.heap[i + 1]
            if current.order == after.order:
                if i + 1 < len(self.heap) - 1 and self.heap[i + 2].order == current.order:
                    after_after = self.heap[i + 2]
                    if after.data < after_after.data:
                        after.add_at_end(after_after)
                        del self.heap[i + 2]
                    else:
                        after_after.add_at_end(after)
                        del self.heap[i + 1]
                else:
                    if current.data < after.data:
                        current.add_at_end(after)
                        del self.heap[i + 1]
                    else:
                        after.add_at_end(current)
                        del self.heap[i]
            if i < len(self.heap) - 1 and self.heap[i].order != self.heap[i + 1].order:
                i += 1

    def get_smallest_node(self):
        min_node = self.heap[0]
        for tree in self.heap:
            if tree.data < min_node.data:
                min_node = tree
        return min_node

    def get_min(self):
        min_node = self.get_smallest_node()
        return min_node.data

    def extract_min(self):
        min_node = self.get_smallest_node()
        self.heap.remove(min_node)
        h = Binomial_Heap()
        h.heap.append(min_node.children)
        self.merge_heap(h)

    def print_heap(self):
        i = 1
        for tree in self.heap:
            print("Tree {0} : ".format(i))
            tree.print_tree()
            print()
            i += 1

def heap_builder(elements):
    heap = Binomial_Heap()
    for i in range(len(elements)):
        heap.insert_data(elements[i])
    return heap


if __name__ == "__main__":
    bheap = Binomial_Heap()
    bheap.insert_data(15)
    bheap.insert_data(33)
    bheap.insert_data(28)
    bheap.insert_data(41)
    bheap.insert_data(7)
    bheap.insert_data(25)
    bheap.insert_data(12)

    bheap2 = heap_builder([6, 44, 10, 17, 29, 31, 48, 50, 8, 22, 23, 24, 30, 32, 45, 55, 3, 37, 18])
    bheap.merge_heap(bheap2)

    bheap.print_heap()
