

def main():
    inp = input()
    arr = []
    id = 0

    empty = [int(x) for x in [inp[y] for y in range(1, len(inp), 2)]]
    data = [int(x) for x in [inp[y] for y in range(0, len(inp), 2)]]
    fill_indecies = [[] for _ in range(len(empty))]
    if len(data) > len(empty):
        empty.append(0)
    print("empty: ", empty)
    print("data: ", data)
    print("id: ", id)


    for x in range(len(data)-1, 0, -1):
        size = data[x]
        for y in range(x):
            if empty[y] >= size:
                empty[y] -= size
                empty[x-1] = empty[x-1] + size
                fill_indecies[y].append(x)
                break

    new_data = []
    visited = set()
    print("empty: ", empty)
    print("data: ", data)
    for i in range(len(inp)):
        if i % 2:
            for x in fill_indecies[int((i - 1)/2)]:
                new_data.extend([x for _ in range(data[x])])
                visited.add(x)
            new_data.extend([-1 for _ in range(empty[int((i - 1)/2)])])

        else:
            if int(i/2) not in visited:
                new_data.extend([int(i/2) for _ in range(data[int(i/2)])])

    print(new_data)
    pointer_1 = 0
    pointer_2 = len(new_data)-1

    while(False):
        while(new_data[pointer_1] != -1):
            pointer_1 += 1
            if pointer_1 >= pointer_2:
                break
        while(new_data[pointer_2] == -1):
            pointer_2 -= 1
            if pointer_1 >= pointer_2:
                break
        if pointer_1 >= pointer_2:
            break
        new_data[pointer_1] = new_data[pointer_2]
        new_data[pointer_2] = -1
    sum = 0
    pointer_1 = 0
    print(new_data)
    for x in range(len(new_data)):
        if new_data[x] != -1: 
            print(new_data[x])
            sum += x * new_data[x]
    print(sum)


main()
