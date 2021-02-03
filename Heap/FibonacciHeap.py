class Fibonacci_Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.order = 0
        self.parent = self.left = self.right = None

    def add_at_end(self, t):
        self.children.append(t)
        t.parent = self
        self.order += 1

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



class Fibonacci_Heap:
    def __init__(self):
        self.least = None
        self.count = 0


    def merge_heap(self, h):
        if self.count == 0:
            self.least, self.count = h.least, h.count
            return
        self.count += h.count
        self.least.right.left = h.least.left
        h.least.left.right = self.least.right
        self.least.right = h.least
        h.least.left = self.least
        if self.least.data > h.least.data:
            self.least = h.least


    def insert_data(self, data):
        h = Fibonacci_Heap()
        t = Fibonacci_Tree(data)
        t.left = t.right = t
        h.least = t
        h.count = 1
        self.merge_heap(h)


    def get_min(self):
        if self.least:
            return self.least.datatra

    def extract_min(self):
        if self.count == 0:
            return
        least = self.least
        if self.count > 1:
            least.left.right = least.right
            least.right.left = least.left
            self.least = least.left
            itr = self.least.left
            while itr != least.left:
                if itr.data < self.least.data:
                    self.least = itr
                itr = itr.left
        else:
            self.least = None

        self.count -= 1
        for child in least.children:
            h = Fibonacci_Heap
            child.parent = None
            child.left = child.right = child
            h.least = child
            h.count = 1
            self.merge_heap(h)
        del least
        self.consolidate_fibonacci()

    def decrease_key(self, key, val):
        itr = self.least
        count = 1
        flag = 0
        while count <= self.count and flag == 0:
            count += 1
            if itr.data == key:
                itr.data = val
                flag = 1
            else:
                q = []
                q.append(itr)
                while q and flag == 0:
                    parent = q.pop(0)
                    for child in parent.children:
                        q.append(child)
                        if child.data == key:
                            child.data = val
                            c = child
                            while c.parent and c.data < c.parent.data:
                                c.data, c.parent.data = c.parent.data, c.data
                                c = c.parent
                            flag = 1
            if flag and self.least.data > itr.data:
                self.least = itr
        return flag


    def delete_key(self, key):
        if self.decrease_key(key, float('-inf')):
            self.extract_min()



    def get_order_map(self):
        order_map = dict()
        itr = self.least
        count = 1
        while count <= self.count:
            try:
                order_map[itr.order].append(itr)
            except KeyError:
                order_map[itr.order] = [itr]
            itr = itr.left
            count += 1
        return order_map


    def consolidate_fibonacci(self):
        order_map = self.get_order_map()
        while len(order_map.keys()) != self.count:
            for key in list(order_map):
                while len(order_map[key]) > 1:
                    parent = order_map[key].pop(0)
                    child = order_map[key].pop(0)
                    if parent.data > child.data:
                        parent, child = child, parent
                    child.left.right = child.right
                    child.right.left = child.left
                    child.right = child.left = None
                    parent.add_at_end(child)
                    self.count -= 1
                    try:
                        order_map[parent.order].append(parent)
                    except KeyError:
                        order_map[parent.order] = [parent]
                if len(order_map[key]) == 0:
                    del order_map[key]


    def print_fibonacci_heap(self):
        itr = self.least
        count = 1
        while count <= self.count:
            print("Tree {0} : ".format(count))
            itr.print_tree()
            itr = itr.left
            count += 1


if __name__ == "__main__":
    f_heap = Fibonacci_Heap()
    f_heap.insert_data(3)
    f_heap.insert_data(8)
    f_heap.insert_data(4)
    f_heap.insert_data(10)
    f_heap.insert_data(1)
    f_heap.insert_data(7)
    f_heap.insert_data(9)

    f_heap2 = Fibonacci_Heap()
    f_heap2.insert_data(5)
    f_heap2.insert_data(20)

    f_heap.merge_heap(f_heap2)
    f_heap.consolidate_fibonacci()


    f_heap.extract_min()
    f_heap.decrease_key(9, 2)
    f_heap.extract_min()
    f_heap.delete_key(20)


    f_heap.print_fibonacci_heap()
