import math
from collections import OrderedDict
import itertools
import random


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


# tsp 알고리즘 함수
def tsp(candidate, distance_graph):
    
    graph = candidate
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

    movement = list(OrderedDict.fromkeys(movement_all)) # 중복 방문 제거
    movement.append(movement_all[-1]) # 마지막 점 추가

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


# 후보해 초기 선택 함수
def first_candidate(points):
    all_candidate = list(itertools.permutations(points)) # 모든 가능한 순열 생성
    # 순열에서 랜덤하게 8개의 후보해 선택
    random_candidate = [list(candidate) for candidate in random.sample(all_candidate, 8)]
    # 각 후보해에 첫번째 요소를 마지막 요소에도 추가
    for i in range(len(random_candidate)):
        random_candidate[i].append(random_candidate[i][0])

    return random_candidate


# 각 후보해 tsp input 수정 함수
def modifying_tsp_input(candidate):
    # 각 후보해를 tsp input에 맞게 변경
    for i in range(len(candidate)):
        candidate[i].pop() # 각 후보해의 마지막 요소를 제거
        candidate[i] = [(candidate[i][j], candidate[i][j + 1]) for j in range(len(candidate[i]) - 1)]

    return candidate


# 적합도 평가 함수
def evaluation(candidate_fitness):
    total = sum(num[1] for num in candidate_fitness) # 거리만 추출하여 더하기
    # 평균 계산
    average = total / len(candidate_fitness)

    print("총합:", total, "| 평균:", average)


# 후보해 선택 함수
def candidate_selection(candidate_fitness):

    candidate = [] # 이동 순서만 추출할 리스트

    max_candidate = max(candidate_fitness, key=lambda x: x[1]) # 가장 긴 거리를 가진 후보해 찾기
    candidate_fitness.remove(max_candidate)  # 해당 후보해 삭제

    min_candidate = min(candidate_fitness, key=lambda x: x[1]) # 가장 짧은 거리를 가진 후보해 찾기
    candidate_fitness.append(min_candidate) # 후보해 리스트에 추가

    # 이동 거리를 제외하고 이동 순서만 추출
    for i in range(len(candidate_fitness)):
        candidate.append(candidate_fitness[i][0])

    return candidate

def cycle_exchange(list1, list2):
    n = len(list1)
    start_index = 2  # 3번째 요소부터 시작

    while start_index < n:
        temp = list1[start_index]
        list1[start_index] = list2[start_index]
        list2[start_index] = temp
        start_index += 3

# 사이클 교차 연산 함수
def cycle_crossover(candidate):

    last_element = [] # 각 후보해의 마지막 요소

    # 후보해 간의 교환 중 중복 방지를 위해 각 후보해의 마지막 요소 임시 제거
    for i in range(len(candidate)):
        last_element.append(candidate[i][-1])  # 마지막 원소를 빼고 저장
        candidate[i] = candidate[i][:-1]  # 마지막 원소를 제외한 나머지 부분 유지
        # lists[i].append(last_element)  # 뺀 원소를 다시 마지막에 추가

    candidate[0] = ['G', 'H', 'B', 'A', 'E', 'C', 'F', 'D']
    candidate[1] = ['A', 'C', 'E', 'F', 'D', 'B', 'H', 'G']
    print("교차 전 : ", candidate[0], candidate[1])

    candidate[0], candidate[1] = cycle_exchange(candidate[0], candidate[1])

    print("교차 후 : ", candidate[0], candidate[1])

# genetic 알고리즘 함수
def genetic(candidate, distance_graph):

    candidate = modifying_tsp_input(candidate) # 8개의 후보해를 tsp input에 맞게 변경
    candidate_fitness = [] # 각 후보해의 결과를 저장할 리스트
    # # tsp 알고리즘 실행 (8개의 후보해, 각 점간의 거리 그래프)
    for i in range(len(candidate)):
        (movement, travel_distance) = tsp(candidate[i], distance_graph)

        candidate_fitness.append((movement, travel_distance)) # 후보해의 결과를 저장

    evaluation(candidate_fitness)  # 적합도 평가
    candidate = candidate_selection(candidate_fitness) # 후보해 선택
    cycle_crossover(candidate) # 사이클 교차 연산 (3번째 요소 교횐)



# 각 점의 좌표
nodes = { 'A': (0, 3), 'B': (7, 5), 'C': (6, 0), 'D': (4, 3), 'E': (1, 0), 'F': (5, 3), 'G': (2, 2), 'H': (4, 1) }
distance_graph = calculate_distance_all(nodes) # 모든 점간의 거리 계산

points = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 8개의 점 리스트
candidate = first_candidate(points) # 8개의 후보해 선택

# genetic 알고리즘 실행
genetic(candidate, distance_graph)

