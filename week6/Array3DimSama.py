from __future__ import annotations

class Array3DimSama:
    _x : int
    _y : int
    _z : int
    _elements : list[list[list[int]]]

    def __init__(self, const1 : Array3DimSama | list[list[list[int]]] | int = NotImplemented, const2 : int = 0, const3 : int = 0): 
        if isinstance(const1, Array3DimSama):
            self._x = const1._x
            self._y = const1._y
            self._z = const1._z
            self._elements = const1._elements
        elif isinstance(const1, list):
            self._x = len(const1)
            self._y = len(const1[0])
            self._z = len(const1[0][0])
            self._elements = const1
        elif isinstance(const1, int):
            self._x = const1
            self._y = const2
            self._z = const3
            self._elements = [[[0 for _ in range(const3)] for _ in range(const2)] for _ in range(const1)]
        else:
            self._x = 0
            self._y = 0
            self._z = 0
            self._elements = [[[]]]

    def jumlah_2_array_3d_sama(self, m1 : Array3DimSama, m2 : Array3DimSama = NotImplemented) -> Array3DimSama:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Array3DimSama):
            used_m1 = m1
            used_m2 = m2

        result = [[[0 for _ in range(used_m1._z)] for _ in range(used_m1._y)] for _ in range(used_m1._x)]
        for i in range(used_m1._x):
            for j in range(used_m1._y):
                for k in range(used_m1._z):
                    result[i][j][k] = used_m1._elements[i][j][k] + used_m2._elements[i][j][k]
    
        return Array3DimSama(result)
    
    def selisih_2_array_3d_sama(self, m1 : Array3DimSama, m2 : Array3DimSama = NotImplemented) -> Array3DimSama:
        used_m1 = self
        used_m2 = m1
        if isinstance(m2, Array3DimSama):
            used_m1 = m1
            used_m2 = m2

        result = [[[0 for _ in range(used_m1._z)] for _ in range(used_m1._y)] for _ in range(used_m1._x)]
        for i in range(used_m1._x):
            for j in range(used_m1._y):
                for k in range(used_m1._z):
                    result[i][j][k] = used_m1._elements[i][j][k] - used_m2._elements[i][j][k]
    
        return Array3DimSama(result)
    
    def tampil_array_3d_sama(self, m : Array3DimSama = NotImplemented):
        if isinstance(m, Array3DimSama):
            print(m._elements)
        else:
            print(self._elements)

a = Array3DimSama([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]) # array
b = Array3DimSama([[[3, 4], [5, 6]], [[1, 2], [7, 8]], [[11, 12], [10, 9]]]) # array
c = Array3DimSama(a) # object Array3DimSama
d = Array3DimSama() # tanpa parameter
e = Array3DimSama(5, 3, 4) # 3 parameter x, y, z

print("a = ", end = "")
a.tampil_array_3d_sama()

print("b = ", end = "")
b.tampil_array_3d_sama()

print("c = ", end = "")
c.tampil_array_3d_sama()

print("d = ", end = "")
Array3DimSama.tampil_array_3d_sama(d)

print("e = ", end = "")
e.tampil_array_3d_sama()

print("a + c = ", end = "")
a.jumlah_2_array_3d_sama(c).tampil_array_3d_sama()

print("a + b = ", end = "")
Array3DimSama.tampil_array_3d_sama(Array3DimSama.jumlah_2_array_3d_sama(a, b))

print("a - c = ", end = "")
a.selisih_2_array_3d_sama(c).tampil_array_3d_sama()

print("b - c = ", end = "")
Array3DimSama.tampil_array_3d_sama(Array3DimSama.selisih_2_array_3d_sama(b, c))