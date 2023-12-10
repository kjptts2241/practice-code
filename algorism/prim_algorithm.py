import heapq

def prim(graph):
    outputT = []  # 트리 T 초기화
    visited = set()  # 방문한 노드를 저장할 집합
    start_node = 0  # 임의로 시작 노드를 0으로 설정

    # 우선순위 큐를 초기화하고 시작 노드의 모든 간선을 추가
    queue = [(weight, start_node, neighbor) for start_node, neighbor, weight in graph]
    heapq.heapify(queue)

    visited.add(start_node)  # 시작 노드를 방문한 것으로 표시

    while queue: # 우선순위 큐가 빌때까지 반복
        weight, current_node, neighbor = heapq.heappop(queue)  # 우선순위 큐에서 가장 작은 가중치의 간선을 선택

        if neighbor not in visited:  # 선택한 노드가 이미 방문한 노드가 아니라면
            visited.add(neighbor)  # 선택한 노드를 방문한 것으로 표시
            outputT.append((current_node, neighbor, weight))  # 해당 간선을 트리 T 에 추가 

            # 현재 노드와 연결된 다른 미방문 노드의 간선을 우선순위 큐에 추가
            for next_start_node, next_neighbor, next_weight in graph:
                # 미방문 노드의 연결할 점이 방문 표시가 안됬고, 방문한 노드가 미방문 노드와 연결되있다면 우선순위 큐에 추가 
                if next_neighbor not in visited and (next_start_node == neighbor or next_start_node == current_node):
                    heapq.heappush(queue, (next_weight, next_start_node, next_neighbor))

    return outputT # 트리 T 가 완성되면 리턴

# 강의자료 31p 그래프
graph = [(0, 1, 3), (0, 3, 2), (0, 4, 4), (1, 2, 1), (1, 3, 4), (1, 5, 2), (2, 5, 1), (3, 4, 5), (3, 5, 7), (4, 5, 9)]

# prim 알고리즘 실행
outputT = prim(graph)

# 결과 출력
for edge in outputT:
    print(edge)