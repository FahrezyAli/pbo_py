from zope.interface import Interface, implementer, Attribute

class A(Interface): # type: ignore
    NILAI_A = Attribute("NILAI_A")
    
    def hitung_kali(self, a : int, b : int) -> int: # type: ignore
        pass

class B(Interface): # type: ignore
    NILAI_B = Attribute("NILAI_B")

    def hitung_kurang(self, a : int, b : int) -> int: # type: ignore
        pass

@implementer(A, B)
class C(Interface): # type: ignore
    NILAI_C = Attribute("NILAI_C")

    def hitung_jumlah(self, a : int, b : int) -> int: # type: ignore
        pass

@implementer(C)
class D:
    NILAI_A = 5
    NILAI_B = 10
    NILAI_C = 15

    d : int

    def __init__(self, d : int = 0):
        self.d = d

    def tampil_d(self):
        print(self.d)

    def tampil_konstanta(self):
        print(self.NILAI_A)
        print(self.NILAI_B)
        print(self.NILAI_C)

    def hitung_kali(self, a : int, b : int) -> int:
        return a * b
    
    def hitung_jumlah(self, a : int, b : int) -> int:
        return a + b
    
    def hitung_kurang(self, a : int, b : int) -> int:
        return a - b
    
def main():
    c1 = D()
    c2 = D(5)

    c1.tampil_d()
    c2.tampil_d()

    c2.tampil_konstanta()

    c2.hitung_jumlah(5, 5)
    c2.hitung_kali(10, 2)
    c2.hitung_kurang(10, 7)

if __name__ == "__main__":
    main()