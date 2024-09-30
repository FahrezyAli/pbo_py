class Number:

    _num : int
    _positive : str
    _odd : str

    def __init__(self, num: int):
        self._num = num

        if num > 0:
            self._positive = "Positif"
        elif num == 0:
            self._positive = "Nol"
        else:
            self._positive = "Negatif"

        if num % 2 == 0:
            self._odd = "Genap"
        else:
            self._odd = "Ganjil"

    def get_number(self) -> int:
        return self._num

    def get_state(self) -> str:
        return f"{self._positive} {self._odd}"
    
def main():
    ten = Number(10)
    print(ten.get_number())

if __name__ == "__main__":
    main()