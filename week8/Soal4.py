from Cast import cast

class BendaPersegi:
    _panjang : int
    _lebar : int
    _warna : str

    def __init__(self, panjang : int = 0, lebar : int = 0, warna : str = "hitam"):
        self._panjang = panjang
        self._lebar = lebar
        self._warna = warna

    def get_panjang(self) -> int:
        return self._panjang
    
    def get_lebar(self) -> int:
        return self._lebar
    
    def get_warna(self) -> str:
        return self._warna
    
    def display(self):
        print(f"Panjang : {self._panjang}")
        print(f"Lebar   : {self._lebar}")
        print(f"Warna   : {self._warna}")

class Balok(BendaPersegi):
    __tinggi : int

    def __init__(self, panjang: int = 0, lebar: int = 0, tinggi : int = 0, warna: str = "hitam"):
        super().__init__(panjang, lebar, warna)
        self.__tinggi = tinggi

    def get_tinggi(self) -> int:
        return self.__tinggi
    
    def volume_balok(self) -> int:
        return self._panjang * self._lebar * self.__tinggi
    
    def display(self):
        print(f"Panjang : {self._panjang}")
        print(f"Lebar   : {self._lebar}")
        print(f"Tinggi  : {self.__tinggi}")
        print(f"Warna   : {self._warna}")
        print(f"Volume  : {self.volume_balok()}")

def main():
    bl1 = Balok(5, 7, 10, "biru")
    bl1.display()
    print()

    bp1 = cast(bl1, BendaPersegi)
    bp1.display() # type: ignore
    print()

    bl2 = cast(bp1, Balok)
    bl2.display() # type: ignore
    print()
    
if __name__ == "__main__":
    main()