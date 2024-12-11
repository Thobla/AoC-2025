

def main():
    inp = input()
    arr = []
    id = 0

    for i in range(len(inp)):
            if i % 2:
                for _ in range(int(inp[i])):
                    arr.append(-1)
            else:
                for _ in range(int(inp[i])):
                    arr.append(id)
                id += 1

    pointer_1 = 0
    pointer_2 = len(arr)-1
    print(arr)
    while(True):
        while(arr[pointer_1] != -1):
            pointer_1 += 1
            if pointer_1 >= pointer_2:
                break
        while(arr[pointer_2] == -1):
            pointer_2 -= 1
            if pointer_1 >= pointer_2:
                break
        if pointer_1 >= pointer_2:
            break
        arr[pointer_1] = arr[pointer_2]
        arr[pointer_2] = -1
    sum = 0
    pointer_1 = 0
    print(arr)
    while(arr[pointer_1] != -1):
        sum += pointer_1 * arr[pointer_1]
        pointer_1 += 1
    print(sum)


main()
