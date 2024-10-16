from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, trailer=False):
        super().__init__(color)
        self.trailer = trailer

    def has_trailer(self):
        return self.trailer

    def __str__(self):
        return f"{super().__str__()}
has trailer: {self.trailer}"
