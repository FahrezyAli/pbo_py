from __future__ import annotations
import math

class KordinatNDimensi:

    __kordinat : list[int]

    def __init__(self, kordinat : list[int]):
        self.__kordinat = kordinat

    def set_kordinat(self, kordinat):
        self.__kordinat = kordinat

    def get_kordinat(self) -> list[int]:
        return self.__kordinat
    
    def jarak_2_titik(self, B : KordinatNDimensi) -> float:
        result : float = 0

        if len(self.__kordinat) != len(B.__kordinat):
            print("Illegal Operations: Length of both coordinate is not the same!")

        else:
            length = len(self.__kordinat)
            for i in range(0, length):
                result += (self.__kordinat[i] - B.__kordinat[i]) ** 2
                
            result = math.sqrt(result)

        return result
    
def main():
    titik_satu = KordinatNDimensi([1, 2, 3, 4, 5])
    titik_dua  = KordinatNDimensi([6, 7, 8, 9])

    print(titik_satu.get_kordinat())

    print(titik_satu.jarak_2_titik(titik_dua))

    titik_dua.set_kordinat([6, 7, 8, 9, 10])

    print(titik_dua.jarak_2_titik(titik_satu))

if __name__ == "__main__":
    main()
