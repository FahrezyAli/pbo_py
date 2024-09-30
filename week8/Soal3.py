import math
from Cast import cast

class BendaBulat:
    
    _radius : int
    _warna : str

    def __init__(self, radius : int = 0, warna : str = "hitam"):
        self._radius = radius
        self._warna = warna

    def get_radius(self) -> int:
        return self._radius

    def get_warna(self) -> str:
        return self._warna

    def display(self):
        print(f"Radius : {self._radius}")
        print(f"Warna  : {self._warna}")

class Tabung(BendaBulat):

    __tinggi : int

    def __init__(self, radius: int = 0, tinggi : int = 0, warna: str = "hitam"):
        super().__init__(radius, warna)
        self.__tinggi = tinggi 

    def get_tinggi(self) -> int:
        return self.__tinggi
    
    def luas_permukaan_tabung(self) -> float:
        return 2 * math.pi * self._radius * (self._radius + self.__tinggi)
    
    def display(self):
        print(f"Radius         : {self._radius}")
        print(f"Tinggi         : {self.__tinggi}")
        print(f"Warna          : {self._warna}")
        print(f"Luas Permukaan : {self.luas_permukaan_tabung()}")

def main():
    tb1 = Tabung(5, 10, "hijau")
    tb1.display()
    print()

    bb1 = cast(tb1, BendaBulat)
    bb1.display() # type: ignore
    print()

    tb2 = cast(bb1, Tabung)
    tb2.display() # type: ignore

if __name__ == "__main__":
    main()