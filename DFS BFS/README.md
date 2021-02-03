## DFS/BFS 그래프 탐색을 위한 대표적인 두 가지 알고리즘
- 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

### 스택
- 스택은 박스 쌓기에 비유할 수 있다. 흔히 박스는 아래에서부터 위로 차곡차곡 쌓는다. 아래에 있는 박스를 치우기 위해서는 위에 있는 박스를 먼저 내려야 한다.
- 이러한 구조를 선입후출 구조 또는 후입선출 구조라고 한다.(FILO)
- stack = []
- stack.append() , stack.pop() , stack[::-1]

### 큐
- 큐는 대기 줄에 비유할 수 있다.
- from collections import deque
- queue = deque()
- queue.append() , queue.popleft() , queue.reverse() 
- list 반환 : list(queue)

### 재귀함수
- 재귀함수란 자기자신을 다시 호출하는 함수
- 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.
- 마지막 호출된 함수가 끝나면 이전 함수들도 순차적으로 종료된다.
- 코드가 간결해지고 수학의 점화식의 형태를 나타낸다.
- factorial(n) = n * factorial(n-1)