import ast
import re

print(sum(2+s.count('\\')+s.count('"') for s in open("input.txt")))

