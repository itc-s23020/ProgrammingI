import random

name = "taiki"

while True:
    random_alphabet = random.choice("abcdefghijklmnopqrstuvwxyz")
    print(random_alphabet)

    if random_alphabet.lower() == name[0]:
        break
