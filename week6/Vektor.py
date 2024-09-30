from __future__ import annotations

class Vektor:
    _length : int
    _elements : list[int]

    def __init__(self, const1 : Vektor | list[int] | int = NotImplemented, const2 : int = 0): 
        if isinstance(const1, Vektor): # Jika const1 = Vektor: Copy data
            self._length = const1._length
            self._elements = const1._elements
        elif isinstance(const1, list): # Jika const1 = list: gunakan list
            self._length = len(const1)
            self._elements = const1
        elif isinstance(const1, int): # Jika const1 = int: buat list kosong dengan size const1
            self._length = const1
            self._elements = [0 for _ in range(const1)]
        else: # Jika tidak ada parameter: buat list kosong dengan size 0
            self._length = 0
            self._elements = []

    def jumlah_2_vektor(self, v1 : Vektor, v2 : Vektor = NotImplemented) -> Vektor:
        result = []
        used_v1 = self
        used_v2 = v1
        if isinstance(v2, Vektor):
            used_v1 = v1
            used_v2 = v2

        used_length = min(used_v1._length, used_v2._length)
        for i in range(used_length):
            result.append(used_v1._elements[i] + used_v2._elements[i])

        return Vektor(result)
    
    def selisih_2_vektor(self, v1 : Vektor, v2 : Vektor = NotImplemented) -> Vektor:
        result = []
        used_v1 = self
        used_v2 = v1
        if isinstance(v2, Vektor):
            used_v1 = v1
            used_v2 = v2

        used_length = min(used_v1._length, used_v2._length)
        for i in range(used_length):
            result.append(used_v1._elements[i] - used_v2._elements[i])

        return Vektor(result)
    
    def tampil_vektor(self, v : Vektor = NotImplemented):
        if isinstance(v, Vektor):
            print(v._elements)
        else:
            print(self._elements)

a = Vektor([1, 2, 3]) # array
b = Vektor([4, 5, 6, 7, 10], 5) # array dan size
c = Vektor(a) # object Vektor
d = Vektor() # tanpa parameter
e = Vektor(5) # size 

print("a = ", end = "")
a.tampil_vektor()

print("b = ", end = "")
b.tampil_vektor()

print("c = ", end = "")
c.tampil_vektor()

print("d = ", end = "")
Vektor.tampil_vektor(d)

print("e = ", end = "")
e.tampil_vektor()

print("a + c = ", end = "")
a.jumlah_2_vektor(c).tampil_vektor()

print("a + b = ", end = "")
Vektor.tampil_vektor(Vektor.jumlah_2_vektor(a, b))

print("a - c = ", end = "")
a.selisih_2_vektor(c).tampil_vektor()

print("b - c = ", end = "")
Vektor.tampil_vektor(Vektor.selisih_2_vektor(b, c))