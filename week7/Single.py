class B:
    _a : float
    _b : float

    def __init__(self, a : float, b : float):
        self.a = a
        self.b = b
    
    def get_a(self):
        return self.a
    
    def get_b(self):
        return self.b
    
    def show_a(self):
        print(f"Nilai a: {self.a}")

    def show_b(self):
        print(f"Nilai b: {self.b}")

class D(B):

    def __init__(self, a: float, b: float):
        super().__init__(a, b)

    def mul(self):
        return self.b * self.a
    
    def dev(self):
        return self.b / self.a

    def display(self):
        self.show_a()
        self.show_b()
        print(f"Nilai c: {self.mul()}")
        print(f"Nilai d: {self.dev()}")

def main():
    test = D(5, 6)
    test.display()

if __name__ == "__main__":
    main()