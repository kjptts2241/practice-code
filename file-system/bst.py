# BST 생성 함수
class Node:
    def __init__(self, key):
        self.key = key # 루트 값 초기화
        self.left = None # 왼쪽 자식 노드 초기화
        self.right = None # 오른쪽 자식 노드 초기화

class BinarySearchTree:
    # BST 생성
    def __init__(self):
        self.root = None
    
    # 삽입
    def insert(self, key):
        self.root = self.insert_recursive(self.root, key)
    
    # 삽입 함수
    def insert_recursive(self, node, key):
        # BST에 노드가 없다면 루트에 노드 생성
        if node is None:
            return Node(key)
        
        # 삽입 key가 노드의 key보다 작다면 왼쪽 자식 노드에 노드 생성
        if key < node.key:
            node.left = self.insert_recursive(node.left, key)
        else: # 삽입 key가 노드의 key보다 크다면 오른쪽 자식에 노드 생성
            node.right = self.insert_recursive(node.right, key)
        
        return node
    
    # 검색
    def search(self, key):
        path = "R" # 경로 맨 처음에 루트 R 고정
        return self.search_recursive(self.root, key, path)
    
    # 검색 함수
    def search_recursive(self, node, key, path):
        # 노드에 key가 없다면 None 리턴
        if node is None:
            return None
        
        # 검색 key가 루트에 있다면 R 리턴
        if node.key == key:
            return path
        
        # 검색 key가 노드의 key보다 작다면 왼쪽 자식 노드로 이동 후, 경로에 0 추가
        if key < node.key:
            return self.search_recursive(node.left, key, path + "0")
        else: # 검색하는 key가 노드의 key보다 크다면 오른쪽 자식 노드로 이동 후, 경로에 1 추가
            return self.search_recursive(node.right, key, path + "1")
    
    # 삭제
    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)
    
    # 삭제 함수
    def delete_recursive(self, node, key):
        # 노드에 key가 없다면 None 리턴
        if node is None:
            return None
        
        # 삭제 key가 노드의 key보다 작다면 왼쪽 자식 노드로 이동
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)
        elif key > node.key: # 삭제 key가 노드의 key보다 크다면 오른쪽 자식 노드로 이동
            node.right = self.delete_recursive(node.right, key)
        else:
            # 삭제 key가 노드의 key와 일치하면 삭제
            # 노드의 자식이 한 개인 경우
            if node.left is None: # 오른쪽 자식이 남아있다면 오른쪽 자식으로 대체
                return node.right
            elif node.right is None: # 왼쪽 자식이 남아있다면 왼쪽 자식으로 대체
                return node.left
            
            # 노드의 자식이 두 개인 경우
            min_node = self.find_min(node.right) # 오른쪽 서브트리의 최소값인 노드를 찾아서
            node.key = min_node.key # 최소값인 노드로 대체한 후
            node.right = self.delete_recursive(node.right, min_node.key) # 대체한 최소값 노드는 삭제
        
        return node
    
    # 오른쪽 서브트리의 최소값 찾는 함수
    def find_min(self, node):
        current_root = node # 서브트리의 루트
        # 루트에서 왼쪽 자식노드로 계속 이동
        # 마지막 노드의 key 값을 최소값으로 리턴
        while current_root.left is not None:
            current_root = current_root.left
        return current_root


# BST 테스트 케이스 실행 함수
def bst_test_case(input_lines):
    # BST 생성
    bst = BinarySearchTree()
    
    # 키 삽입
    insert_count = int(input_lines[0]) # 삽입 key 개수
    insert_keys = list(map(int, input_lines[1].split())) # 삽입 key 리스트
    # 리스트 순서대로 key 삽입
    for key in insert_keys:
        bst.insert(key)
    
    # 첫 번째 검색
    search1_count = int(input_lines[2]) # 검색 key 개수
    search1_keys = list(map(int, input_lines[3].split())) # 검색 key 리스트
    search1_results = [] # 검색한 key의 경로 저장 리스트
    # 리스트 순서대로 key를 검색 후, 경로 저장
    for key in search1_keys:
        path = bst.search(key)
        search1_results.append(path)
    
    # 키 삭제
    delete_count = int(input_lines[4]) # 삭제 key 개수
    delete_keys = list(map(int, input_lines[5].split())) # 삭제 key 리스트
    # 리스트 순서대로 key 삭제
    for key in delete_keys:
        bst.delete(key)
    
    # 두 번째 검색
    search2_count = int(input_lines[6]) # 검색 key 개수
    search2_keys = list(map(int, input_lines[7].split())) # 검색 key 리스트
    search2_results = [] # 검색한 key의 경로 저장 리스트
    # 리스트 순서대로 key를 검색 후, 경로 저장
    for key in search2_keys:
        path = bst.search(key)
        search2_results.append(path)
    
    # (첫 번째 검색 결과의 경로 + 두 번째 검색 결과의 경로) 리턴
    return search1_results + search2_results


# 파일 읽기
with open('bst_input.txt', 'r') as f:
        test_case_count = int(f.readline().strip()) # 테스트 케이스 개수
        
        output_results = [] # 테스트 케이스의 검색 결과 저장 리스트
        # 테스트 케이스 순서대로
        for _ in range(test_case_count):
            input_lines = [f.readline().strip() for _ in range(8)] # [삽입, 첫 번째 검색, 삭제, 두 번째 검색] 순으로 분리
            test_case_results = bst_test_case(input_lines) # 테스트 케이스 실행 후
            output_results.extend(test_case_results) # 검색 결과 리스트 저장
    
# 파일 쓰기
with open('bst_output.txt', 'w') as out:
    for result in output_results:
        out.write(result + '\n')