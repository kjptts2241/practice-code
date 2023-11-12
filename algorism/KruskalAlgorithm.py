# union find 자료 구조 초기화 함수
def disjoint_sets(n):
    parent = [i for i in range(n)]
    return parent

def kruskal(graph, node_num):
    outputT = []  # 트리 T 초기화
    parent = disjoint_sets(node_num)  # node 만큼 union find 자료 구조 초기화

    # 간선을 가중치로 정렬
    edges_sort = sorted(graph, key=lambda edge: edge[2])

    # 정렬된 간선을 하나씩 사이클 검사하면서 트리 T에 추가
    for edge in edges_sort:
        node1, node2, weight = edge
        # node1과 node2가 같은 집합에 속해있지 않다면 (사이클이 없음)
        # 해당 간선을 트리 T 에 추가, union 함수로 두개의 node를 같은 집합에 넣기
        if find(parent, node1) != find(parent, node2):
            outputT.append(edge)
            union(parent, node1, node2)

    return outputT # 트리 T 가 완성되면 리턴

# 해당 node가 어디 집합에 있는 찾아주는 함수
def find(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find(parent, parent[node])
    return parent[node]

# 서로 다른 node1과 node2를 같은 집합에 넣기
def union(parent, node1, node2):
    parent_node1 = find(parent, node1)
    parent_node2 = find(parent, node2)
    parent[parent_node1] = parent_node2

# 강의자료 15p 그래프
graph = [(0, 1, 8), (0, 3, 2), (0, 4, 4), (1, 2, 1), (1, 3, 4), (1, 5, 2), (2, 5, 1), (3, 4, 3), (3, 5, 7), (4, 5, 9)]

# kruskal 알고리즘 실행
node_num = 6  # node 수
outputT = kruskal(graph, node_num)

# 결과 출력
for edge in outputT:
    print(edge)