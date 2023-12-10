# txt 파일 읽어서 개행 제거 후 정수형 리스트에 저장
with open("input.txt", "r") as f:
    input_list = f.readlines();
    input_list = [int(line.strip()) for line in input_list]

def down_heap(A, n, i):
    bigger = i  # 루트 노드
    left_child = 2 * i + 1 # i의 왼쪽 자식 노드
    right_child = 2 * i + 2 # i의 오른쪽 자식 노드
    
    # 왼쪽 자식이 루트보다 크면 bigger 업데이트
    if left_child < n and A[left_child] > A[i]:
        bigger = left_child
    
    # 오른쪽 자식이 bigger 크면 bigger 업데이트
    if right_child < n and A[right_child] > A[bigger]:
        bigger = right_child
    
    # bigger가 루트가 아니라면 교환하고 재귀적으로 down_heap 호출
    if bigger != i:
        A[i], A[bigger] = A[bigger], A[i]
        down_heap(A, n, bigger)

def heap_sort(A):
    n = len(A)
    
    # 다운 힙으로 힙을 구성
    for i in range(n // 2 - 1, -1, -1):
        down_heap(A, n, i)
    
    # 힙에서 원소를 하나씩 추출하며 정렬
    for i in range(n - 1, 0, -1):
        # 루트 노드와 마지막 원소를 교환하고 최댓값을 뒤로 보냄
        A[i], A[0] = A[0], A[i]
        down_heap(A, i, 0)

    return A

# heap_sort 실행
input_list = heap_sort(input_list)

# 결과 출력
print(input_list)

# output.txt로 결과를 출력
with open("output.txt", "w") as f:
    for value in input_list:
        f.write(f"{value}\n")