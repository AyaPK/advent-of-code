details = [x.strip() for x in open("input.txt", "r").readlines()]
reindeers = []

class Reindeer:
    is_flying = True
    rested_time = 0
    flight_time = 0
    flight_distance = 0

    def __init__(self, detail):
        self.speed = int(detail.split(" ")[3])
        self.stamina = int(detail.split(" ")[6])
        self.rest = int(detail.split(" ")[-2])

    def to_string(self):
        return f"This reindeer can fly {self.speed} km/s for {self.stamina} seconds, and needs {self.rest} seconds to recover"

    def distance_string(self):
        return f"This reindeer has flown {self.flight_distance}"

    def take_turn(self):
        if self.is_flying:
            self.flight_distance += self.speed
            self.flight_time += 1
            if self.flight_time == self.stamina:
                self.flight_time = 0
                self.is_flying = False
        else:
            self.rested_time += 1
            if self.rested_time == self.rest:
                self.is_flying = True
                self.rested_time = 0

for detail in details:
    reindeers.append(Reindeer(detail))

for x in range(2503):
    for r in reindeers:
        r.take_turn()

distances = []
for r in reindeers:
    distances.append(r.flight_distance)
print(max(distances))