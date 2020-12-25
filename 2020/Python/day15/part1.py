arr = open("input.txt", "r").read().split(",")

step = len(arr)-1
while step != 2020:
    num = arr[step]
    if num not in arr[:len(arr)-1]:
        arr.append('0')
        step += 1
    else:
        place = len(arr) - 1 - arr[:len(arr)-1][::-1].index(num)
        arr.append(str(step-place+1))
        step += 1
    if step%1000000== 0:
        print(step)
print(arr[-2])