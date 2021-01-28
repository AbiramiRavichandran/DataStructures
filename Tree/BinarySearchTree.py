class BST:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def print_level_order(self, level):
        if level == 1:
            print(self.data, end=" ")
        else:
            if self.left:
                self.left.print_level_order(level - 1)
            if self.right:
                self.right.print_level_order(level - 1)

    def level_order_traversal(self):
        h = self.get_maxdepth() + 1
        for level in range(h):
            self.print_level_order(level)

    def print_spiral(self, level, flip):
        if level == 1:
            print(self.data, end=" ")
        else:
            if flip:
                if self.left:
                    self.left.print_spiral(level - 1, flip)
                if self.right:
                    self.right.print_spiral(level - 1, flip)
            else:
                if self.right:
                    self.right.print_spiral(level - 1, flip)
                if self.left:
                    self.left.print_spiral(level - 1, flip)

    def level_order_spiral(self):
        h = self.get_maxdepth() + 1
        flip = True
        for level in range(h):
            self.print_spiral(level, flip)
            flip = not flip

    def search(self, value):
        if self.data == value:
            return True
        if self.data > value and self.left:
            return self.left.search(value)
        elif self.data < value and self.right:
            return self.right.search(value)
        else:
            return False

    def get_lowest(self):
        if self.left:
            return self.left.get_lowest()
        else:
            return self.data

    def get_highest(self):
        if self.right:
            return self.right.get_highest()
        else:
            return self.data

    def del_node(self, value):
        if value > self.data and self.right:
            self.right = self.right.del_node(value)
        elif value < self.data and self.left:
            self.left = self.left.del_node(value)
        elif self.data == value:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            max_value = self.left.get_highest()
            self.data = max_value
            self.left.del_node(max_value)

        return self

    def get_maxdepth(self):

        ldepth = self.left.get_maxdepth() if self.left else 0
        rdepth = self.right.get_maxdepth() if self.right else 0

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

    def get_diameter(self):

        ldepth = self.left.get_maxdepth() if self.left else 0
        rdepth = self.right.get_maxdepth() if self.right else 0

        ldia = self.left.get_diameter() if self.left else 0
        rdia = self.right.get_diameter() if self.right else 0

        return max(ldepth + rdepth + 1, max(ldia, rdia))

    def get_lowest_common_ancestor(self, n1, n2):
        if self.data > n1 and self.data > n2 and self.left:
            return self.left.get_lowest_common_ancestor(n1, n2)

        if self.data < n1 and self.data < n2 and self.right:
            return self.right.get_lowest_common_ancestor(n1, n2)

        return self

    def is_balanced(self):
        lh = rh = 0
        is_l_balanced = is_r_balanced = 1

        if self.left:
            lh = self.left.get_maxdepth()
            is_l_balanced = self.left.is_balanced()
        if self.right:
            rh = self.right.get_maxdepth()
            is_r_balanced = self.right.is_balanced()

        return abs(lh - rh) <= 1 and is_l_balanced and is_r_balanced

    def count_half_nodes(self):

        if self.left and self.right:
            return self.left.count_half_nodes() + self.right.count_half_nodes()
        if self.left is None and self.right:
            return 1 + self.right.count_half_nodes()
        if self.right is None and self.left:
            return 1 + self.left.count_half_nodes()
        return 0

    def print_singles(self):
        if self.left is None and self.right is None:
            return
        if not self.left:
            print(self.right.data)
            self.right.print_singles()
        elif not self.right:
            print(self.left.data)
            self.left.print_singles()
        else:
            self.left.print_singles()
            self.right.print_singles()


    def count_full_nodes(self):
        if self.left and self.right:
            return 1 + self.left.count_full_nodes() + self.right.count_full_nodes()
        if self.left is None and self.right:
            return self.right.count_full_nodes()
        if self.right is None and self.left:
            return self.left.count_full_nodes()
        return 0

    def level_order_traversal_2(self, is_root=True):
        if is_root:
            print(self.data)
        if self.left:
            print(self.left.data)
        if self.right:
            print(self.right.data)
        if self.left:
            self.left.level_order_traversal_2(False)
        if self.right:
            self.right.level_order_traversal_2(False)

    def print_ancestors(self, target):
        if self.data == target:
            return True
        l = self.left.print_ancestors(target) if self.left else False
        r = self.right.print_ancestors(target) if self.right else False
        if l or r:
            print(self.data, end=" ")
            return True
        return False

    def get_distance_of_node(self, data):
        if self.data == data:
            return 0
        l = self.left.get_distance_of_node(data) if self.left else -1
        r = self.right.get_distance_of_node(data) if self.right else -1
        if l >= 0 or r >= 0:
            return max(l, r) + 1
        return -1

    def get_size(self):
        l_size = self.left.get_size() if self.left else 0
        r_size = self.right.get_size() if self.right else 0

        return 1 + l_size + r_size

    def print_kth_largest_num(self, k, c=1):
        if self.right:
            c = self.right.print_kth_largest_num(k, c)
        if c == k:
            print(self.data)
        c += 1
        if self.left:
            c = self.left.print_kth_largest_num(k, c)
        return c




def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


# inorder traversal without recursion

def inorderTraversal(root):
    stack = []
    current = root

    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
        else:
            break


def preOrderTraversal(root):
    stack = []
    current = root

    while True:
        if current:
            stack.append(current)
            print(current.data)
            current = current.left
        elif stack:
            current = stack.pop()
            current = current.right
        else:
            break


def postOrderTraversal(root):
    s1 = []
    s2 = []
    s1.append(root)

    while s1:
        current = s1.pop()
        s2.append(current)
        if current.left:
            s1.append(current.left)
        if current.right:
            s1.append(current.right)

    while s2:
        node = s2.pop()
        print(node.data, end=" ")


def levelOrderTraversal(root):
    queue = []
    temp = root

    while temp:
        print(temp.data)

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        temp = queue.pop(0) if queue else None


def iterative_height(root):
    q = []
    height = 0

    q.append(root)

    while True:
        nodeCount = len(q)
        if nodeCount == 0:
            return height
        height += 1

        while nodeCount > 0:
            node = q.pop(0)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1


def get_leaf_count(root):
    if not root:
        return 0

    q = []
    q.append(root)
    count = 0

    while q:
        current = q.pop(0)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        if current.left is None and current.right is None:
            count += 1

    return count


def search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return i


def print_post_from_in_and_pre(inOrder, preOrder, n):
    root_index = search(inOrder, preOrder[0])

    if root_index != 0:
        print_post_from_in_and_pre(inOrder, preOrder[1:n], root_index)

    if root_index != n - 1:
        print_post_from_in_and_pre(inOrder[root_index + 1:n], preOrder[root_index + 1:n], n - root_index - 1)

    print(preOrder[0])


def get_pre_and_suc(root, key):
    if not root:
        return None

    if root.data == key:
        if root.left:
            temp = root.left
            while temp.right:
                temp = temp.right
            get_pre_and_suc.pre = temp.data if temp else None
        if root.right:
            temp = root.right
            while temp.left:
                temp = temp.left
            get_pre_and_suc.suc = temp.data if temp else None

    if root.data < key:
        get_pre_and_suc.pre = root.data
        get_pre_and_suc(root.right, key)

    if root.data > key:
        get_pre_and_suc.suc = root.data
        get_pre_and_suc(root.left, key)


def print_right_view(root, level):
    if not root:
        return
    if print_right_view.max_level < level:
        print(root.data)
        print_right_view.max_level = level

    print_right_view(root.right, level + 1)
    print_right_view(root.left, level + 1)


def print_left_view(root, level):
    if not root:
        return
    if print_left_view.max_level < level:
        print(root.data)
        print_left_view.max_level = level

    print_left_view(root.left, level + 1)
    print_left_view(root.right, level + 1)


def min_depth(root):
    if not root:
        return 0
    q = []

    q.append({'node': root, 'depth': 1})

    while q:
        q_item = q.pop(0)

        node = q_item['node']
        d = q_item['depth']

        if node.left is None and node.right is None:
            return d
        if node.left:
            q.append({'node': node.left, 'depth': d + 1})
        if node.right:
            q.append({'node': node.right, 'depth': d + 1})


def zig_zag_traversal(root):
    flip = True
    current = []
    next_level = []

    current.append(root)
    while current:
        node = current.pop()
        print(node.data, end=" ")
        if flip:
            if node.right:
                next_level.append(node.right)
            if node.left:
                next_level.append(node.left)
        else:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not current:
            current = next_level
            next_level = []
            flip = not flip


def level_order_line_by_line(root):
    if not root:
        return
    q = []
    q.append(root)
    while True:
        nodeCount = len(q)
        if not q:
            break
        while nodeCount:
            node = q.pop(0)
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            nodeCount -= 1
        print()


def get_level_of_node(root, data, level=1):
    if not root:
        return 0
    if root.data == data:
        return level
    down_level = get_level_of_node(root.left, data, level + 1)
    if down_level != 0:
        return down_level
    return get_level_of_node(root.right, data, level + 1)


def get_max_depth(root):
    max_depth = 0
    if not root:
        return max_depth
    q = []

    q.append(root)

    while q:
        count = len(q)
        if count > max_depth:
            max_depth = count

        while count:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1

    return max_depth


def get_max_width(root):
    if not root:
        return 0
    max_width = 0
    q = []
    q.append(root)

    while q:
        count = len(q)
        if count > max_width:
            max_width = count

        while count:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            count -= 1
    return max_width

def is_complete(root):
    if not root:
        return True
    q = []

    flag = False

    q.append(root)
    while q:
        node = q.pop(0)
        if node.left:
            if flag:
                return False
            q.append(node.left)
        else:
            flag = True
        if node.right:
            if flag:
                return False
            q.append(node.right)
        else:
            flag = True
    return True

def print_leaf_to_node_paths(root, path_array=[]):
    if not root:
        return

    path_array.append(str(root.data))
    if root.left is None and root.right is None:
        print(' '.join(path_array))
    else:
        print_leaf_to_node_paths(root.left, path_array)
        print_leaf_to_node_paths(root.right, path_array)
    path_array.pop()

def print_left_and_right_most_nodes(root):
    if not root:
        return
    q = []
    q.append(root)

    while q:
        n = len(q)

        for i in range(n):
            node = q.pop(0)

            if i == 0 or i == n-1:
                print(node.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


def print_nodes_at_k_distance_from_root(root, k, level=0):
    if not root:
        return
    if level == k:
        print(root.data)
    else:
        print_nodes_at_k_distance_from_root(root.left, k, level + 1)
        print_nodes_at_k_distance_from_root(root.right, k, level + 1)


def get_deepest_node(root, level=0):
    if root:
        if level > get_deepest_node.max:
            get_deepest_node.max = level
            get_deepest_node.res = root.data
        get_deepest_node(root.left, level + 1)
        get_deepest_node(root.right, level + 1)

def find_mirror_node(target, left, right):
    if left is None or right is None:
        return None
    if left.data == target:
        return right.data
    if right.data == target:
        return left.data
    mirror_value = find_mirror_node(target, left.left, right.right)
    if mirror_value:
        return mirror_value
    return find_mirror_node(target, left.right, right.left)



if __name__ == "__main__":
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print(find_mirror_node(9, numbers_tree.left, numbers_tree.right))
    # get_deepest_node.res = -1
    # get_deepest_node.max = -1
    # get_deepest_node(numbers_tree)
    # print(get_deepest_node.max)
    # print(get_deepest_node.res)
    #numbers_tree.print_singles()
    #print_nodes_at_k_distance_from_root(numbers_tree, 0)
    #print_left_and_right_most_nodes(numbers_tree)
    #numbers_tree.print_kth_largest_num(8)
    #print_leaf_to_node_paths(numbers_tree)
    #print(numbers_tree.get_distance_of_node(90))
    #print(numbers_tree.get_size())
    #numbers_tree.print_ancestors(9)
    #print(is_complete(numbers_tree))
    #numbers_tree.level_order_traversal_2()
    #print(get_max_width(numbers_tree))
    # print(get_level_of_node(numbers_tree, 18))
    # print(min_depth(numbers_tree))
    # print_left_view.max_level = 0
    # print_left_view(numbers_tree, 1)
    # print(numbers_tree.count_full_nodes())
    # numbers_tree.level_order_traversal()
    # print()
    # level_order_line_by_line(numbers_tree)
    # numbers_tree.level_order_spiral()
    # print()
    # zig_zag_traversal(numbers_tree)
    # print(numbers_tree.count_half_nodes())
    # print(get_leaf_count(numbers_tree))
    # pre = []
    # suc = []
    #
    # get_pre_and_suc.pre = None
    # get_pre_and_suc.suc = None
    # get_pre_and_suc(numbers_tree, 21)
    #
    # print(get_pre_and_suc.pre, get_pre_and_suc.suc)
    # print(iterative_height(numbers_tree))
    # print("Height: ", numbers_tree.get_maxdepth())
    # print("Post order traversal :", numbers_tree.post_order_traversal())
    # postOrderTraversal(numbers_tree)
    # print(numbers_tree.is_balanced())
    # print_post_from_in_and_pre([4,2,5,1,3,6],[1,2,4,5,3,6],6)
    # lowest_common_ancestor = numbers_tree.get_lowest_common_ancestor(1, 34)
    # print(lowest_common_ancestor.data)
    # print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    # print("In order traversal gives this sorted list:", inorderTraversal(numbers_tree))
    # print("Pre order traversal :", numbers_tree.pre_order_traversal())
    # print("Pre order traversal :")
    # preOrderTraversal(numbers_tree)
    # print("Height: ", numbers_tree.get_maxdepth())
    # print("diameter", numbers_tree.get_diameter())
    # numbers_tree.del_node(23)
    # print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    # print("Height: ", numbers_tree.get_maxdepth())
    # print("diameter", numbers_tree.get_diameter())
    # numbers_tree.del_node(9)
    # print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    # print("Height: ", numbers_tree.get_maxdepth())
    # print("diameter", numbers_tree.get_diameter())
