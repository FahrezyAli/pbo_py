from Cast import cast

class Vehicle:

    def start(self):
        print("Vehicle start code")

    def stop(self):
        print("Vehicle stop code")

class Car(Vehicle):

    __nb_of_seats : int

    def start(self):
        print("Car start code")

    def set_nb_of_seats(self, nb_of_seats : int):
        self.__nb_of_seats = nb_of_seats

    def get_nb_of_seats(self) -> int:
        return self.__nb_of_seats
    
def main():
    car1 = Car()
    car1.set_nb_of_seats(6)
    print(f"Seats : {car1.get_nb_of_seats()}")
    car1.start()
    car1.stop()
    print()

    vehicle1 = cast(car1, Vehicle)
    vehicle1.start() # type: ignore
    vehicle1.stop() # type: ignore
    print()

    car2 = cast(vehicle1, Car)
    car2.set_nb_of_seats(7) # type: ignore
    print(f"Seats : {car2.get_nb_of_seats()}") # type: ignore
    car2.start() # type: ignore
    car2.stop() # type: ignore
    print()

if __name__ == "__main__":
    main()


