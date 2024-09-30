from __future__ import annotations

class Number:
    _value : int

    def __init__(self, value : int):
        self._value = value

    def __add__(self, other : Number) -> int:
        return self._value + other._value
    
    def __sub__(self, other : Number) -> int:
        return self._value - other._value
    
    def __truediv__(self, other : Number) -> float:
        return self._value / other._value
    
    def __mul__(self, other : Number) -> int:
        return self._value * other._value
    
    def __gt__(self, other : Number) -> bool:
        return self._value > other._value