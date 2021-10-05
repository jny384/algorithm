import sys

def mergeSort(start, end):
    global swap
    if start < end:
        mid = (start + end) // 2
        mergeSort(start, mid)
        mergeSort(mid + 1, end)

        a = start
        b = mid + 1
        tmp = []
        while a <= mid and b <= end:
            if arr[a] <= arr[b]:
                tmp.append(arr[a])
                a += 1

            else:
                tmp.append(arr[b])
                b += 1
                swap += (mid - a + 1)  # 스와핑 했을 때 개수추가
        if a <= mid:
            tmp = tmp + arr[a:mid+1]
        if b <= end:
            tmp = tmp + arr[b:end+1]

        for i in range(len(tmp)):
            arr[start + i] = tmp[i]

if __name__ == '__main__':
    swap = 0
    N = int(input())
    arr = list(map(int, input().split()))
    mergeSort(0, N - 1)
    print(swap)