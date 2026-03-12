class Vehicle:
    vehicle_id = 0
    brand = "" 
    price = 0
    def __init__(self,vid,b,p):
        self.vehicle_id = vid
        self.brand = b
        self.price = p
    def display_vehicle(self):
        print("ID:",self.vehicle_id)
        print("Brand:",self.brand)
        print("Price:",self.price)

class Car(Vehicle):
    num_doors = 0
    fuel_type = ""
    def __init__(self,vid,b,p,nd,ft):
        self.vehicle_id = vid
        self.brand = b
        self.price = p
        self.num_doors = nd
        self.fuel_type = ft
    
    def display_car_details(self):
        print("ID:",self.vehicle_id)
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Number of doors:",self.num_doors)
        print("Fuel:",self.fuel_type)
    
c1 = Car(100,"BMW",100000,4,"CNG")
c1.display_car_details()
c2 = Car(200,"Mercedes",200000,4,"Petrol")
c2.display_car_details()