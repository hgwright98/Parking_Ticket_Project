from ParkingTicket import ParkingTicket

class PoliceOfficer:
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    def inspect_car(self, parked_car, parking_meter):
        over_time = parked_car.minutes_parked - parking_meter.minutes_purchased
        if over_time > 0:
            return ParkingTicket(parked_car, self.name, self.badge_number, over_time)
        else:
            return None