

class Auto:
    # class variable counter
    POCET_AUT = 0
    
    
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        # add to class variable counter
        Auto.POCET_AUT += 1
        

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        
        
    @classmethod
    def show_counter(cls):
        print(f"Pocet aut: {cls.POCET_AUT}")
        
    @staticmethod
    def show_info_static(name):
        print("This is static method" + name)
        
        
class Mercedes(Auto):
    POCET_MERCEDES = 0
    
    def __init__(self, brand, model, year, price, color):
        super().__init__(brand, model, year, price)
        self.color = color
        Mercedes.POCET_MERCEDES += 1 
        
        
mercedes = Mercedes("Mercedes", 'M5', 2020, 50000, 'black') 
nissan = Auto("Nissan", 'GTR', 2019, 60000)
# 20 dalsich aut

# zadefinovanu classu
#  TU
    # instanciu classu
    # instanciu classy


print(Auto.POCET_AUT)
print(Mercedes.POCET_MERCEDES)
Auto.show_counter()