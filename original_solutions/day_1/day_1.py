from aocd import submit, get_data
import numpy as np
from sys import argv
import re
from collections import defaultdict

assert len(argv) == 2, "args: [a, b, A, B]"
assert argv[1] in ['a', 'b', 'A', 'B']

CMD = argv[1]

lines = get_data(day=1,year=2023).splitlines()

if CMD == "a" or CMD == "b":
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]

if lines[-1] == "":
    lines = lines[:-1]

def part_A():
    S = 0
    for l in lines:
        f = re.findall(r"\d", l)
        s = f[0] + f[-1]
        S += int(s)
    return S

def part_B():
    m = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }
    S = 0
    for l in lines:
        f = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l)
        S += int(m[f[0]] + m[f[-1]])
    return S


# ---------------------------------------------------------------------------


ans = part_A() if (CMD == "A" or CMD == "a") else part_B()
print("ANSWER:", ans)
if CMD != "a" and CMD != "b" and ans != 0:
    submit(ans)