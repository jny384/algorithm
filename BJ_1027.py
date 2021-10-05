N = int(input())
buildings = list(map(int, input().split(' ')))
max_visible = 0

for i in range(N):
    visible = 0
    num = -99999999999
    for j in range(i+1, N):
        y = (buildings[j] - buildings[i]) / (j - i)
        if y > num:
            visible += 1
            num = y
    num = 99999999999
    for j in range(i-1, -1, -1):
        y = (buildings[j] - buildings[i]) / (j - i)
        if y < num:
            visible += 1
            num = y
    if visible > max_visible:
        max_visible = visible
print(max_visible)