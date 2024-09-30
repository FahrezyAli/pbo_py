import math

class Shape:
    _name : str

    def __init__(self, name : str):
        self._name = name

    def get_name(self):
        return self._name
    
    def calculate_area(self):
        return 0
    
class Circle(Shape):
    _radius : float

    def __init__(self, name: str, r : float):
        super().__init__(name)
        self._radius = r

    def calculate_area(self):
        return math.pi * self._radius * self._radius
    
class Square(Shape):
    _sisi : float

    def __init__(self, name: str, s : float):
        super().__init__(name)
        self._sisi = s

    def calculate_area(self):
        return self._sisi * self._sisi
    
def main():
    bulat = Circle("bulat", 10)
    kotak = Square("kotak", 10)

    print(f"luas {bulat.get_name()}: {bulat.calculate_area()}")
    print(f"luas {kotak.get_name()}: {kotak.calculate_area()}")

if __name__ == "__main__":
    main()