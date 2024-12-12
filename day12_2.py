def define_garden(x, y, width, height, garden, plant, grid):
    grid[y][x] = '.'
    for dir in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        if x + dir[0] >= 0 and y + dir[1] >= 0 and x + dir[0] < width and y + dir[1] < height:
            if grid[y + dir[1]][x + dir[0]] == plant and grid[y + dir[1]][x + dir[0]] != '.':
                grid[y + dir[1]][x + dir[0]] = '.'
                garden.append((x + dir[0], y + dir[1]))
                define_garden(x + dir[0], y + dir[1], width, height, garden, plant, grid)


def update_neighbours(gfa, x, y, dir, garden):
    if dir[0] == 0:
        if dir[1] == 1:
            if gfa[garden.index((x, y))][2]:
                gfa[garden.index((x, y))][2] = False
                if (x + 1, y) in garden:
                    update_neighbours(gfa, x + 1, y, dir, garden)
                if (x - 1, y) in garden:
                    update_neighbours(gfa, x - 1, y, dir, garden)
        if dir[1] == -1:
            if gfa[garden.index((x, y))][3]:
                gfa[garden.index((x, y))][3] = False
                if (x + 1, y) in garden:
                    update_neighbours(gfa, x + 1, y, dir, garden)
                if (x - 1, y) in garden:
                    update_neighbours(gfa, x - 1, y, dir, garden)

    elif dir[1] == 0:
        if dir[0] == 1:
            if gfa[garden.index((x, y))][0]:
                gfa[garden.index((x, y))][0] = False
                if (x, y + 1) in garden:
                    update_neighbours(gfa, x, y + 1, dir, garden)
                if (x, y - 1) in garden:
                    update_neighbours(gfa, x, y - 1, dir, garden)
        if dir[0] == -1:
            if gfa[garden.index((x, y))][1]:
                gfa[garden.index((x, y))][1] = False
                if (x, y + 1) in garden:
                    update_neighbours(gfa, x, y + 1, dir, garden)
                if (x, y - 1) in garden:
                    update_neighbours(gfa, x, y - 1, dir, garden)



def compute_cost(garden, plant, width, height, grid):
    perimiter = 0
    print("plant: ", plant)
    garden_face_angles = compute_face_angles(garden, plant, width, height, grid)
    for i in range(len(garden)):
        pos = garden[i]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for j in range(len(directions)):
            dir = directions[j]
            x = pos[0]
            y = pos[1]
            if garden_face_angles[i][j]:
                perimiter += 1
                update_neighbours(garden_face_angles, x, y, dir, garden)
    area = len(garden)
    print("perimiter: ", perimiter)
    print("area: ", area)
    return perimiter * area


def compute_face_angles(garden, plant, width, height, grid):
    garden_pos_angles = []
    for pos in garden:
        pos_angles = [False, False, False, False]
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(len(directions)):
            dir = directions[i]
            x = pos[0]
            y = pos[1]
            if x + dir[0] < 0 or y + dir[1] < 0 or x + dir[0] >= width or y + dir[1] >= height:
                pos_angles[i] = True
            elif grid[y + dir[1]][x + dir[0]] != plant:
                pos_angles[i] = True
        garden_pos_angles.append(pos_angles)
    return garden_pos_angles




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
        garden_face_angles = compute_face_angles(garden, plant, width, height, original_grid)
        sum += compute_cost(gardens[i], garden_plants[i], width, height, original_grid)

    print(sum)

main()
