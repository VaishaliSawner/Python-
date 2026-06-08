class Airplane:
    def __init__(self, flight_no, destination, departure_time):
        self.flight_no = flight_no
        self.destination = destination
        self.departure_time = departure_time
        self.status = "On Time"

    def check_status(self):
        print(f"Flight {self.flight_no} is {self.status}")

    def delay(self, minutes):
        self.status = f"Delayed by {minutes} minutes"


plane = Airplane("AI101", "Delhi", "10:00 AM")

plane.check_status()
plane.delay(30)
plane.check_status()