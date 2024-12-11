import math


# replace 0 by 1
def rule_1(old_dct, new_dct, old_keys, new_keys):
    if 0 in old_keys:
        new_dct[1] = old_dct[0]
        new_keys.add(1)


def rule_2(old_dct, new_dct, number, old_keys, new_keys):
    if number == 0:
        return
    dividor = math.floor(math.log10(number)) + 1
    if ((dividor % 2) == 0 and (dividor > 1)):
        stone_1 = int(number % int(10**(dividor/2)))
        stone_2 = int(math.floor(number/(10**(dividor/2))))
        if stone_1 in new_keys:
            new_dct[stone_1] += old_dct[number]
        else:
            new_dct[stone_1] = old_dct[number]
            new_keys.add(stone_1)
        if stone_2 in new_keys:
            new_dct[stone_2] += old_dct[number]
        else:
            new_dct[stone_2] = old_dct[number]
            new_keys.add(stone_2)

    else:
        if number*2024 in new_keys:
            new_dct[number*2024] += old_dct[number]
        else:
            new_dct[number*2024] = old_dct[number]
            new_keys.add(number*2024)



def main():
    inp = [int(x) for x in input().split()]
    new_dct = {}
    old_dct = {}
    old_keys = set(inp)
    new_keys = set()
    for x in inp:
        old_dct[x] = 0
    for x in inp:
        old_dct[x] += 1

    for i in range(75):
        rule_1(old_dct, new_dct, old_keys, new_keys)
        for number in old_keys:
            rule_2(old_dct, new_dct, number, old_keys, new_keys)
        old_dct = new_dct
        new_dct = {}
        old_keys = new_keys
        new_keys = set()

    sum = 0
    for x in old_keys:
        sum += old_dct[x]
    print(sum)
main()
