from functools import lru_cache


def parse_input():
    with open("day6-1-input.txt") as file:
        return [int(c) for c in file.readline().strip().split(",")]


@lru_cache
def process(fish, days):
    if days == 0:
        return 1

    days -= 1
    return (
        process(8, days) + process(6, days)
        if fish - 1 == -1
        else process(fish - 1, days)
    )


def main():
    fishes = parse_input()
    days = 256

    # calculate how many fishes will a 'prime' fish generate over the days.
    print(sum(map(lambda fish: process(fish, days), fishes)))


if __name__ == "__main__":
    main()
