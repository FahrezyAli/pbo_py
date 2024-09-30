class Student:
    _roll_number : int

    def __init__(self, a : int = 0):
        self._roll_number = a

    def put_number(self):
        print(f"Roll Number : {self._roll_number}")

class Test(Student):
    _sub1 : float
    _sub2 : float

    def __init__(self, x : float, y : float, a : int = 0):
        super().__init__(a)
        self._sub1 = x
        self._sub2 = y

    def put_marks(self):
        print(f"Sub 1 : {self._sub1}")
        print(f"Sub 2 : {self._sub2}")
        
class Result(Test):
    _total : float

    def __init__(self, x: float, y: float, a: int = 0):
        super().__init__(x, y, a)
        self._total = x + y

    def get_sub1(self):
        return self._sub1
    
    def get_sub2(self):
        return self._sub2

    def display(self):
        self.put_number()
        self.put_marks()
        print(f"Total : {self._total}")

def main():
    ali = Result(75, 25)
    balqis = Result(50, 50, 1)

    ali.display()
    balqis.display()

if __name__ == "__main__":
    main()