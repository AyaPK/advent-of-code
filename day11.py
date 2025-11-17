# ...existing code...

def generate_step2_pattern():
    size = 5
    max_val = 5
    center = size // 2
    grid = []
    for row in range(size):
        line = []
        for col in range(size):
            val = max_val - abs(center - row) - abs(center - col)
            line.append(str(val))
        grid.append("".join(line))
    return grid

# Example usage:
for line in generate_step2_pattern():
    print(line)

# ...existing code...
