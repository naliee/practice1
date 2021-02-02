from random import *

user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# users = range(1, 21) : 1부터 20까지 숫자 생성
# users = list(users): 위의 range는 list가 아니기 때문에 타입 변경

# 무작위로 추첨 하되, 중복 불가 - 4명 뽑아서 한 명은 치킨
shuffle(user)
winners = sample(user, 4)

'''chicken = str(sample(user, 1))
print(chicken)

user2 = set(user)
user2 = user2.remove(chicken)
coffee = sample(user2, 3)'''

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]) )
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))   #          500
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))  #         +500
print("{0: >+10}".format(-500)) #         -500
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) #         -500
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(100000000000))     # 100,000,000,000
# 3자리마다 콤마를 찍어주기, +- 부호도 붙이기 
print("{0:+,}".format(100000000000))    # +100,000,000,000
# 3자리마다 콤마를 찍어주기, 부호, 자릿수 확보하기, 빈 자리 ^로 채우기
print("{0:^<+30,}".format(100000000000)) # +100,000,000,000^^^^^^^^^^^^^^
# 소수점 출력
print("{0:f}".format(5/3))  # 1.666667
# 소수점 특정 자리수까지만 표시 (소수점 3째 자리에서 반올림하여 2자리까지만)
print("{0:f}".format(5/3))  # 1.67

for i in range(1, 51):
     with open("{0}주차.txt".format(str(i)), "w", encoding="utf8") as report:
         report.write("- {0} 주차 주간보고 -\n부서 : \n이름 : \n업무 요약 : ".format(str(i)))


chicken = 10
waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

class SoldOutError(Exception):
    def __init__(self):
        pass

while(True):
    try:
        if chicken <= 0:
            raise SoldOutError

        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
    
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    except ValueError:
        print("잘못된 값을 입력하였습니다.")

