from datetime import datetime
class Car:
    def __init__(self, year = None):
        self.creation_date = datetime.now() # 
        # self.manufacturer = 

    def turn_on(self):
        return self.year + 'vroom'


older_car = Car(1990)
new_car = Car(2010)

# Factory -> class creates new instances 
# Blueprint -> define the functionality of those instances