from ParkedCar import ParkedCar
from ParkingMeter import ParkingMeter
from PoliceOfficer import PoliceOfficer

def run_scenario(car, meter, officer):
    ticket = officer.inspect_car(car, meter)
    if ticket:
        print(ticket)
    else:
        print(f"{car} is legally parked. No ticket issued.\n")

def scenario_1():
    print("Scenario 1: A Car is Parked Legally\n".center(83))
    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    officer = PoliceOfficer("John Doe", "5678")
    run_scenario(car, meter, officer)

def scenario_2():
    print("Scenario 2: A Car Is Parked Illegally (Less Than an Hour Over Time)\n".center(83))
    car = ParkedCar("Honda", "Accord", "Blue", "ABC987", 70)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("Jane Smith", "1234")
    run_scenario(car, meter, officer)

def scenario_3():
    print("Scenario 3: Car Parked Illegally (Multiple Hours Over Time)\n".center(83))
    car = ParkedCar("Ford", "Mustang", "Black", "LMN456", 190)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("James Brown", "4321")
    run_scenario(car, meter, officer)

def scenario_4():
    print("Scenario 4: Multiple Cars in a Parking Lot\n".center(83))
    cars = [
        (ParkedCar("Nissan", "Altima", "White", "JKL321", 60), ParkingMeter(60)), #Parked Legally
        (ParkedCar("Chevy", "Malibu", "Silver", "QWE789", 80), ParkingMeter(60)), #Parked Just Over the Limit
        (ParkedCar("BMW", "X5", "Black", "BMW999", 500), ParkingMeter(60)), #Parked Way Over the Limit
        (ParkedCar("Hyundai", "Elantra", "Gray", "HYU123", 45), ParkingMeter(60)), #Parked Legally
        (ParkedCar("Audi", "A4", "Blue", "AUD456", 65), ParkingMeter(60)) #Parked Just Over the Limit
    ]
    officer = PoliceOfficer("Sarah Green", "9999")
    for car, meter in cars:
        run_scenario(car, meter, officer)

if __name__ == "__main__":
    
    print("========= Parking Ticket System =========\n".center(83))
    scenario_1()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_2()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_3()
    print("\n-----------------------------------------------------------------------------------\n")
    scenario_4()

    car = ParkedCar("Toyota", "Camry", "Red", "XYZ123", 30)
    meter = ParkingMeter(40)
    officer = PoliceOfficer("John Doe", "5678")

    ticket = officer.inspect_car(car, meter)

    if ticket:
        print(ticket)
    else:
        pass  # No ticket issued