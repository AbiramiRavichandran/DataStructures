class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def evaluate_expression(self):

        if self.left is None and self.right is None:
            return int(self.data)

        lval = self.left.evaluate_expression() if self.left else 0
        rval = self.right.evaluate_expression() if self.right else 0

        if self.data == "+":
            return lval + rval
        elif self.data == "-":
            return lval - rval
        elif self.data == "*":
            return lval * rval
        elif self.data == "/":
            return lval / rval





if __name__ == '__main__':

    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('20')
    print(root.evaluate_expression())

    root = None

    # creating a sample tree
    root = node('+')
    root.left = node('*')
    root.left.left = node('5')
    root.left.right = node('4')
    root.right = node('-')
    root.right.left = node('100')
    root.right.right = node('/')
    root.right.right.left = node('20')
    root.right.right.right = node('2')
    print(root.evaluate_expression())