from dataclasses import dataclass


@dataclass
class Command:
    direction: str
    value: int


class Submarine:
    def __init__(self):
        self.depth = 0
        self.position = 0
        self.ops = {"forward": self.forward, "up": self.up, "down": self.down}

    def do(self, command: Command):
        self.ops[command.direction](command.value)

    def forward(self, value):
        self.position += value

    def up(self, value):
        self.depth -= value

    def down(self, value):
        self.depth += value


commands = []

with open("day2-1-input.txt", "r") as file:
    for line in file:
        direction, value = line.strip().split(" ")
        commands.append(Command(direction, int(value)))

submarine = Submarine()

for command in commands:
    submarine.do(command)

print(submarine.depth * submarine.position)
