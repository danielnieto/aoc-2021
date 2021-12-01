import math

arr = []

with open("day1-1-input.txt", "r") as file:
    for line in file:
        arr.append(int(line))

increases = 0
last = math.inf
sums = []

for i in range(len(arr) - 2):
    sums.append(arr[i] + arr[i + 1] + arr[i + 2])

for n in sums:
    if n > last:
        increases += 1
    last = n

print(increases)
