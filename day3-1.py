from collections import Counter

bits = []

with open("day3-input.txt") as f:
    x = 0
    for ch in f.read():

        if ch == "\n":
            x = 0
            continue

        if len(bits) <= x:
            bits.append([])

        bits[x].append(ch)
        x += 1

gamma = epsilon = ""

for i in range(len(bits)):
    common = Counter(bits[i]).most_common(2)
    gamma += common[0][0]
    epsilon += common[1][0]

print(int(gamma, base=2) * int(epsilon, base=2))
