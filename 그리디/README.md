## 접두사 합
- O(N+M)의 시간복잡도
- 알고리즘 로직
    1. N개의 수에 대하여 접두사 합(Prefix Sum)을 계산하여 배열 P에 저장한다.
    2. 매 M개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R]-P[L-1]이다.
    
<img src="image1.PNG" width="500" height="300">