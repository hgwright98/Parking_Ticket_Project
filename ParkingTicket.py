import math

class ParkingTicket:
    def __init__(self, car, officer_name, badge_number, illegal_minutes):
        self.car = car
        self.officer_name = officer_name
        self.badge_number = badge_number
        self.illegal_minutes = illegal_minutes
        self.fine = self.calculate_fine()

    def calculate_fine(self):
        hours = math.ceil(self.illegal_minutes / 60)
        if hours <= 1:
            return 25.00
        else:
            return 25.00 + (hours - 1) * 10.00

    def __str__(self):
        return (
            f"{'--- Parking Ticket ---':^83}\n"
            f"Car: {self.car}\n"
            f"Illegally Parked For: {self.illegal_minutes} minutes\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Issued By: Officer {self.officer_name}, Badge #{self.badge_number}\n"
        )

