def parse_input():
    with open("day6-1-input.txt") as file:
        return [int(c) for c in file.readline().strip().split(",")]


def main():
    fishes = parse_input()
    days = 80

    while days > 0:
        for i in range(len(fishes)):
            if fishes[i] - 1 == -1:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] = fishes[i] - 1
        days -= 1

    print(len(fishes))


if __name__ == "__main__":
    main()
