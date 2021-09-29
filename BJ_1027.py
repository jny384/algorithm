N = int(input())
buildings = list(map(int, input().split()))
max_visible = 0

visible = 0
final_visible = []

for i in range(N):
    visible = 0
    # left side
    max_left = 999999999
    for j in range(i - 1, -1, -1):
        y = (buildings[i] - buildings[j]) / ((i + 1) - (j + 1))
        if y < max_left:
            visible += 1
            max_left = y

    # right side
    min_right = -999999999
    for j in range(i + 1, N):
        y = (buildings[i] - buildings[j]) / (i - j)
        if y > min_right:
            visible += 1
            min_right = y
    final_visible.append(visible)
print(max(final_visible))
