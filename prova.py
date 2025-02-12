import os
os.system('cls')


def runner(brand, model="", year=2021, convertible=False):
    return (brand, str(year), str(convertible))

print(runner("Fermi")[2][2])