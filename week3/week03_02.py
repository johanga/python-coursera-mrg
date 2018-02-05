import csv
import os.path

TYPE_CAR = 'car'
TYPE_TRUCK = 'truck'
TYPE_SPEC_MACHINE = 'spec_machine'

class BaseCar:
    def __init__(self, car_type):
        self.car_type = car_type
        self.photo_file_name = ''
        self.brand = ''
        self.carrying = 0.0
        
    def set_photo_file_name(self, filename):
        self.photo_file_name = filename
    def set_brand(self, brand):
        self.brand = brand
    def set_carrying(self, carrying):
        self.carrying = float(carrying)
       
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

class Car(BaseCar):
    def __init__(self):
        super().__init__(TYPE_CAR)
        self.passenger_seats_count = 0
    
    def set_passenger_seats_count(self, count):
        self.passenger_seats_count = int(count)

class Truck(BaseCar):
    def __init__(self):
        super().__init__(TYPE_TRUCK)
        self.body_width = 0.0
        self.body_height = 0.0
        self.body_length = 0.0
    
    def set_body_width(self, width):
        self.body_width = float(width)
    def set_body_height(self, height):
        self.body_height = float(height)
    def set_body_length(self, length):
        self.body_length = float(length)
        
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length
        
class SpecMachine(BaseCar):
    def __init__(self):
        super().__init__(TYPE_SPEC_MACHINE)
        self.extra = ''
        
    def set_extra(self, extra):
        self.extra = extra

def parse_row(row):
    if len(row) is not 7:
        return None
    
    car = None
    if row[0] == TYPE_CAR:
        car = Car()
        car.set_passenger_seats_count(row[2])
    elif row[0] == TYPE_TRUCK:
        car = Truck()
        try:
            w, h, l = row[4].split('x')
            car.set_body_width(w)
            car.set_body_height(h)
            car.set_body_length(l)
        except ValueError:
            pass
    elif row[0] == TYPE_SPEC_MACHINE:
        car = SpecMachine()
        car.set_extra(row[6])
    else:
        return None
        
    car.set_brand(row[1])
    car.set_photo_file_name(row[3])
    car.set_carrying(row[5])
    return car
        
def get_car_list(filename):
    cars = list()
    with open(filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader) # skip csv header
        for row in reader:
            car = parse_row(row)
            if car is not None:
                cars.append(car)
                
    return cars
