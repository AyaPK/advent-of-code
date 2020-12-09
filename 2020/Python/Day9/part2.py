import cProfile


def f():
    data = [int(x.replace("\n","")) for x in open("input.txt", "r").readlines()]

    number_to_find = 2089807806
    preamble_length = 25
    numbers = data[:preamble_length]
    pointer = preamble_length+0
    xbreak = False
    not_found = True
    while not_found:
        for x in range(26):
            n = numbers[x]
            if xbreak:
                xbreak = False
                break
            for y in range(1, 26):
                try:
                    n += numbers[y]
                except:
                    xbreak = True
                    break
                if n < number_to_find:
                    continue
                elif n > number_to_find:
                    xbreak = True
                    break
                elif n == number_to_find:
                    arr = numbers[x:y+1]
                    arr.sort()
                    print(arr[0]+arr[len(arr)-1])
                    not_found = False
        numbers = numbers[1:]
        numbers.append(data[pointer])
        pointer += 1

cProfile.run("f()")



