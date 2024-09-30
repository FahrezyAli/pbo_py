from math import pi

class BendaBulat:
    _radius : float
    _tinggi : float

    def __init__(self, radius : float, tinggi : float = 0):
        self._radius = radius
        self._tinggi = tinggi

    def luas_lingkaran(self) -> float:
        return pi * self._radius * self._radius
    
    def volume_bola(self) -> float:
        return (4/3) * pi * self._radius * self._radius * self._radius
    
    def luas_permukaan_tabung(self) -> float:
        return 2 * pi * self._radius * (self._radius + self._tinggi)
    
    def volume_silinder(self) -> float:
        return pi * self._radius * self._radius * self._tinggi

class BidangSegi4:
    _panjang : float
    _lebar : float
    _tinggi : float

    def __init__(self, panjang : float, lebar : float = 0, tinggi : float = 0):
        self._panjang = panjang
        self._lebar = lebar
        self._tinggi = tinggi

    def luas_bujur_sangkar(self) -> float:
        return self._panjang * self._panjang
    
    def volume_kubus(self) -> float:
        return self._panjang * self._panjang * self._panjang
    
    def luas_persegi_panjang(self) -> float:
        return self._panjang * self._lebar
    
    def volume_balok(self) -> float:
        return self._panjang * self._lebar * self._tinggi