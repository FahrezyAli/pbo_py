class Sum:
    # menggunakan metode 'None'
    def sum(self, a : int, b : int, c : int = 0, d : int = 0) -> int:
        return a + b + c + d

def main():
    print(Sum().sum(1, 2))
    print(Sum().sum(1, 2, 3))
    print(Sum().sum(1, 2, 3, 4))

if __name__ == "__main__":
    main()