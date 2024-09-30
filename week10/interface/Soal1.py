from zope.interface import Interface, implementer, Attribute

class A(Interface): # type: ignore
    NILAI_A = Attribute("NILAI_A")

    def hitung_kali(self, a : int, b : int) -> int: # type: ignore
        pass

class B:
    NILAI_B = 10
    b : int

    def __init__(self, b : int):
        self.b = b

    def get_b(self) -> int:
        return self.b

    def hitung_kurang(self, a : int, b : int) -> int:
        return a - b
    
@implementer(A)
class C:
    NILAI_A = 15
    c : int

    def __init__(self, c : int):
        self.c = c

    def tampil_bc(self, b : B):
        print(b.get_b())
        print(self.c)

    def tampil_konstanta(self):
        print(self.NILAI_A)
        print(B.NILAI_B)

    def hitung_kali(self, a : int, b : int) -> int:
        return a * b

def main():
    b = B(5)
    c = C(10)

    print(b.hitung_kurang(5, 10))

    print(c.tampil_bc(b))
    print(c.tampil_konstanta())
    print(c.hitung_kali(5, 10))

if __name__ == "__main__":
    main()