def add(*args):
    print(args[1])
    
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
    
calculate(2, add=3, multiply=5)


class car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = car(make="Nissan", model="Skyline")
print(my_car.model)