class ParkedCar:
    def __init__(self, make: str, model: str, color: str, license_number: str, minutes_parked = 60):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self._minutes_parked = None
        self.minutes_parked = minutes_parked  # Use setter for validation

    @property
    def minutes_parked(self):
        return self._minutes_parked
    
    @minutes_parked.setter
    def minutes_parked(self, minutes):
        if minutes < 0:
            raise ValueError("Minutes parked cannot be negative.")
        self._minutes_parked = minutes
        
    def __str__(self):
        return f"{self.color} {self.make} {self.model}, License: {self.license_number}"