from functools import reduce
from itertools import groupby
from math import prod

lines = open("input.txt").read().splitlines()

# ---------- Part 1 ----------
def eval_column(col):
    nums = list(map(int, col[:-1]))
    op = int.__add__ if col[-1] == "+" else int.__mul__
    return reduce(op, nums)

columns = list(zip(*(l.split() for l in lines if l.strip())))
part1 = sum(eval_column(col) for col in columns)
print(part1)

width = max(len(line) for line in lines)
cols = ["".join(c) for c in zip(*(l.ljust(width) for l in lines))]

def evaluate_block(block):
    has_plus = any(c.endswith("+") for c in block)
    fn = sum if has_plus else prod
    values = [int(c[:-1].replace(" ", "")) for c in block if c[:-1].strip()]
    return fn(values)

part2 = sum(
    evaluate_block(list(group))
    for is_blank, group in groupby(cols, key=lambda x: not x.strip())
    if not is_blank
)

print(part2)
