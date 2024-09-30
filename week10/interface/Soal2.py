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
class C(B):
    NILAI_A = 15
    c : int

    def __init__(self, b: int, c : int):
        super().__init__(b)
        self.c = c

    def tampil_bc(self):
        print(self.b)
        print(self.c)

    def tampil_konstanta(self):
        print(self.NILAI_A)
        print(B.NILAI_B)

    def hitung_kali(self, a : int, b : int) -> int:
        return a * b

def main():
    c = C(5, 10)

    print(c.hitung_kurang(5, 10))

    print(c.tampil_bc())
    print(c.tampil_konstanta())
    print(c.hitung_kali(5, 10))

if __name__ == "__main__":
    main()