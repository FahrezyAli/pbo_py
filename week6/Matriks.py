from __future__ import annotations

class Matriks:
    _col : int
    _row : int
    _elements : list[list[int]]

    def __init__(self, const1 : Matriks | list[list[int]] | int =  NotImplemented, const2 : int = 0): 
        if isinstance(const1, Matriks):
            self._col = const1._col
            self._row = const1._row
            self._elements = const1._elements
        elif isinstance(const1, list):
            self._col = len(const1[0])
            self._row = len(const1)
            self._elements = const1
        elif isinstance(const1, int):
            self._col = const1
            self._row = const2
            self._elements = [[0 for _ in range(const1)] for _ in range(const2)]
        else:
            self._col = 0
            self._row = 0
            self._elements = [[]]

    def jumlah_2_matriks(self, m1 : Matriks, m2 : Matriks = NotImplemented) -> Matriks:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Matriks):
            used_m1 = m1
            used_m2 = m2

        used_col = min(used_m1._col, used_m2._col)
        used_row = min(used_m1._row, used_m2._row)
        result = [[0 for _ in range(used_col)] for _ in range(used_row)]
        for i in range(used_col):
            for j in range(used_row):
                result[j][i] = used_m1._elements[j][i] + used_m2._elements[j][i]
    
        return Matriks(result)
    
    def selisih_2_matriks(self, m1 : Matriks, m2 : Matriks = NotImplemented) -> Matriks:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Matriks):
            used_m1 = m1
            used_m2 = m2

        used_col = min(used_m1._col, used_m2._col)
        used_row = min(used_m1._row, used_m2._row)
        result = [[0 for _ in range(used_col)] for _ in range(used_row)]
        for i in range(used_col):
            for j in range(used_row):
                result[j][i] = used_m1._elements[j][i] - used_m2._elements[j][i]
    
        return Matriks(result)
    
    def tampil_matriks(self, m : Matriks = NotImplemented):
        if isinstance(m, Matriks):
            print(m._elements)
        else:
            print(self._elements)

a = Matriks([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) # array
b = Matriks([[1, 2, 3],[5, 6, 7]]) # array
c = Matriks(a) # object Matriks
d = Matriks() # tanpa parameter
e = Matriks(5, 3) # dua parameter column dan row

print("a = ", end = "")
a.tampil_matriks()

print("b = ", end = "")
b.tampil_matriks()

print("c = ", end = "")
c.tampil_matriks()

print("d = ", end = "")
Matriks.tampil_matriks(d)

print("e = ", end = "")
e.tampil_matriks()

print("a + c = ", end = "")
a.jumlah_2_matriks(c).tampil_matriks()

print("a + b = ", end = "")
Matriks.tampil_matriks(Matriks.jumlah_2_matriks(a, b))

print("a - c = ", end = "")
a.selisih_2_matriks(c).tampil_matriks()

print("b - c = ", end = "")
Matriks.tampil_matriks(Matriks.selisih_2_matriks(b, c))