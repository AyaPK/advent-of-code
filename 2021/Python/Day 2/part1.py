class Submarine:
    def __init__(self):
        self.xpos = 0
        self.ypos = 0
        self.aim = 0


data = [x.strip() for x in open("input.txt", "r").readlines()]

sub = Submarine()
for i in data:
    instruction = i.split(" ")[0]
    amount = int(i.split(" ")[1])
    if instruction == "forward":
        sub.xpos += amount
    elif instruction == "up":
        sub.ypos -= amount
    else:
        sub.ypos += amount
print(sub.ypos * sub.xpos)