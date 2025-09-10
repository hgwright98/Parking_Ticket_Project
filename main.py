from ParkedCar import ParkedCar # This imports the ParkedCar class from ParkedCar.py
from ParkingMeter import ParkingMeter # This imports the ParkingMeter class from ParkingMeter.py
from PoliceOfficer import PoliceOfficer # This imports the PoliceOfficer class from PoliceOfficer.py

#This function will be called by each scenario function to run each scenario
#You need to pass in a ParkedCar object(car), ParkingMeter object(meter), and PoliceOfficer object(officer)
def run_scenario(car, meter, officer):
    # Call the inspect_car method of the PoliceOfficer object
    ticket = officer.inspect_car(car, meter)
    # This checks if a ticket was issued and prints the appropriate message
    if ticket:
        print(ticket)
    else:
        print(f"{car} is legally parked. No ticket issued.\n")

#This function sets up and runs Scenario 1
def scenario_1():
    #This prints the scenario title centered within 83 characters
    print("Scenario 1: A Car is Parked Legally\n".center(83))
    # Create instances of ParkedCar, ParkingMeter, and PoliceOfficer for the scenario
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    officer = PoliceOfficer("John Doe", "5678")
    # Call the run_scenario function above with the created objects in this scenario
    run_scenario(car, meter, officer)

#This function sets up and runs Scenario 2
def scenario_2():
    #This prints the scenario title centered within 83 characters
    print("Scenario 2: A Car Is Parked Illegally (Less Than an Hour Over Time)\n".center(83))
    # Create instances of ParkedCar, ParkingMeter, and PoliceOfficer for the scenario
    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Jane Smith", "1234")
    # Call the run_scenario function above with the created objects in this scenario
    run_scenario(car, meter, officer)

#This function sets up and runs Scenario 3
def scenario_3():
    #This prints the scenario title centered within 83 characters
    print("Scenario 3: Car Parked Illegally (Multiple Hours Over Time)\n".center(83))
    # Create instances of ParkedCar, ParkingMeter, and PoliceOfficer for the scenario
    car = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("James Brown", "4321")
    # Call the run_scenario function above with the created objects in this scenario
    run_scenario(car, meter, officer)

#This function sets up and runs Scenario 4
def scenario_4():
    #This prints the scenario title centered within 83 characters
    print("Scenario 4: Multiple Cars in a Parking Lot\n".center(83))
        # Create multiple ParkedCar and ParkingMeter instances, and a single PoliceOfficer instance
    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)), #Parked Legally
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)), #Parked Just Over the Limit
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)), #Parked Way Over the Limit
        (ParkedCar("Hyundai", "Elantra", "Gray", "HYU123", 45), ParkingMeter(60)), #Parked Legally
        (ParkedCar("Audi", "A4", "Blue", "AUD456", 65), ParkingMeter(60)) #Parked Just Over the Limit
    ]
    officer = PoliceOfficer("Sarah Green", "9999")
    # This loop through each car and meter pair and call the run_scenario function
    for car, meter in cars:
        run_scenario(car, meter, officer)

# This is the main entry point of the program where the if __name__ == "__main__": block allows the script to be run directly
if __name__ == "__main__":
    # This prints the main title centered within 83 characters
    print("========= Parking Ticket System =========\n".center(83))
    # This calls each scenario function to run the scenarios
    scenario_1()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_2()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_3()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_4()
    print("\n-----------------------------------------------------------------------------------\n")