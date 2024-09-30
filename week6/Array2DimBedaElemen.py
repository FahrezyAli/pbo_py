from __future__ import annotations

class Array2DimBedaElemen:
    _col : int
    _row : int
    _elements : list[list[int]]

    def __init__(self, const1 : Array2DimBedaElemen | list[list[int]] | int =  NotImplemented, const2 : int = 0): 
        if isinstance(const1, Array2DimBedaElemen):
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

    def jumlah_2_array_2d_beda_elemen(self, m1 : Array2DimBedaElemen, m2 : Array2DimBedaElemen = NotImplemented) -> Array2DimBedaElemen:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Array2DimBedaElemen):
            used_m1 = m1
            used_m2 = m2

        used_col = min(used_m1._col, used_m2._col)
        used_row = min(used_m1._row, used_m2._row)
        result = [[0 for _ in range(used_col)] for _ in range(used_row)]
        for i in range(used_col):
            for j in range(used_row):
                result[j][i] = used_m1._elements[j][i] + used_m2._elements[j][i]
    
        return Array2DimBedaElemen(result)
    
    def selisih_2_array_2d_beda_elemen(self, m1 : Array2DimBedaElemen, m2 : Array2DimBedaElemen = NotImplemented) -> Array2DimBedaElemen:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Array2DimBedaElemen):
            used_m1 = m1
            used_m2 = m2

        used_col = min(used_m1._col, used_m2._col)
        used_row = min(used_m1._row, used_m2._row)
        result = [[0 for _ in range(used_col)] for _ in range(used_row)]
        for i in range(used_col):
            for j in range(used_row):
                result[j][i] = used_m1._elements[j][i] - used_m2._elements[j][i]
    
        return Array2DimBedaElemen(result)
    
    def tampil_array_2d_beda_elemen(self, m : Array2DimBedaElemen = NotImplemented):
        if isinstance(m, Array2DimBedaElemen):
            print(m._elements)
        else:
            print(self._elements)

a = Array2DimBedaElemen([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) # array
b = Array2DimBedaElemen([[1, 2, 3],[5, 6, 7]]) # array
c = Array2DimBedaElemen(a) # object Array2DimBedaElemen
d = Array2DimBedaElemen() # tanpa parameter
e = Array2DimBedaElemen(5, 3) # dua parameter column dan row

print("a = ", end = "")
a.tampil_array_2d_beda_elemen()

print("b = ", end = "")
b.tampil_array_2d_beda_elemen()

print("c = ", end = "")
c.tampil_array_2d_beda_elemen()

print("d = ", end = "")
Array2DimBedaElemen.tampil_array_2d_beda_elemen(d)

print("e = ", end = "")
e.tampil_array_2d_beda_elemen()

print("a + c = ", end = "")
a.jumlah_2_array_2d_beda_elemen(c).tampil_array_2d_beda_elemen()

print("a + b = ", end = "")
Array2DimBedaElemen.tampil_array_2d_beda_elemen(Array2DimBedaElemen.jumlah_2_array_2d_beda_elemen(a, b))

print("a - c = ", end = "")
a.selisih_2_array_2d_beda_elemen(c).tampil_array_2d_beda_elemen()

print("b - c = ", end = "")
Array2DimBedaElemen.tampil_array_2d_beda_elemen(Array2DimBedaElemen.selisih_2_array_2d_beda_elemen(b, c))