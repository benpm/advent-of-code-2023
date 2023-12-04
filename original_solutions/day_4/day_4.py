from aocd import submit, get_data
import numpy as np
from sys import argv
import re
from collections import defaultdict

assert len(argv) == 2, "args: [a, b, A, B]"
assert argv[1] in ["a", "b", "A", "B"]

CMD = argv[1]

lines = get_data(day=4, year=2023).splitlines()

if CMD == "a" or CMD == "b":
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]

if lines[-1] == "":
    lines = lines[:-1]

def part_A():
    s = 0
    for l in lines:
        ss = 0
        wins, mines = re.search(r":\s+([0-9 ]+) \| ([0-9 ]+)", l).groups()
        wins = np.array([int(i) for i in wins.split()])
        mines = np.array([int(i) for i in mines.split()])
        for i in range(sum([int(m in wins) for m in mines])):
            ss = 1 if ss == 0 else (ss*2)
        s += ss
    return s

def part_B():
    deck = []
    copies = defaultdict(lambda: 0)
    for i,l in enumerate(lines):
        n1, n2 = re.search(r":\s+([0-9 ]+) \| ([0-9 ]+)", l).groups()
        n1 = np.array([int(i) for i in n1.split()])
        n2 = np.array([int(i) for i in n2.split()])
        deck.append((n1, n2))
        copies[i] = 1

    for i, card in enumerate(deck):
        matches = sum([int(m in card[0]) for m in card[1]])
        for j in range(matches):
            copies[i + j + 1] += copies[i]
    print(copies)
    return sum(list(copies.values()))


# ---------------------------------------------------------------------------


ans = part_A() if (CMD == "A" or CMD == "a") else part_B()
print("ANSWER:", ans)
if CMD != "a" and CMD != "b" and ans != 0:
    submit(ans)
