class Auto:
    def __init__(self, model, rang, karobka, narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.km = 0
    
    def get_info(self):
        return f"{self.rang.title()} {self.model.title()}. {self.karobka.title()} karobka. Narxi {self.narx}$"
    
    def get_model(self):
       return self.model

    def get_color(self):
       return self.rang

    def get_type(self):
       return self.karobka

    def get_price(self):
       return self.narx

class Avtosalon:
    def __init__(self, nom):
        self.nom = nom
        self.cars = []
        self.number_of_cars = 0
    
    def add_car(self, car):
        self.cars.append(car)
        self.number_of_cars +=1

    def set_km(self,km):
        self.km = km
        
    def get_cars(self):
        return [car.get_info() for car in self.cars]

salon1 = Avtosalon('Shumaxer')

car1= Auto('tesla', 'oq', 'avtomat', 35000)
car2 = Auto('volvo', 'qora', 'avtomat', 45000)

salon1.add_car(car1)
salon1.add_car(car2)

cars_in_salon = salon1.get_cars()
print(cars_in_salon)