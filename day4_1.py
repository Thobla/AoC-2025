inp_len = 140
#inp_len = 10
grid = []
for _ in range(inp_len):
    grid.append(input())

dp = [0 for i in range(inp_len**2)]
print(grid)
for i in range(inp_len**2):
    sum = 0
    x = i%inp_len
    y = i//inp_len
    print("x: ", x,  "y: ", y, "i: ", i)
    if (x >= 3):
        if (y >= 3):
            if (grid[y][x] + grid[y - 1][x - 1] + grid[y - 2][x - 2] + grid[y - 3][x - 3] == "XMAS"):
                sum += 1
        if (y <= inp_len - 4):
            if (grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3] == "XMAS"):
                sum += 1
        if (grid[y][x] + grid[y][x-1] + grid[y][x-2] + grid[y][x-3] == "XMAS"):
            sum += 1
    if (x <= inp_len - 4):
        if (y >= 3):
            #print(i, x, y)
            if (grid[y][x] + grid[y - 1][x + 1] + grid[y - 2][x + 2] + grid[y - 3][x + 3] == "XMAS"):
                sum += 1
        if (y <= inp_len - 4):
            if (grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3] == "XMAS"):
                sum += 1
        if (grid[y][x] + grid[y][x+1] + grid[y][x+2] + grid[y][x+3] == "XMAS"):
            sum += 1
    if (y >= 3):
        if (grid[y][x] + grid[y-1][x] + grid[y-2][x] + grid[y-3][x] == "XMAS"):
            sum += 1
    if(y <= inp_len - 4):
        if (grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+3][x] == "XMAS"):
            sum += 1
    dp[i] = dp[max(0, i-1)] + sum
    #print(dp[i])

#print(dp)
print(dp[-1])
