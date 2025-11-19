#리스트 평균 구하기
def list_avg(nums):
    return sum(nums)/len(nums)
print(list_avg([80, 90, 60, 100]))

#구구단 출력 함수
def gugudan(n):
    for i in range(1, 10):
        print(f"{n} X {i} = {n*i}")
gugudan(5)

# BMI 계산기
def bmi(w, h):
    return round(w/(h**2),2)
print(bmi(100,2))

#여러 숫자의 평균 구하기
def avg(*nums):
    return sum(nums)/len(nums)
print(avg(10, 20, 30, 40, 50))
