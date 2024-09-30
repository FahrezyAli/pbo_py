from __future__ import annotations

class MatriksQ:
    __col : int
    __row : int
    __elements : list[list[int]]

    def __init__(self, elements : list[list[int]]):
        self.__col = len(elements[0])
        self.__row = len(elements)
        self.__elements = elements

    def get_col(self) -> int:
        return self.__col
    
    def get_row(self) -> int:
        return self.__row
    
    def get_elements(self) -> list[list[int]]:
        return self.__elements

    def tampil_vektor(self):
        print(self.__elements)

class VektorQ:
    __len : int
    __elements : list[int]

    def __init__(self, elements : list[int]):
        self.__len = len(elements)
        self.__elements = elements

    def get_elements(self) -> list[int]:
        return self.__elements
    
    def jumlah_2_vektor(self, v : VektorQ) -> VektorQ:
        result = []

        for i in range(self.__len):
            result.append(self.__elements[i] + v.__elements[i])

        return VektorQ(result)
    
    def tampil_vektor(self):
        print(self.__elements)

def main():
    matriks = MatriksQ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    vektor1 = VektorQ(matriks.get_elements()[0])
    vektor2 = VektorQ(matriks.get_elements()[1])
    vektor3 = VektorQ(matriks.get_elements()[2])

    vektor4 = vektor1.jumlah_2_vektor(vektor2)

    matriks2 = MatriksQ([vektor1.get_elements(), vektor4.get_elements()])
    matriks2.tampil_vektor()

if __name__ == "__main__":
    main()