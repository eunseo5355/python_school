"""
가위바위보를 사용자가 이길 때까지 반복한다.

입력예)
1: 가위 2: 바위 3: 보

입력예 1)
1
출력예 1)
졌습니다!
다시 시도하세요.

입력예 2)
1
출력예 2)
비겼습니다!
다시 시도하세요.

입력예 3)
2
출력예 3)
이겼습니다!
축하합니다.
"""
import random
# random 정수를 발생시키기 위해 포함

while True:  # 무한반복
    m = random.randint(1, 3)  # 1과 3 사이의 난수를 발생시킴
    print("1: 가위 2: 바위 3: 보")  # 입력 안내문
    y = int(input("입력:"))  # 입력 받기
    print("생성된 값: %d" % m)
    if m == 1:  # 내가 가위라면
        if y == 2:  # 입력이 바위인 경우 성공
            print("이겼습니다!\n축하합니다.")
            break
    elif m == 2:  # 내가 바위라면
        if y == 3:  # 입력이 보인 경우 성공
            print("이겼습니다!\n축하합니다.")
            break
    elif m == 3:  # 내가 보라면
        if y == 1:  # 가위가 입력되면 성공
            print("이겼습니다!\n축하합니다.")
            break
    elif m == y:
        print("비겼습니다!\n다시 시도하세요.")
    else:  # 이기지도 비기지도 않으면 진 경우
        print("졌습니다!\n다시 시도하세요.")