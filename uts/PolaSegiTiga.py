import random

class PolaSegiTiga:
    __tinggi : int

    def __init__(self, tinggi : int):
        self.__tinggi = tinggi

    def generate(self):
        random.seed(15)
        k = random.randint(0, 10)

        for i in range(0, self.__tinggi + 1):
            for j in range(0, i):
                print(k, end = " ")
                k = random.randint(0, 10)
            print()

def main():
    n = int(input("Tinggi Pola = "))

    pola = PolaSegiTiga(n)

    pola.generate()

if __name__ == "__main__":
    main()

