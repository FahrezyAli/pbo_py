from typing import TypeAlias

numeric : TypeAlias = int | float

class Balok:
    def volume(self, panjang : numeric, lebar : numeric = 0, tinggi : numeric = 0) -> numeric:
        return panjang * lebar * tinggi

def main():
    print(Balok().volume(5))
    print(Balok().volume(5, 2))
    print(Balok().volume(5, 2, 3))

if __name__ == "__main__":
    main()