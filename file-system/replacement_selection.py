import heapq

# replacement_selection 함수
def replacement_selection(numbers, buffer_size):
    runs = [] # 전체 run들
    buffer = numbers[:buffer_size] # 버퍼 사이즈만큼 버퍼 초기화
    heapq.heapify(buffer) # 버퍼를 힙으로 변경
    current_run = [] # 현재 run
    freeze_elements = [] # 프리즈된 값

    # 입력 리스트의 값들이 없어질때까지
    for elem in numbers[buffer_size:]:
        min_elem = heapq.heappop(buffer) # 버퍼에서 최소 값을 뽑아서
        current_run.append(min_elem) # 현재 run에 추가

        if elem < min_elem: # 입력 리스트에 뽑아온 값이, run에 저장한 값보다 작으면
            freeze_elements.append(elem) # 프리즈 리스트에 저장
        else:
            heapq.heappush(buffer, elem) # 아니면 버퍼에 저장

        if not buffer: # 버퍼가 비었다면 (프리즈의 값의 개수가 버퍼 사이즈만큼 생겼을때)
            runs.append(current_run) # 현재 run을 전체 run에 넣기
            current_run = [] # 새로운 run 시작 (비우기)
            buffer = freeze_elements # 버퍼에 프리즈된 값들을 넣기
            freeze_elements = [] # 프리즈 리스트는 비우기
            heapq.heapify(buffer) # 버퍼를 다시 힙으로 변경

    while buffer: # 버퍼에 값이 남아있다면
        current_run.append(heapq.heappop(buffer)) # 현재 run에 버퍼 값들을 추가하고
    runs.append(current_run) # 전체 run에 추가

    current_run = [] # 새로운 run 시작 (비우기)
    
    heapq.heapify(freeze_elements) # 프리즈 리스트를 힙으로 변경
    while freeze_elements: # 프리즈 리스트에 값이 남아있다면
        current_run.append(heapq.heappop(freeze_elements)) # 현재 run에 프리즈 리스트 값들을 추가하고
    runs.append(current_run) # 전체 run에 추가

    return runs

# 파일 읽기
with open('replacement_input.txt', 'r') as f:
        test_cases = int(f.readline().strip())
        
        with open('replacement_output.txt', 'w') as out:
            for _ in range(test_cases):
                n = int(f.readline().strip())
                numbers = list(map(int, f.readline().split()))
                
                runs = replacement_selection(numbers, 5) # replacement_selection 수행 (buffer size = 5)

                # Test Case들의 replacement_selection를 수행한 run의 개수, run 값을 파일에 저장
                out.write(f"{len(runs)}\n")
                for run in runs:
                    out.write(" ".join(map(str, run)) + "\n")