import sys
input = sys.stdin.readline

list = int(input())
positive = []
negative = []
one = 0

for _ in range(list) : # 0과 음수, 1, 양수 나누기
    l = int(input())
    if l > 1 :
        positive.append(l)
    elif l == 1 : #1은 곱하지 않고 sum에 그대로 더 함
        one += 1
    else:
        negative.append(l)

def match_number(L) : # 양수 음수 리스트 더해주는 과정이 같아서 함수로 묶음
    sum = 0
    if len(L) % 2 == 0: # 원소가 짝수개일 경우 두개씩 곱함
        for i in range(0, len(L), 2):
            sum += L[i] * L[i+1]
    else: # 원소가 홀수개일 경우 두개씩 곱하고
        for i in range(0, len(L)-1, 2):
            sum += L[i] * L[i+1]
        sum += L[len(L)-1] # 마지막 수는 더해줌
    return sum



# 절대값이 큰 수부터 오게 정렬
positive.sort(reverse=True) # 양수는 내림차순
negative.sort()
max_sum = match_number(positive) + match_number(negative) + one
print(max_sum)