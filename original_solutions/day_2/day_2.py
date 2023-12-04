from aocd import submit, get_data
import numpy as np
from sys import argv
import re
from collections import defaultdict

assert len(argv) == 2, "args: [a, b, A, B]"
assert argv[1] in ["a", "b", "A", "B"]

CMD = argv[1]

lines = get_data(day=2, year=2023).splitlines()

if CMD == "a" or CMD == "b":
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]

if lines[-1] == "":
    lines = lines[:-1]

def part_A():
    c = {
        "red": 12, "green": 13, "blue": 14
    }
    t = 0
    for l in lines:
        day, games = re.search(r"Game (\d+): (.*)", l).groups()
        p = True
        for g in games.split("; "):
            gs = g.split(", ")
            for s in gs:
                count, color = re.search(r"(\d+) (\w+)", s).groups()
                if color not in c or int(count) > c[color]:
                    p = False
                    break
        if p:
            t += int(day)

    return t

def part_B():
    c = {
        "red": 12, "green": 13, "blue": 14
    }
    t = 0
    for l in lines:
        day, games = re.search(r"Game (\d+): (.*)", l).groups()
        p = True
        for g in games.split("; "):
            gs = g.split(", ")
            for s in gs:
                count, color = re.search(r"(\d+) (\w+)", s).groups()
                if color not in c or int(count) > c[color]:
                    p = False
                    break
        if p:
            t += int(day)

    return t


# ---------------------------------------------------------------------------


ans = part_A() if (CMD == "A" or CMD == "a") else part_B()
print("ANSWER:", ans)
if CMD != "a" and CMD != "b" and ans != 0:
    submit(ans)
