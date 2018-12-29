from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    car2 = SilverServiceTaxi("Car 2", 100, 5, 2)
    car2.drive(40)
    print(car2)
    print(car2.get_fare())


main()