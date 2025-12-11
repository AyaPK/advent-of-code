lines = [line.strip() for line in open("input.txt").readlines()]

nums1 = [int(x.strip()) for x in lines[0].split(" ") if x]
nums2 = [int(x.strip()) for x in lines[1].split(" ") if x]
nums3 = [int(x.strip()) for x in lines[2].split(" ") if x]
nums4 = [int(x.strip()) for x in lines[3].split(" ") if x]
symbols = [x.strip() for x in lines[4].split(" ") if x]

print(nums1)
print(nums2)
print(nums3)
print(symbols)

total = 0
print(symbols)
for x in range(len(nums1)):
    n1 = nums1[x]
    n2 = nums2[x]
    n3 = nums3[x]
    n4 = nums4[x]
    sym = symbols[x]

    if sym == "+":
        result = n1 + n2 + n3 + n4
    elif sym == "-":
        result = n1 - n2 - n3 - n4
    elif sym == "*":
        result = n1 * n2 * n3 * n4
    elif sym == "/":
        if n2 == 0 or n3 == 0:
            result = "undefined"
        else:
            result = n1 / n2 / n3 / n4
    else:
        result = "invalid symbol"
    total += int(result)

"""
math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Reading the problems right-to-left one column at a time, the problems are now quite different:

    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544

Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

