# 10000개의 20차원 벡터로 이루어진 도형에서 가장 volume이 큰 행렬의 volume 찾기
# input.csv : 20 X 10000 행렬 (20 X 1 벡터가 10000개)
# input file의 첫째 항은 인덱스 표시 (2행부터 21행까지가 실제 벡터 값)

import pandas as pd
import numpy as np
import math
import time

# quick 정렬 함수
def quick_sort(A, left, right):
    if (left < right): # 리스트에 원소가 1개가 아니라면
        p = sorting(A, left, right)
        quick_sort(A, left, p-1) # pivot 보다 작은 그룹 재귀정렬
        quick_sort(A, p, right) # pivot와 pivot 보다 큰 그룹 재귀정렬

    return A

# pivot보다 큰수와 작은수로 구분하고 pivot index return
def sorting(A, left, right):
    pivot = A[(left + right) // 2] # 한 가운데 숫자를 pivot 지정

    while left <= right: # left가 right보다 작을때까지
        while A[left][1] < pivot[1]: # pivot보다 왼쪽의 값이 클때까지 left를 오른쪽으로 한칸씩 이동
            left += 1
        while A[right][1] > pivot[1]: # pivot보다 오른쪽의 값이 작을때까지 right를 왼쪽으로 한칸씩 이동
            right -= 1
        
        if left <= right: # left가 right 보다 작다면
            A[left], A[right] = A[right], A[left] # pivot보다 작은 값을 왼쪽으로 pivot 큰 값을 오른쪽으로 교환
            left, right = left + 1, right - 1 # 교환 후 left 오른쪽 한칸 이동, right 왼쪽 한칸 이동
        
    return left # pivot 자리 index return

# volume 계산 함수
def volume(matrix):
    vt = matrix # vector
    trans_vt = np.transpose(matrix) # vector의 전치행렬
    dot_vt = np.dot(trans_vt, vt) # vector transpose * vector
    det_vt = np.linalg.det(dot_vt) # det 계산
    volume = math.sqrt(det_vt)  # 루트 계산
    
    return volume

start = time.time()

# input.csv 읽어오기
input = pd.read_csv('C:/donga/algorism/input.csv', header=0)

vt_volume = [] # 각 벡터의 volume 저장 리스트
matrix = [] # 전체 행렬

for row in range(len(input.columns)):
    matrix.append(input.iloc[:, row].tolist()) # 리스트 형식으로 행렬에 20x1 벡터 저장
    matrix[row] = [[num] for num in matrix[row]] # 각 벡터안의 숫자를 개별 리스트로 변환
    vt_volume.append([row, volume(matrix[row])]) # 벡터의 volume 저장


# 각 벡터의 volume quick 정렬
vt_volume = quick_sort(vt_volume, 0, len(vt_volume)-1)
# 20개의 가장 높은 volume의 index를 저장
max_idx = [item[0] for item in vt_volume[-20:]]


max_volume_vt = [] # 20개의 높은 volume의 벡터 리스트
for idx in max_idx:
    max_volume_vt.append(matrix[idx]) # volume이 높은 벡터들을 저장

volume = volume(np.hstack(max_volume_vt)) # volume이 높은 벡터들을 병합 후 volume 계산

end = time.time()
running_time = end - start

print("최대 volume :", volume)
print("해당 벡터의 집합 :", max_idx)
print(f"running time : {running_time:.1f} 초")
print("performance metric value :", volume / running_time)