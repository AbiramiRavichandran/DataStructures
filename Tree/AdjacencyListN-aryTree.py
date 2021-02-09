from collections import deque
adj = [[] for i in range(100)]

def count_nodes(root):
    count = 0
    q = deque()
    q.append(root)

    while q:
        node = q.popleft()
        for i in adj[node]:
            child = i
            if len(adj[child]) > len(adj[node]):
                count += 1
            q.append(child)
    return count


if __name__ == "__main__":
    adj[1].append(2)
    adj[1].append(3)
    adj[2].append(4)
    adj[2].append(5)
    adj[2].append(6)
    adj[3].append(9)
    adj[5].append(7)
    adj[5].append(8)

    root = 1
    print(count_nodes(root))