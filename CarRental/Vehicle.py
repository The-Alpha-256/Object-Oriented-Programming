class Vehicle:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"This vehicle is {self.color}"
