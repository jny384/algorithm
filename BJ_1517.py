list = [int(x) for x in input("숫자를 공백으로 구분하여 입력해주세요 : ").split()]
list_length = len(list)
swap = 0

for i in range(list_length - 1) :
    for j in range(list_length - 1 - i) :
        if list[j] > list[j + 1] :
            list[j], list[j + 1] = list[j + 1], list[j]
            swap += 1
print(list)
print(swap)
