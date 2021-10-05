list = [int(x) for x in input("숫자를 공백으로 구분하여 입력해주세요 : ").split()]
list_length = len(list)
sort_list = sorted(list)
sum = 0

negative = []

for i in range(list_length - 1, -1, -1): # 가장 큰 수부터 묶으려면 내림차순으로 for문을 돌린다.
    if list_length % 2 == 0: # N(list_length)가 짝수일 때
        if sort_list[i] <= 0:
            negative.append(sort_list[i])
        elif sort_list[i-1] <= 0:
            sum += sort_list[i]
        elif i % 2 == 1:
            sum += sort_list[i]*sort_list[i-1]

    elif list_length % 2 == 1: # N(list_length)가 홀수일 때
        if sort_list[i] <= 0:
            negative.append(sort_list[i])
        elif sort_list[i-1] <= 0:
            sum += sort_list[i]
        elif i % 2 == 0:
            sum += sort_list[i] * sort_list[i - 1]

len_negative = len(negative)
for i in range(len_negative - 1, -1, -1):
    if len_negative % 2 == 0:
        if i % 2 == 1:
            sum += negative[i]*negative[i-1]
    else:
        if i == 0:
            sum += negative[0]
        elif i % 2 == 0:
            sum += negative[i]*negative[i-1]

print(sum)

# 1 : 음수의 절대값
# 음수 * 음수 = 양수이므로 절대값이 큰 음수끼리 곱하면 합이 최대가 된다. 따라서 음수만 따로 추출하여 합이 최대가 되는 경우를 구한다.

# 2 : index 값
# 최대의 합을 도출하기 위해서는 절대값이 큰수끼리 묶어야 한다. 따라서 sort_list에서 가장 큰  index 값부터 왼쪽으로 묶어가야 한다.
# 그러나 하나의 원소는 묶이지 않거나 한번만 묶일 수 있다. 따라서 원소가 홀수개이면 짝수 index를 가지는 원소를 중심으로 묶고, 원소가 짝수개이면 홀수를 중심으로 묶는다.

# 3 : 양수 혹은 음수 중 절대값이 가장 작은 수
# 양수 혹은 음수에서 절대값이 가장 작은 수는 묶이지 않을 수 있다. 묶이지 않는 경우, 그대로 sum에 더한다.
# 음수 중 가장 작은 절대값을 가지는 수는 0의 index를 갖는다. (음수 리스트 negative : 내림차순으로 정렬)