#This is the file ParkingMeter.py that defines the ParkingMeter class
class ParkingMeter:
    #This constructor initializes the ParkingMeter with minutes_purchased, defaulting to 60
    def __init__(self, minutes_purchased=60):
        self._minutes_purchased = 60
        self.minutes_purchased = minutes_purchased  # use setter

    #This is a property for minutes_purchased with a getter and setter to ensure the value is positive
    @property
    def minutes_purchased(self):
        return self._minutes_purchased

    #This is the setter for minutes_purchased that raises a ValueError if a non-positive value is provided
    @minutes_purchased.setter
    def minutes_purchased(self, value):
        if value <= 0:
            raise ValueError("Minutes purchased must be greater than 0.")
        self._minutes_purchased = value

