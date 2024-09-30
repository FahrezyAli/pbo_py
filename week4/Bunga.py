class Bunga:
    def bunga(self, m0 : int, r : int | float, n : int) -> int:
        return int(m0 * pow((1 + r), n))

def main():
    print(Bunga().bunga(1, 2, 3))
    print(Bunga().bunga(1, 2.5, 3))

if __name__ == "__main__":
    main()