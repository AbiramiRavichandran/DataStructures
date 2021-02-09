class k_ary_heap:
    def __init__(self, k):
        self.items = []
        self.k = k

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insert_data(self, data):
        index = len(self.items)
        self.items.append(data)
        self.restore_up(index)


    def restore_up(self, i):
        while i != 0:
            p = self.get_parent(i)
            if self.items[p] < self.items[i]:
                self.swap(i, p)
            i = p

    def restore_down(self, i):
        largest = i
        for j in range(self.k):
            c = self.get_child(i, j)
            if c < len(self.items) and self.items[c] > self.items[largest]:
                largest = c
        if i != largest:
            self.swap(i, largest)
            self.restore_down(largest)

    def get_parent(self, i):
        return (i - 1) // self.k

    def get_child(self, i, position):
        return i * self.k + (position + 1)

    def get_max(self):
        if self.items:
            return self.items[0]

    def extract_max(self):
        if not self.items:
            return None
        largest = self.get_max()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.restore_down(0)
        return largest

    def modify_key(self, key, val):
        i = self.items.index(key)
        self.items[i] = val
        if key < val:
            self.restore_up(i)
        else:
            self.restore_down(i)

    def delete_key(self, key):
        i = self.items.index(key)
        self.items[i] = self.items[-1]
        del self.items[-1]
        self.restore_down(i)


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 8, 9, 10]
    h = k_ary_heap(3)
    h.insert_data(4)
    h.insert_data(5)
    h.insert_data(6)
    h.insert_data(7)
    h.insert_data(8)
    h.insert_data(9)
    h.insert_data(10)

    h.extract_max()
    h.delete_key(8)
    h.modify_key(7, 2)
    h.modify_key(6, 10)


    print(h.items)
