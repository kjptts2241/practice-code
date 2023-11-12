import time

INF = float('inf')

def floyd(graph):
    vertex = 10  # 그래프 정점 초기화
    matrix = [[INF] * vertex for _ in range(vertex)] # 정점 수 만큼 inf로 행렬 초기화

    # 각 정점간의 거리 행렬 초기화
    for edge in graph:
        start, end, distance = edge
        matrix[start][end] = distance
        matrix[end][start] = distance  # 반대도 초기화

    # 같은 정점은 0으로 초기화 (서울 -> 서울, 천안 -> 천안, ...)
    for i in range(vertex):
        matrix[i][i] = 0

    # 다이렉트 path와 경유점 k를 지나는 path를 비교해 거리가 짧은 것을 초기화
    for k in range(vertex):
        for i in range(vertex):
            # 경우점 k와 시작점 i는 달라야함
            if i != k:
                for j in range(vertex):
                    # 끝점 j는 경우점 k와 시작점 i와 달라야함
                    if j != k and j != i:
                        matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])       

    return matrix

# 각 지역간의 거리 그래프
graph = [
    #서울(0), 천안(1), 원주(2), 논산(3), 대전(4), 강릉(5), 광주(6), 대구(7), 포항(8), 부산(9)
    (0, 1, 12), (0, 2, 15), (1, 3, 4), (1, 4, 10), (2, 5, 21), (2, 7, 7), (3, 4, 3),
    (3, 6, 13), (4, 7, 10), (5, 8, 25), (6, 9, 15), (7, 8, 19), (7, 9, 9), (8, 9, 5)
]

start = time.time()  # 시작 시간 저장

result = floyd(graph)

# 결과 출력
for row in result:
    print(row)

print()
print("Floyd 알고리즘 실행시간 :", time.time() - start)  # 실행 시간