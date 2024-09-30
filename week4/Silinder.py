from math import pi

class Silinder:
    def volume(self, r : int | float, t : int | float = 0) -> float:
        return pi * r * t * t

def main():
    print(Silinder().volume(5))
    print(Silinder().volume(5, 10))

if __name__ == "__main__":
    main()