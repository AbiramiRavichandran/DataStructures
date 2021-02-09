def get_product(tree, k):
    level = -1
    p = 1
    n = len(tree)
    for i in range(n):
        if tree[i] == '(':
            level += 1
        elif tree[i] == ')':
            level -= 1
        else:
            if level == k:
                p *= (int(tree[i]) - int('0'))
    return p



if __name__ == "__main__":
    tree = "(0(5(6()())(4()(9()())))(3()())))"
    print(get_product(tree, 2))