import math
import heapq
from collections import OrderedDict

# 각 점간의 거기를 계산
def calculate_distance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# 모든 점의 거리 계산
def calculate_distance_all(nodes):
    
    calculated_distances = {} # 이미 계산한 거리를 저장하는 딕셔너리
    distance_graph = [] # 모든 점의 거리가 계산된 리스트

    for node1_name, node1 in nodes.items():
        for node2_name, node2 in nodes.items():
            # 같은 점이거나 이미 계산한 점들간의 거리를 제외
            if node1_name != node2_name and (node1_name, node2_name) not in calculated_distances:
                # 계산한 각 점의 거리를 저장
                distance = calculate_distance(node1, node2)
                distance_graph.append((node1_name, node2_name, distance))
                # 계산한 각 점과 거리는 딕셔너리에 넣어서 제외
                calculated_distances[(node1_name, node2_name)] = distance
                calculated_distances[(node2_name, node1_name)] = distance
    
    return distance_graph

def prim(graph):
    prim_graph = []  # 트리 T 초기화
    visited = set()  # 방문한 노드를 저장할 집합
    start_node = list(graph)[0][0] # 임의로 시작 노드를 첫 번째 노드로 설정

    # 우선순위 큐를 초기화하고 시작 노드의 모든 간선을 추가
    queue = [(weight, start_node, neighbor) for start_node, neighbor, weight in graph]
    heapq.heapify(queue)

    visited.add(start_node)  # 시작 노드를 방문한 것으로 표시

    while queue: # 우선순위 큐가 빌때까지 반복
        weight, current_node, neighbor = heapq.heappop(queue)  # 우선순위 큐에서 가장 작은 가중치의 간선을 선택

        if neighbor not in visited:  # 선택한 노드가 이미 방문한 노드가 아니라면
            visited.add(neighbor)  # 선택한 노드를 방문한 것으로 표시
            prim_graph.append((current_node, neighbor))  # 해당 간선을 트리 T 에 추가 

            # 현재 노드와 연결된 다른 미방문 노드의 간선을 우선순위 큐에 추가
            for next_start_node, next_neighbor, next_weight in graph:
                # 미방문 노드의 연결할 점이 방문 표시가 안됬고, 방문한 노드가 미방문 노드와 연결되있다면 우선순위 큐에 추가 
                if next_neighbor not in visited and (next_start_node == neighbor or next_start_node == current_node):
                    heapq.heappush(queue, (next_weight, next_start_node, next_neighbor))

    return prim_graph # 트리 T 가 완성되면 리턴

def tsp(prim_graph, distance_graph):
    
    graph = sorted(prim_graph) # 간선 정렬 (A, B, .. H 순으로 정렬)
    reversed_graph = [(t[1], t[0]) for t in graph] # 정렬된 간선 거꾸로
    graph += reversed_graph # 거꾸로 된 간선을 원래의 리스트에 추가
    movement_all = [] # 모든 이동 순서
    travel_distance = 0 # 이동 거리

    start_node = graph[0][0] # 시작을 첫번째 간선의 시작점으로 설정
    current_node = start_node
    movement_all.append(start_node) # 이동한 점을 이동 순서에 저장

    # 프림 알고리즘으로 만든 트리의 간선을 따라서 모든 점들을 방문하고 방문 순서 찾기
    while graph: # 그래프가 빌때까지 반복
        next_node = None
        for line in graph:
            if current_node == line[0]: # 현재 노드에서 시작하는 간선이 그래프에 있다면
                next_node = line[1] # 해당 간선의 끝 노드를 다음 노드로 설정
                movement_all.append(next_node) # 해당 간선으로 이동한 점을 이동 순서에 저장
                graph.remove(line) # 그래프에서 해당 간선을 제거
                current_node = next_node # 현재 노드를 다음 노드로 설정
                break

    # 중복 방문 제거
    movement = list(OrderedDict.fromkeys(movement_all))
    # 마지막 점 추가
    movement.append(movement_all[-1])

    # 총 이동 거리 계산
    for i in range(len(movement) - 1):
        current_node = movement[i]
        next_node = movement[i + 1]

        # 완성된 TSP 방문순서를 전부 확인해서 좌표간의 거리가 계산된 그래프와 비교해서 이동 거리 계산
        for line in distance_graph:
            if (line[0] == current_node and line[1] == next_node) or (line[1] == current_node and line[0] == next_node):
                travel_distance += line[2]
                break
    
    return movement, travel_distance

# 각 점의 좌표
nodes = { 'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3), 'E': (1, 0), 'F': (5, 3), 'G': (2, 2), 'H': (4, 1) }

# 모든 점간의 거리 계산
distance_graph = calculate_distance_all(nodes)
# prim 알고리즘 실행
prim_graph = prim(distance_graph)
# tsp 알고리즘 실행 (매개변수 : 프림 알고리즘 결과 및 각 점간의 거리 그래프)
movement, travel_distance = tsp(prim_graph, distance_graph)

# 결과 출력
print("이동 순서 : " + str(movement))
print("이동 거리 : " + str(travel_distance))