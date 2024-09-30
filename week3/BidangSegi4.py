class BidangSegi4:

    _panjang : float
    _lebar : float

    def set_panjang(self, panjang : float):
        self._panjang = panjang

    def set_lebar(self, lebar : float):
        self._lebar = lebar

    def get_panjang(self) -> float:
        return self._panjang
    
    def get_lebar(self) -> float:
        return self._lebar
    
    def keliling_bujur_sangkar(self) -> float:
        return self._panjang * 4
    
    def keliling_persegi_panjang(self) -> float:
        return 2 * (self._panjang + self._lebar)
    
    def luas_bujur_sangkar(self) -> float:
        return self._panjang * self._panjang
    
    def luas_persegi_panjang(self) -> float:
        return self._panjang * self._lebar