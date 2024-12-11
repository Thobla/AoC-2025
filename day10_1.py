paths = set()
def find_paths(x, y, itt, grid):
    global paths
    sum = 0
    if itt == 9:
        if grid[x][y] == 9 and (x, y) not in paths:
            paths.add((x, y))
            return 1
        else:
            return 0
    if (x, y) not in paths:
        if grid[x][y] == itt:
            paths.add((x, y))
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if x + dir[0] < 60 and y + dir[1] < 60 and x + dir[0] >= 0 and y + dir[1] >= 0:
                    sum += find_paths(x + dir[0], y + dir[1], itt+1, grid)
    return sum


def main():
    global paths
    grid = [[0 for _ in range(60)]for _ in range(60)]
    for i in range(60):
        inp = input()
        for j in range(len(inp)):
            grid[i][int(j)] = int(inp[j])

    sum = 0
    for i in range(3600):
        x = i % 60
        y = i//60
        #print(x, y)
        paths = set()
        sum += find_paths(x, y, 0, grid)
        #print(biggest)

    print(sum)
main()
