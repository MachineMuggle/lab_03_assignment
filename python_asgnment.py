import time 
class Flight:
    def __init__(self,id,fr,to,price):
        self.id = id
        self.fr = fr
        self.to = to
        self.price = price
    def show_deets(self):
        print(f"{self.id}---{self.fr}---{self.to}---{self.price}")
flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ()
    ]
flights = []
flights.append(Flight("AI161E90", "BLR", "BOM", 5600))
flights.append(Flight("BR161F91", "BOM", "BBI", 6750))
flights.append(Flight("AI161F99", "BBI", "BLR", 8210))
flights.append(Flight("VS171E20", "JLR", "BBI", 5500))
flights.append(Flight("AS171G30", "HYD", "JLR", 4400))
flights.append(Flight("AI131F49", "HYD", "BOM", 3499))

while True:
    print("1. Search Flights\n2. Exit")
    ch = int(input("Enter choice: "))
    if(ch==1):
        print("1. Search flights to a city?\n2. Search flights from a city?\n3. Search flights between two cities?")
        ch2 = int(input("Enter choice: "))
        if (ch2==1):
            ch3 = input("Enter name of city: ")
            for flight in flights:
                if (flight.to == ch3):
                    time.sleep(0.5)
                    flight.show_deets()
        elif(ch2==2):
            ch3 = input("Enter name of city: ")
            for flight in flights:
                if (flight.fr == ch3):
                    time.sleep(0.5)
                    flight.show_deets()
        elif(ch2==3):
            ch3 = input("Enter name of destination: ")
            ch4 = input("Enter name your city: ")
            for flight in flights:
                if ((flight.to == ch3) and (flight.fr == ch4)):
                    time.sleep(0.5)
                    flight.show_deets()
        time.sleep(1)
    elif(ch==2):
        break
