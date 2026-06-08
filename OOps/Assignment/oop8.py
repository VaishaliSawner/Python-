class TrafficLight:
    def __init__(self, color, duration):
        self.color = color
        self.duration = duration

    def change_color(self, new_color):
        self.color = new_color

    def check(self):
        if self.color == "red":
            print("STOP")
        elif self.color == "green":
            print("GO")
        else:
            print("WAIT")


t = TrafficLight("red", 30)
t.check()

t.change_color("green")
t.check()