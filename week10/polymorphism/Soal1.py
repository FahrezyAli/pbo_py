from abc import ABC, abstractmethod
from typing_extensions import override

class Employee(ABC):
    __holiday_entitlement : bool
    __employee_name : str
    __employee_dept: str
    __length_of_service: int

    def __init__(self, name : str, dept : str, los : int, holidays : bool):
        self.__employee_name = name
        self.__employee_dept = dept
        self.__length_of_service = los
        self.__holiday_entitlement = holidays
    
    @abstractmethod
    def get_name(self) -> str:
        return self.__employee_name
    
    @abstractmethod
    def get_department(self) -> str:
        return self.__employee_dept
    
    @abstractmethod
    def get_length_of_service(self) -> int:
        return self.__length_of_service

    @abstractmethod
    def get_holidays(self) -> bool:
        return self.__holiday_entitlement

    def __str__(self) -> str:
        return f"Name : {self.__employee_name}\nDepartment : {self.__employee_dept}\nLength of Service : {self.__length_of_service}\nIs on Holidays? : {self.__holiday_entitlement}"

class Technician(Employee):
    __holidays : bool

    def __init__(self, name: str, dept: str, los: int, holidays: bool):
        super().__init__(name, dept, los, holidays)
        self.__holidays = holidays

    def get_name(self) -> str:
        return super().get_name()
    
    @override
    def get_department(self) -> str:
        return super().get_department()

    @override
    def get_length_of_service(self) -> int:
        return super().get_length_of_service()

    @override
    def get_holidays(self) -> bool:
        return self.__holidays

    @override
    def __str__(self) -> str:
        return f"Name : {self.get_name()}\nDepartment : {self.get_department()}\nLength of Service : {self.get_length_of_service()} Days\nIs on Holidays? : {self.get_holidays()}"

class Manager(Employee):
    __holidays : bool

    def __init__(self, name: str, dept: str, los: int, holidays: bool):
        super().__init__(name, dept, los, holidays)
        self.__holidays = holidays

    @override
    def get_name(self) -> str:
        return super().get_name()

    @override
    def get_department(self) -> str:
        return super().get_department()
    
    @override
    def get_length_of_service(self) -> int:
        return super().get_length_of_service()

    @override
    def get_holidays(self) -> bool:
        return self.__holidays

    @override
    def __str__(self) -> str:
        return f"Name : {self.get_name()}\nDepartment : {self.get_department()}\nLength of Service : {self.get_length_of_service()} Days\nIs on Holidays? : {self.get_holidays()}"

    
def main():
    ALDI = Technician("Aldi", "Dept. Mesin", 257, False)
    ALFIN = Manager("ALFIN", "Dept. Listrik", 356, True)

    print(ALDI, end="\n\n")
    print(ALFIN)
    

if __name__ == "__main__":
    main()