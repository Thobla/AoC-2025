def define_garden(x, y, width, height, garden, plant, grid):
    grid[y][x] = '.'
    for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if x + dir[0] >= 0 and y + dir[1] >= 0 and x + dir[0] < width and y + dir[1] < height:
            if grid[y + dir[1]][x + dir[0]] == plant and grid[y + dir[1]][x + dir[0]] != '.':
                grid[y + dir[1]][x + dir[0]] = '.'
                garden.append((x + dir[0], y + dir[1]))
                define_garden(x + dir[0], y + dir[1], width, height, garden, plant, grid)

def compute_cost(garden, plant, width, height, grid):
    perimiter = 0
    print("plant: ", plant)
    for pos in garden:
        for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = pos[0]
            y = pos[1]
            if x + dir[0] < 0 or y + dir[1] < 0 or x + dir[0] >= width or y + dir[1] >= height:
                print("1, X: ", x + dir[0], ", Y: ", y+dir[1])
                perimiter += 1
            elif grid[y + dir[1]][x + dir[0]] != plant:
                print("2, X: ", x + dir[0], ", Y: ", y+dir[1])
                perimiter += 1
    area = len(garden)
    print("perimiter: ", perimiter)
    print("area: ", area)
    return perimiter * area



def main():
    width = 140
    height = 140
    inp_length = width*height
    grid = []
    original_grid = []
    for i in range(height):
        inp = list(input())
        grid.append(inp)
        original_grid.append(inp.copy())

    gardens = []
    garden_plants = []
    for i in range(inp_length):
        x = i % width
        y = i//width
        plant = grid[y][x]
        if grid[y][x] != '.':
            garden = []
            garden.append((x, y))
            grid[y][x] = '.'
            define_garden(x, y, width, height, garden, plant, grid)
            garden_plants.append(plant)
            gardens.append(garden)

    sum = 0
    for i in range(len(gardens)):
        sum += compute_cost(gardens[i], garden_plants[i], width, height, original_grid)

    print(sum)

main()
