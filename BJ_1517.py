def merge_sort(start, end):
    global swap
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if N[a] <= N[b]:
                temp.append(N[a])
                a += 1
            else:
                temp.append(N[b])
                b += 1
                swap += (mid - a + 1)
        if a <= mid:
            temp = temp + N[a:mid + 1]

        if b <= end:
            temp = temp + N[b:end + 1]
        for i in range(len(temp)):
            N[start+i] = temp[i]

swap = 0
N = [int(x) for x in input("숫자를 공백으로 구분하여 입력해주세요 : ").split()]
merge_sort(0, len(N) - 1)
print(swap)
