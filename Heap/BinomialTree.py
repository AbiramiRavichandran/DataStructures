class BinomialTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.order = 0

    def add_at_end(self, t):
        self.children.append(t)
        self.order += 1


if __name__ == "__main__":
    pass