width = 50
height = 50
grid = []
for i in range(height):
    grid.append(input())
anti_grid = [['.' for _ in range(width)] for _ in range(height)]
sum = 0


char_positions = {}
for x in range(width):
    for y in range(height):
        if grid[y][x] != '.':
            if grid[y][x] not in char_positions.keys():
                char_positions[grid[y][x]] = []
            char_positions[grid[y][x]].append((x, y))


for elem in char_positions.keys():
    positions = char_positions[elem]
    for pos_1 in positions:
        for pos_2 in positions:
            if pos_1 == pos_2:
                continue
            x_diff = pos_1[0] - pos_2[0]
            y_diff = pos_1[1] - pos_2[1]
            print("pos_1: ", pos_1, "pos_2: ", pos_2, "x_diff: ", x_diff, "y_diff: ", y_diff)
            if pos_1[1] + y_diff >= 0 and pos_1[0] + x_diff >= 0 and pos_1[1] + y_diff < height and pos_1[0] + x_diff < width:
                if anti_grid[pos_1[1] + y_diff][pos_1[0] + x_diff] != '#':
                    anti_grid[pos_1[1] + y_diff][pos_1[0] + x_diff] = '#'
                    sum += 1

for i in range(height):
    print(anti_grid[i])
print(sum)


