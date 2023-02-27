class Car:

    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.is_busy = False
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat

    def __str__(self):
        return f'Car: (color = {self.color}, count_passenger_seats = {self.count_passenger_seats}, baby_seat = {self.is_baby_seat}, busy = {self.is_busy})'


WV = Car('red', 8, False)
BMW = Car('blue', 6, False)
BMW.is_busy = True
print(WV.__str__())
print(BMW.__str__())
