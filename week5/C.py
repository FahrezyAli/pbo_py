from __future__ import annotations

class Vektor:
    _length : int
    _elements : list[int]

    def __init__(self, construct : list[int] | Vektor): 
        if isinstance(construct, Vektor):
            self._length = construct._length
            self._elements = construct._elements
        else:
            self._length = len(construct)
            self._elements = construct

    def jumlah_2_vektor(self, v1 : Vektor, v2 : Vektor = NotImplemented) -> Vektor:
        result = []
        used_var1 = self
        used_var2 = v1
        if isinstance(v2, Vektor):
            used_var1 = v1
            used_var2 = v2

        used_length = min(used_var1._length, used_var2._length)
        for i in range(used_length):
            result.append(used_var1._elements[i] + used_var2._elements[i])
    
        if used_var1._length > used_var2._length:
            for i in range(used_var2._length, used_var1._length):
                result.append(used_var1._elements[i])
        else:
            for i in range(used_var1._length, used_var2._length):
                result.append(used_var2._elements[i])

        return Vektor(result)
    
    def selisih_2_vektor(self, v1 : Vektor, v2 : Vektor = NotImplemented) -> Vektor:
        result = []
        used_var1 = self
        used_var2 = v1
        if isinstance(v2, Vektor):
            used_var1 = v1
            used_var2 = v2

        used_length = min(used_var1._length, used_var2._length)
        for i in range(used_length):
            result.append(used_var1._elements[i] - used_var2._elements[i])
    
        if used_var1._length > used_var2._length:
            for i in range(used_var2._length, used_var1._length):
                result.append(used_var1._elements[i])
        else:
            for i in range(used_var1._length, used_var2._length):
                result.append(used_var2._elements[i])

        return Vektor(result)
    
    def tampil_vektor(self, v : Vektor = NotImplemented):
        if isinstance(v, Vektor):
            print(v._elements)
        else:
            print(self._elements)

def main():
    a = Vektor([1, 2, 3])
    b = Vektor([4, 5, 6, 7, 10])
    c = Vektor(a)

    c.tampil_vektor()
    Vektor.tampil_vektor(c)

    a.jumlah_2_vektor(c).tampil_vektor()
    Vektor.tampil_vektor(Vektor.jumlah_2_vektor(a, c))
    a.jumlah_2_vektor(b).tampil_vektor()

    b.selisih_2_vektor(c).tampil_vektor()
    Vektor.tampil_vektor(Vektor.selisih_2_vektor(b, c))

if __name__ == "__main__":
    main()