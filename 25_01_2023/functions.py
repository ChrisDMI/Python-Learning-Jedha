'''
Créons une classe voiture
'''

class Voiture: 
    wheels = 4
    energy = 'oil'
    nb_door = 4
    nb_place = 4
    
    def __init__(self, brand:str, model:str, distance:float, control:bool):
        self.brand = brand
        self.model = model
        self.distance = distance
        self.control = control
    

    def passenger(self, driver:str, copilot:str=None, passenger_1:str=None, passenger_2:str=None):
        self.driver = driver
        self.copilot = copilot
        self.passenger_1 = passenger_1
        self.passenger_2 = passenger_2






    def tentatative_restante(self, tentative:int):
        tentative -= 1
        print('Tentatives restantes : {} '.format(tentative))
        return tentative



    def input_code_pin_user(self, password:str='0000'):
        mot_de_passe = input('Enter your password:')

        tentative = 3

        

        while mot_de_passe != password:
            self.tentatative_restante(tentative)
            tentative -=1
            if mot_de_passe == 'exit':
                return False

            try: 
                int(mot_de_passe)
                print('You have a wrong password !')
                mot_de_passe = input('Enter your password : ')
                
            except:
                print('Please enter only alpha numeric caracter')
                mot_de_passe = input('Enter your password : ')
        
        if mot_de_passe == password: 
            print('You have the right password !')
            return True
        else:
            print('Connection denied')
            return False





    def driving(self, start:str, final:str, miles:float):

        try:
            self.driver
            if self.input_code_pin_user():
                self.distance += miles
                print("I'am driving : ", True)
            else:
                print('You can not drive this car')

            if self.distance > 5000:
                self.control = False
            
        except:
            print('There is no driver')

            

        
def input_code_pin_user(password:str='0000') -> bool:
    input_user = input('Please enter your password')

    tentative = 3

    while input_user != password and tentative > 0:

        if input_user == 'exit':
            return False

        tentative -=1
        print('Tentatives restantes : {}'.format(tentative))

        try:
            int(input_user)
            print('Wrong Password')
            input_user = input('Please enter your password')
            
        except:
            print('Wrong input, please entre numbers')
            input_user = input('Please enter your password')

    if input_user == password:
        print('Successful connection')
        return True
    else:
        print('Connexion denied')
        return False