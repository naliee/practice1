import math
import os
import random
import re
import sys

def raw_input(self):
    return random.randint(1, 100)


def alg(self, n):
    if (n % 2 > 0) or (n % 2 == 0 and 6 <= n <= 20):
        print("weird")
    elif (n % 2 == 0 and 2 <= n <= 5) or (n % 2 == 0 and n > 20):
        print("Not weird")


if __name__ == '__main__':
    n = int(raw_input().strip())
    alg(n)