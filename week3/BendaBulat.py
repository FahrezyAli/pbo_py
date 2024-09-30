import math

class BendaBulat:

    _radius : float

    def set_radius(self, radius : float):
        self._radius = radius

    def get_radius(self) -> float:
        return self._radius
    
    def keliling_lingkaran(self) -> float:
        return 2 * math.pi * self._radius
    
    def luas_lingkaran(self) -> float:
        return math.pi * self._radius * self._radius
    
    def volume_bola(self) -> float:
        return (4/3) * math.pi * self._radius * self._radius * self._radius

def main():
    radius = float(input("Inputlah radius lingkaran/bola: "))
    lingkaran = BendaBulat()
    lingkaran.set_radius(radius)

    print(f"Keliling Lingkaran: {lingkaran.keliling_lingkaran()}")
    print(f"Luas Lingkaran: {lingkaran.luas_lingkaran()}")
    print(f"Volume Bola: {lingkaran.volume_bola()}")

if __name__ == "__main__":
    main()