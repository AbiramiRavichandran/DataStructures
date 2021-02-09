class Node:
    def __init__(self, arr, k):
        self.points = [] * k
        for i in range(k):
            self.points[i] = arr[i]
        self.left = self.right = None


class k_D_Tree:
    def __init__(self, k):
        self.k = k
        self.root = None

    def insert_node(self, root, p, depth=0):
        if not root:
            return Node(p, self.k)

        cd = depth % self.k
        if p[cd] < root.points[cd]:
            root.left = k_D_Tree.insert_node(root.left, p, depth + 1)
        else:
            root.right = k_D_Tree.insert_node(root.right, p, depth + 1)

        return root

    def are_same_points(self, s, t):
        for i in range(self.k):
            if s[i] != t[i]:
                return False
        return True

    def copy_points(self, s, t):
        for i in range(self.k):
            s[i] = t[i]

    def search_node(self, root, p, depth=0):
        if not root:
            return False
        if self.are_same_points(root.points, p):
            return True

        cd = depth % self.k
        if p[cd] < root.points[cd]:
            return self.search_node(root.left, p, depth + 1)
        return self.search_node(root.right, p, depth + 1)


    def find_min(self, root, d, depth=0):
        if not root:
            return None
        cd = depth % self.k
        min_node = None
        if cd == k:
            if not root.left:
                return root
            min_node = self.find_min(root.right, d, depth + 1)
        else:
            left = self.find_min(root.left, d, depth + 1)
            right = self.find_min(root.right, d, depth + 1)
            if left is None and right is None:
                return root
            if left is None:
                min_node = right
            elif right is None:
                min_node = left
            else:
                min_node = left if left.points[cd] < right.points[cd] else right

        return root if root.points[d] < min_node.points[d] else min_node



    def delete_node(self, root, p, depth=0):
        if not root:
            return
        cd = depth % self.k
        if self.are_same_points(root.points, p):
            if root.right:
                min_node = self.find_min(root.right, cd, depth + 1)
                root.points.copy(root.points, min_node.points)
                root.right = self.delete_node(root.right, min_node.points, depth + 1)
            elif root.left:
                min_node = self.find_min(root.left, cd, depth + 1)
                root.points.copy(root.points, min_node.points)
                root.left = self.delete_node(root.left, min_node.points, depth + 1)
            else:
                del root
                return None
        elif p[cd] < root.point[cd]:
            root.left = self.delete_node(root.left, p, depth + 1)
        else:
            root.right = self.delete_node(root.right, p, depth + 1)

        return root


if __name__ == "__main__":
    pass