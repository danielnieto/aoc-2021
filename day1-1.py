import math
arr = []

with open('day1-1-input.txt', 'r') as file:
    for line in file:
        arr.append(int(line))


increases = 0
last = math.inf

for n in arr:
    if n > last:
        increases += 1
    last = n

print(increases)