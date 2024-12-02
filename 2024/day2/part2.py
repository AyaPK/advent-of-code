reports = [x.strip() for x in open("input.txt").readlines()]

found = 0


def is_safe(report):
    asc = sorted(report)
    desc = sorted(report, reverse=True)

    if report == asc or report == desc:
        for i, x in enumerate(report):
            f = True
            x = int(x)
            try:
                y = int(report[i+1])
            except:
                break

            if abs(x-y) < 1 or abs(x-y) > 3:
                f = False
                break
        if f:
            return True
    return False


for report in reports:
    report = report.split(" ")
    report = [int(x) for x in report]

    if is_safe(report):
        found += 1
        continue

    dampened = False
    for x in range(len(report)):
        if is_safe(report[:x] + report[x + 1:]):
            found += 1
            dampened = True
            break
    if dampened:
        continue

print(found)


