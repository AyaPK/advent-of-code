import re

def has_abba(segment):
    for i in range(len(segment) - 3):
        if segment[i] != segment[i + 1] and segment[i:i + 2] == segment[i + 3:i + 1:-1]:
            return True
    return False

def get_parts(file):
    with open(file) as f:
        content = f.read().splitlines()
    processed = [re.split(r'\[|\]', line) for line in content]
    return [(" ".join(parts[::2]), " ".join(parts[1::2])) for parts in processed]

def supports_ssl(supernets, hypernets):
    for supernet in supernets.split():
        for i in range(len(supernet) - 2):
            if supernet[i] == supernet[i + 2] != supernet[i + 1]:
                aba = supernet[i:i + 3]
                bab = aba[1] + aba[0] + aba[1]
                if any(bab in hypernet for hypernet in hypernets.split()):
                    return True
    return False

data = get_parts('input.txt')
result_1 = sum(has_abba(supernets) and not has_abba(hypernets) for supernets, hypernets in data)
result_2 = sum(supports_ssl(supernets, hypernets) for supernets, hypernets in data)

print('Answer #1:', result_1)
print('Answer #2:', result_2)
