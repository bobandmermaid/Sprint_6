import random


def random_telephone():
    region = '+7'
    operator = random.randint(900, 999)
    number = random.randint(1000000, 9999999)

    return region + str(operator) + str(number)
