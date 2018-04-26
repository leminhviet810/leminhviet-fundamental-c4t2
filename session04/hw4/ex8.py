class Car:
    def __init__(self):
        self.brand = ""
    def set_Brand(self):
        self.brand = input("Brand?")
    def set_Max_Speed(self):
        self.ms = input("Max speed?")
    def print_Data(self):
        print(self.brand, "with", self.ms, 'km/h')
a = Car()
a.set_Brand()
a.set_Max_Speed()
a.print_Data()