import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)


die_6 = Die(6)

print("Tiradas del dado de 6 caras:")
for _ in range(10):
    print(die_6.roll_die())

die_10 = Die(10)

print("\nTiradas del dado de 10 caras:")
for _ in range(10):
    print(die_10.roll_die())

die_20 = Die(20)

print("\nTiradas del dado de 20 caras:")
for _ in range(10):
    print(die_20.roll_die())
