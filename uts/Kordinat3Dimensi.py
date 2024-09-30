from __future__ import annotations

class Kordinat3Dimensi:

    __i : int
    __j : int
    __k : int

    def __init__(self, i : int, j : int, k : int):
        self.__i = i
        self.__j = j
        self.__k = k

    def panjang_2_kordinat(self, A : Kordinat3Dimensi, B : Kordinat3Dimensi = NotImplemented) -> int:
        result : int
        if isinstance(B, Kordinat3Dimensi):
            result = (A.__i - B.__i) ** 2 + (A.__j - B.__j) ** 2 + (A.__k - B.__k) ** 2

        else:
            result = (self.__i - A.__i) ** 2 + (self.__j - A.__j) ** 2 + (self.__k - A.__k) ** 2
        return result

    def cos_alfa(self, B : Kordinat3Dimensi, C : Kordinat3Dimensi) -> float:
        ab = self.panjang_2_kordinat(B)
        ac = self.panjang_2_kordinat(C)
        bc = self.panjang_2_kordinat(B, C)
        return (ab + ac + bc) / (2 * ab * ac)

    def tampil(self):
        print(f"({self.__i}, {self.__j}, {self.__k})")

def main():
    a = Kordinat3Dimensi(1, 2, 3)
    b = Kordinat3Dimensi(4, 5, 6)
    c = Kordinat3Dimensi(7, 8, 9)

    a.tampil()

    print(a.panjang_2_kordinat(b))

    print(a.cos_alfa(b, c))

if __name__ == "__main__":
    main()
