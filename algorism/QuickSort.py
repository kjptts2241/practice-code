# txt 파일 읽어서 개행 제거 후 정수형 리스트에 저장
with open("inupt_quick_sort.txt", "r") as f:
    input_list = f.readlines();
    input_list = [int(line.strip()) for line in input_list]

def QuickSort(A, left, right):
    if (left < right): # 리스트에 원소가 1개가 아니라면
        p = sorting(A, left, right)
        QuickSort(A, left, p-1) # pivot 보다 작은 그룹 재귀정렬
        QuickSort(A, p, right) # pivot와 pivot 보다 큰 그룹 재귀정렬

    return A

# pivot보다 큰수와 작은수로 구분하고 pivot index return
def sorting(A, left, right):
    pivot = A[(left + right) // 2] # 한 가운데 숫자를 pivot 지정

    while left <= right: # left가 right보다 작을때까지
        while A[left] < pivot: # pivot보다 왼쪽의 값이 클때까지 left를 오른쪽으로 한칸씩 이동
            left += 1
        while A[right] > pivot: # pivot보다 오른쪽의 값이 작을때까지 right를 왼쪽으로 한칸씩 이동
            right -= 1
        
        if left <= right: # left가 right 보다 작다면
            A[left], A[right] = A[right], A[left] # pivot보다 작은 값을 왼쪽으로 pivot 큰 값을 오른쪽으로 교환
            left, right = left + 1, right - 1 # 교환 후 left 오른쪽 한칸 이동, right 왼쪽 한칸 이동
        
    return left # pivot 자리 index return

# QuickSort 실행
input_list = QuickSort(input_list, 0, len(input_list)-1)

# 결과 출력
print(input_list)

