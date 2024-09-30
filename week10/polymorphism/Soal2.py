from __future__ import annotations
from abc import ABC, abstractmethod
from math import pi
from typing_extensions import override

class RoundShape(ABC):
    __radius : int
    __objC : Center

    def __init__(self, r : int, x : int, y : int, z : int = 0):
        self.__radius = r
        self.__objC = self.Center(x, y, z)

    class Center(ABC):
        __x : int
        __y : int
        __z : int

        def __init__(self, x : int, y : int, z : int = 0):
            self.__x = x
            self.__y = y
            self.__z = z

    @abstractmethod
    def get_radius(self) -> int:
        return self.__radius

    @abstractmethod
    def area(self) -> float:
        pass

class Circle(RoundShape):

    def __init__(self, r: int, x: int, y: int):
        super().__init__(r, x, y)

    @override
    def get_radius(self) -> int:
        return super().get_radius()

    @override
    def area(self) -> float:
        return pi * self.get_radius() * self.get_radius()

class Sphere(RoundShape):

    def __init__(self, r: int, x: int, y: int, z):
        super().__init__(r, x, y, z)

    @override
    def get_radius(self) -> int:
        return super().get_radius()

    @override
    def area(self) -> float:
        return 4 * pi * self.get_radius() * self.get_radius()
    
class Tabung(Sphere):
    __t : int

    def __init__(self, r: int, t : int, x: int, y: int, z: int = 0):
        super().__init__(r, x, y, z)
        self.__t = t

    @override
    def get_radius(self) -> int:
        return super().get_radius()

    @override
    def area(self) -> float:
        return self.__t * 2 * pi * self.get_radius()
    
def main():
    lingkaran = Circle(7, 1, 2)
    bola = Sphere(14, 3, 2, 3)
    tabung = Tabung(20, 10, 3, 2, 3)

    print("Circle")
    print(f"Area : {lingkaran.area()}\n")

    print("Sphere")
    print(f"Area : {bola.area()}\n")

    print("Tabung")
    print(f"Area : {tabung.area()}\n")

if __name__ == "__main__":
    main()