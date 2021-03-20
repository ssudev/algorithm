## 자물쇠와 열쇠
<div>
    <img src="image1.PNG" width="400" height="500">
</div>
<div>
    <img src="image2.PNG" width="400" height="320">
</div>

### 문제 해설
- 포인트는 LOCK 배열을 3배로 만들어서 KEY를 맞추기 쉽게 만든다.
- 2차원 배열 오른쪽으로 돌리기 : new_map[j][n-i-1] = map[i][j]