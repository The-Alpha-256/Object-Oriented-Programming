from Truck import Truck
from Garage import Garage

class GarageTester:
    @staticmethod
    def get_example():
        truck = Truck("black", False)
        garage = Garage()
        garage.set_vehicle(truck)
        print(garage)

if __name__ == "__main__":
    GarageTester.get_example()
