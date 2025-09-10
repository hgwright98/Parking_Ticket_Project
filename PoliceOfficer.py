#This is the file PoliceOfficer.py that defines the PoliceOfficer class
#This imports the ParkingTicket class from ParkingTicket.py
from ParkingTicket import ParkingTicket

class PoliceOfficer:
    #This constructor initializes the PoliceOfficer with name and badge_number
    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    #This method inspects a parked car against a parking meter and issues a ticket if the car is parked illegally using the ParkingTicket class
    def inspect_car(self, parked_car, parking_meter):
        #This calculates the number of minutes the car is parked over the purchased time and issues a ticket if necessary
        over_time = parked_car.minutes_parked - parking_meter.minutes_purchased
        if over_time > 0:
            return ParkingTicket(parked_car, self.name, self.badge_number, over_time)
        else:
            return None