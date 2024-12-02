reports = [x.strip() for x in open("input.txt").readlines()]

found = 0
for report in reports:
    report = report.split(" ")
    report = [int(x) for x in report]
    asc = sorted(report)
    desc = sorted(report, reverse=True)
    f = True
    dampened = False

    if report == asc or report == desc:
        for i, x in enumerate(report):
            f = True
            dampened = False
            x = int(x)
            try:
                y = int(report[i+1])
            except:
                break

            if abs(x-y) < 1 or abs(x-y) > 3:
                if not dampened:
                    dampened = True
                    try:
                        y = int(report[i + 2])
                    except:
                        break
                    if abs(x - y) < 1 or abs(x - y) > 3:
                        f = False
                        break
        if f:
            found += 1

print(found)


