print(
    sum(
        [
            num *
            [
                x.split("   ")[1]
                for x in [
                    x.strip()
                    for x in open("input.txt").readlines()
                ]
            ].count(str(num))
            for num in sorted(
                [
                    int(x.split("   ")[0])
                    for x in [
                        x.strip()
                        for x in open("input.txt").readlines()
                    ]
                ]
            )
        ]
    )
)
