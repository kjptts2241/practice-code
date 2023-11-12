import time
import heapq

INF = float('inf')

def dijkstra(graph, start):
    vertex = 10  # 그래프 정점 초기화
    
    # 최단 거리를 저장할 배열 초기화
    distance = [INF] * vertex
    distance[start] = 0 # 현재 정점 0으로 초기화
    
    # 우선순위 큐를 사용하여 최단 거리 업데이트
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)
        
        # 현재 정점까지의 거리가 기존에 저장된 거리보다 크면 무시
        if current_dist > distance[current_vertex]:
            continue
        
        # 현재 정점에서 이웃한 정점들을 탐색
        for neighbor, edge_weight in get_neighbors(graph, current_vertex):
            new_distance = distance[current_vertex] + edge_weight
            
            # 새로운 경로가 더 짧으면 업데이트하고 우선순위 큐에 추가
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distance

# 현재 정점에서의 이웃한 정점들을 찾는 함수
def get_neighbors(graph, vertex):
    neighbors = []

    # 그래프에서 첫번째 요소 또는 두번째 요소가 현재 vertex와 같다면 현재 vertex를 제외하고 배열에 저장
    for edge in graph:
        if edge[0] == vertex:
            neighbors.append((edge[1], edge[2]))
        elif edge[1] == vertex:
            neighbors.append((edge[0], edge[2]))

    return neighbors

# 각 지역간의 거리 그래프
graph = [
    #서울(0), 천안(1), 원주(2), 논산(3), 대전(4), 강릉(5), 광주(6), 대구(7), 포항(8), 부산(9)
    (0, 1, 12), (0, 2, 15), (1, 3, 4), (1, 4, 10), (2, 5, 21), (2, 7, 7), (3, 4, 3),
    (3, 6, 13), (4, 7, 10), (5, 8, 25), (6, 9, 15), (7, 8, 19), (7, 9, 9), (8, 9, 5)
]

start = time.time()  # 시작 시간 저장

for start_vertex in range(10):
    result = dijkstra(graph, start_vertex)

    # 결과 출력
    print(result)

print()
print("Dijkstra 알고리즘 실행시간 :", time.time() - start)  # 실행 시간

