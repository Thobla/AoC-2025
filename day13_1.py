

import re
import numpy as np
import math


sum = 0
for i in range(int(1280/4)):
    inp = re.split(',| |\+', input())
    A = (int(inp[3]), int(inp[6]))
    inp = re.split(',| |\+', input())
    B = (int(inp[3]), int(inp[6]))
    inp = re.split(',| |\=', input())
    C = (int(inp[2]), int(inp[5]))

    dp = [[False for _ in range(101)] for _ in range(101)]
    for i in range(101):
        for j in range(101):
            if A[0]*i + B[0]*j == C[0] and A[1]*i + B[1]*j == C[1]:
                dp[j][i] = True
    sum_partial = math.inf
    valid = False
    for i in range(101):
        for j in range(101):
            if dp[j][i]:
                valid = True
                sum_partial = min(sum_partial, 3*i + j)
    if valid:
        sum += sum_partial
    input()

print(sum)
