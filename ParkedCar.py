# This is the file ParkedCar.py that defines the ParkedCar class
class ParkedCar:
    # The constructor initializes the car's attributes where make, model, color, and license_number are strings, and minutes_parked is an integer with a default value of 60
    def __init__(self, make: str, model: str, color: str, license_number: str, minutes_parked = 60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = None # Private attribute to store minutes parked
        self.minutes_parked = minutes_parked  # This uses the setter to validate and set the value

    #This is a property for minutes_parked with a getter and setter to ensure the value is non-negative
    @property
    def minutes_parked(self):
        return self._minutes_parked
    
    #This is the setter for minutes_parked that raises a ValueError if a negative value is provided
    @minutes_parked.setter
    def minutes_parked(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes parked cannot be negative.")
        self._minutes_parked = minutes
    
    #This method returns a string representation of the ParkedCar object
    def __str__(self):
        return f"{self.color} {self.make} {self.model}, License: {self.license_number}"