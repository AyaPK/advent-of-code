lines = [x.strip() for x in open("input.txt").readlines()]
left = [int(x.split("   ")[0]) for x in lines]
right = [int(x.split("   ")[1]) for x in lines]

left.sort()
right.sort()
nums = []

for i, x in enumerate(left):
    nums.append(abs(x-right[i]))

print(sum(nums))