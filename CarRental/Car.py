from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, winter_tires=False):
        super().__init__(color)
        self.winter_tires = winter_tires

    def has_winter_tires(self):
        return self.winter_tires

    def __str__(self):
        return f"{super().__str__()}
has winter tires: {self.winter_tires}"
