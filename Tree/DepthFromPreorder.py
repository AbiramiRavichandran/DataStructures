def find_depth(tree, n):
    if find_depth.index > n or tree[find_depth.index] == 'l':
        return 0
    find_depth.index += 1
    left = find_depth(tree, n)
    find_depth.index += 1
    right = find_depth(tree, n)
    return max(left, right) + 1


if __name__ == "__main__":
    tree = "nlnnlll"
    find_depth.index = 0
    print(find_depth(tree, len(tree) - 1))
