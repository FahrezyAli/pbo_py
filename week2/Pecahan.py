class Pecahan:

    _pembilang : int
    _penyebut : int

    def __init__(self, pembilang : int, penyebut : int):
        self._pembilang = pembilang
        self._penyebut = penyebut

    def get_pembilang(self) -> int:
        return self._pembilang