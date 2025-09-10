#This is the file ParkingTicket.py that defines the ParkingTicket class
#This imports the math module to use the ceil function for rounding up
import math

class ParkingTicket:
    #This constructor initializes the ParkingTicket with car, officer_name, badge_number, and illegal_minutes
    def __init__(self, car, officer_name, badge_number, illegal_minutes):
        self.car = car
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    #This method calculates the fine based on the number of illegal minutes parked
    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes / 60)
        # Fine structure: $25 for the first hour or part of an hour, plus $10 for each additional hour or part of an hour
        if hours <= 1:
            return 25.00
        else:
            return 25.00 + (hours - 1) * 10.00
        
    #This method returns a string representation of the ParkingTicket object based on the attributes of th above class
    def __str__(self):
        return (
            f"{'--- Parking Ticket ---':^83}\n"
            f"Car: {self.car}\n"
            f"Illegally Parked For: {self.illegal_minutes} minutes\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Issued By: Officer {self.officer_name}, Badge #{self.badge_number}\n"
        )

