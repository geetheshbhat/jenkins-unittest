from math import log10


def surface_area(x: int, y: int):

    if not isinstance(x,(int, float)) and not isinstance(y,(int, float)):
        raise TypeError("The number can be only int or float")
    if isinstance(x,bool) and isinstance(y,bool):
        raise TypeError("The number can be only int or float")
    if x <= 0 or y <=0:
        raise ValueError("Variable value must be greater than zero")
    if (int(log10(x))+1) > 3 or (int(log10(y))+1) > 3:
        raise ValueError("Only 2 decimal places allowed")
    else:
        return x*y
