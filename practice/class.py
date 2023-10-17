class Friend:

    def __init__(self):
        self.name = 'Sanib'
        self.no = 7066967487
        self.status = 'fantastic'
        self.worth = 'disloyal'
    
    def way(self):
        return f'{self.name} is travelling to my house in {self.status} condition'


one = Friend()
print(f'name is :{one.name}')
print(f'number is :{one.no}')
print(f'worth is :{one.worth}')
print(one.way())


# ---------------------------------------------------------------
class car:

    def __init__ (self):
        print('Welcome to the Garage')
    
    def sport(self,name,model,speed):
        print("This is a Sport Car ",name,' Model-- ',model,' Speed-- ',speed)

    def sedan(self,name,model,speed):
        print("This is a Sedan ",name,' Model-- ',model,' Speed-- ',speed)

    def suv(self,name,model,speed):
        print("This is a SUV ",name,' Model-- ',model,' Speed-- ',speed)

class truck(car):

    def truckSport(self,name,model,speed):
        print("This is a Monster Sport ",name,' Model-- ',model,' Speed-- ',speed)

    def truckSedan(self,name,model,speed):
        print("This is a sedan truck ",name,' Model-- ',model,' Speed-- ',speed)


gaadi = truck()
gaadi.sport('ferrari',784,'230km')
gaadi.truckSedan('monsters','xxys',543)
