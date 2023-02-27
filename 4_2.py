class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.is_busy = False
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self):
        return f'Car: (color = {self.color}, count_passenger_seats = {self.count_passenger_seats}, baby_seat = {self.is_baby_seat}, busy = {self.is_busy})'


class Taxi:

    def __init__(self, list_car):
        self.lst = list_car

    def find_car(self, count_passenger_seats, is_baby_seat):
        for i in self.lst:
            if is_baby_seat:
                if i.is_baby_seat and not i.is_busy:
                    if i.count_passenger_seats > count_passenger_seats:
                        i.is_busy = True
                        return i
            else:
                if i.count_passenger_seats >= count_passenger_seats and not i.is_busy:
                    i.is_busy = True
                    return i


WV = Car('red', 4, False)
BMW = Car('blue', 5, False)
AUDI = Car('green', 5, True)
BUS = Car('yellow', 16, True)
BMW.is_busy = True
cars = [WV, BMW, AUDI, BUS]
taxi = Taxi(cars)
print(taxi.find_car(5, True))
print(taxi.find_car(8, False))
print(taxi.find_car(5, False))
