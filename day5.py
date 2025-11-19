
# 환경설정
# python 파일 하나 (.py)

# 가상환경
## venv venv(가상환경 이름)
## 활성화: source/venv/bin/activate or venv/scripts/activate
## 비활성화: deactivate

# 자료형
# 숫자형: 정수(int), 실수(float)
# 문자형: 문자열(str)
# 논리형: 불리언(bool)
# None

# 변수
# 값을 저장하는(가리키는) 상자 -> 값을 재사용, 어떤 곳에서 가져다 쓰기 위해서
a = 10

# 출력하는 방법
print()
# 입력하는 방법
input() # input으로 받은 값은 문자열, 숫자로 쓰고 싶으면 형 변환(int(), float())


# 자료 구조
# 리스트
# [a, b, c]
# 성격이 비슷한 여러 값들을 한 번에 저장하기 위해
# 순서가 있고 수정 가능

# 튜플
# (123.65, 1231.53)
# 바뀌면 안 되는 값을 보호하기 위해
# 순서가 있고 수정이 불가능

# 딕셔너리
# { key: value }
# 각 값에 대한 정체성 부여(설명)하기 위해
# 순서 없고 수정 가능

# 셋
# set()
# 중복을 허용하지 않는다


# 기본 연산자
# +, -, *, /
# //, %, **
# ==, !=

# 연산자 연결
## 조건 연결 -> n % 2 == 0
## 논리 연산자 and, or, not
# and
# 첫 번째 조건(n % 2 == 0) and 두 번째 조건(n % 4 == 0)
# 참 and 참 -> 참
# 참 and 거짓 -> 거짓
# 거짓 and 거짓 -> 거짓

# or
# 첫 번째 조건(n % 2 == 0) or 두 번째 조건(n % 4 == 0)
# 참 or 참 -> 참
# 참 or 거짓 -> 참
# 거짓 or 거짓 -> 거짓

# not
# not 조건(n % 2 == 0)


# 조건문, 반복분

# if
# if 조건문1:
#   실행문1
# elif 조건문2:
#   실행문2
# elif 조건문3:
#   실행문3
# else:
#   실행문

# "조건문 어떻게 만들 것인가"
# "조건마다 어떻게 분기할 것인가"

# 반복분
# for, while

# for
# for 변수 in 순회할 곳:
# 순회할 것이 정해져있다. 범위, 횟수 정해져 있음

# for 변수 in range(범위):
# 범위, 횟수를 직접 지정

# while
# while 조건:
# 조건이 참일 동안 반복 -> 조건이 거짓이 되는 순간 멈춤
# 횟수 < "조건"


# break
# break를 만나면 반복문이 끝남

# continue
# continue를 만나면 일단 끝내고 반복문은 끝나지 않음

# while True:
#   if 조건:
#       break


# 함수
# def 함수 이름(매개변수):
# 자주 쓰는 코드를 한 번 만 정의하여 꺼내쓰는 용도
# 선언부, 호출부 -> 함수이름(인자)

# 함수 실행 결과 사용: return
# 변수 = 함수이름(인자)

# 매개변수
# 가변 매개변수: 매개변수 갯수를 정해놓지 않고 사용하고 싶을때
# def 함수이름(args):
#   print(args) -> () 하나의 튜플 형태로 받는다
# 함수이름(1, 2, 3, 4, .....)


# 키워드 가변 매개변수: 유연하게 입력 처리
# def 함수이름(**kwargs): 
#   print(kwargs) -> 키 값이(딕셔너리) 있는 형태로 받는다
# 함수이름(name = "", age = "", nickname = "")



## continue 사용 버전
import random

def guess_game():
    answer = random.randint(1, 10)
    while True:
        guess = int(input('숫자를 입력하시오: '))
        if guess != answer:
            print('틀력습니다.')
            continue
        print('맞았습니다')
        break

guess_game()