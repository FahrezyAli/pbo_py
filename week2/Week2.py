class BendaBulat:
    
    def luas_lingkaran(self, radius : int) -> float:
        return 3.14 * radius * radius
    
    def volume_bola(self, radius : int) -> float:
        return (4/3) * 3.14 * radius * radius * radius

class BendaBulatDua:

    _radius : int

    def set_radius(self, radius : int):
        self._radius = radius

    def get_radius(self) -> int:
        return self._radius
    
    def luas_lingkaran(self) -> float:
        return 3.14 * self._radius * self._radius
    
    def volume_bola(self) -> float:
        return (4/3) * 3.14 * self._radius * self._radius * self._radius
    
class BidangSegi4:

    def luas_bujur_sangkar(self, panjang : int) -> int:
        return panjang * panjang
    
    def luas_persegi_panjang(self, panjang : int, lebar : int) -> int:
        return panjang * lebar
    
class BidangSegi4Dua:

    _panjang : int
    _lebar : int

    def set_panjang(self, panjang : int):
        self._panjang = panjang

    def set_lebar(self, lebar : int):
        self._lebar = lebar

    def get_panjang(self) -> int:
        return self._panjang
    
    def get_lebar(self) -> int:
        return self._lebar
    
    def luas_bujur_sangkar(self) -> int:
        return self._panjang * self._panjang
    
    def luas_persegi_panjang(self) -> int:
        return self._panjang * self._lebar