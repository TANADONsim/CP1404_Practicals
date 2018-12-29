"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel, price_per_km)
        self.price_per_km = price_per_km * fanciness
        self.current_fare_distance = 0
        self.flagfall = 4.50

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = self.price_per_km * self.current_fare_distance + self.flagfall
        return fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0
