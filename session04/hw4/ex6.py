class string:
    def __init__(self):
        self.str = ""
    def get_str(self):
        self.str = input("Input string:")
    def print_str(self):
        x = self.str.upper()
        return x
string = string()
y = string.get_str()
x = string.print_str()
print (x)

