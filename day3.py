import math
import sys

sys.setrecursionlimit(10000000)

sum = 0


def search_1(word, p1):
    if (len(word) - p1 < 4):
        return False
    return word[p1:(p1+4)] == "mul(" #)


def search_2(word, start_idx):
    p=start_idx
    while True:
        if (word[p].isdigit()):
            p+=1
        else:
            return p

def search_3(word, start_idx, mults, sum):
    if word[start_idx] == ",":
        p = search_2(word, start_idx+1)
        if p == start_idx+1:
            return start_idx + 1, sum
        else:
            mults.append(int(word[start_idx+1:p]))
            return search_3(word, p, mults, sum)
    elif word[start_idx] == ")":
        return start_idx+1, sum + math.prod(mults)
    else:
        return start_idx, sum


def search_4(word, start_idx):
    if(word[start_idx:start_idx+4] == "do()"):
        return True


def search_5(word, start_idx):
    if(word[start_idx:start_idx+7]=="don't()"):
        return True


def search(word, p1, p2, sum, valid):
    if p1 == len(word):
        return sum, valid
    if valid:
        temp_sum = sum
        if (search_1(word, p1)):
            p2 = p1 + 4
        else:
            if search_5(word, p1):
                return search(word, p1+7, p1+7, sum, False)
            else:
                return search(word, p1+1, p1+1, sum, True)
        temp_p = search_2(word, p2)
        if (temp_p == p2):
            return search(word, p2, p2, sum, valid)
        else:
            p2, temp_sum = search_3(word, temp_p, [int(word[p2:temp_p])], sum)
        return search(word, p2, p2, temp_sum, True)
    else:
        if search_4(word, p1):
            return search(word, p1+4, p1+4, sum, True)
        else:
            return search(word, p1+1, p1+1, sum, False)


def test(i, word):
    if i == len(word):
        return "finished"
    else:
        return test(i+1, word)


word = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print("test: ", search(word, 0, 0, 0, True))

sum = 0
valid = True
for _ in range(6):
    inp = input()
    print(test(0, inp))
    sum, valid = search(inp, 0, 0, sum, valid)
print(sum)
