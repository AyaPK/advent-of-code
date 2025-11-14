lines = [x.strip() for x in open("input.txt").readlines()]

def decode_line(line):
    patterns, outputs = line.split(" | ")
    patterns = ["".join(sorted(p)) for p in patterns.split()]
    outputs = ["".join(sorted(o)) for o in outputs.split()]

    # Map of segment pattern → digit
    digits = {}

    # Group patterns by length
    by_len = {}
    for p in patterns:
        by_len.setdefault(len(p), []).append(p)

    # Easy ones by unique length
    digits[1] = by_len[2][0]
    digits[4] = by_len[4][0]
    digits[7] = by_len[3][0]
    digits[8] = by_len[7][0]

    # 3 = length 5 and contains all of 1
    digits[3] = next(p for p in by_len[5] if all(c in p for c in digits[1]))
    # 9 = length 6 and contains all of 3
    digits[9] = next(p for p in by_len[6] if all(c in p for c in digits[3]))
    # 0 = length 6 and contains all of 1 but is not 9
    digits[0] = next(p for p in by_len[6] if all(c in p for c in digits[1]) and p != digits[9])
    # 6 = remaining length-6
    digits[6] = next(p for p in by_len[6] if p not in (digits[0], digits[9]))
    # 5 = length-5 and is subset of 6
    digits[5] = next(p for p in by_len[5] if all(c in digits[6] for c in p))
    # 2 = remaining length-5
    digits[2] = next(p for p in by_len[5] if p not in (digits[3], digits[5]))

    # Build reverse lookup
    pattern_to_digit = {v: str(k) for k, v in digits.items()}

    # Decode outputs
    value = int("".join(pattern_to_digit[o] for o in outputs))
    return value

total = sum(decode_line(line) for line in lines)
print(total)
