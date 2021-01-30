n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # // 연산자는 몫을 넘지 않는 최대 정수
    count += n // coin
    n %= coin