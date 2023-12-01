from aocd import submit, get_data
import numpy as np
from sys import argv
import re
from collections import defaultdict

assert len(argv) == 2, "args: [a, b, A, B]"
assert argv[1] in ["a", "b", "A", "B"]

CMD = argv[1]

lines = get_data(day=1, year=2023).splitlines()

if CMD == "a" or CMD == "b":
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]

if lines[-1] == "":
    lines = lines[:-1]

def part_A():
    return sum([int(f[0] + f[-1]) for f in [re.findall(r"\d", l) for l in lines]])

def part_B():
    m = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    M = {**{k: i for i, k in enumerate(m, 1)}, **{str(i): i for i in range(1, 10)}}
    return sum([int(M[f[0]] * 10 + M[f[-1]]) for f in [re.findall(f"(?=(\d|{'|'.join(m)}))", l) for l in lines]])


# ---------------------------------------------------------------------------


ans = part_A() if (CMD == "A" or CMD == "a") else part_B()
print("ANSWER:", ans)
if CMD != "a" and CMD != "b" and ans != 0:
    submit(ans)
