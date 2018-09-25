# this file contains the code for app menus
from abc import ABC, abstractmethod
import json
from logos import LOGOS
#logos = json.load(open("logos.json", 'r'))

# an abstract menu class
class Menu(ABC):
    @abstractmethod
    def display(self):
        pass

# the main menu
class MainMenu(Menu):
    def display(self):
        print(LOGOS["mainmenu"])
        print(" " * 30 + "Your #1 Travel Website")
        print('*' * 100)
        print('Choose one of the following: ')
        print('1 to login')
        print('2 to register')
        print('3 to read FAQ')

        self.getUserChoice()

    def getUserChoice(self):
        validChoice = False
        while( not validChoice):

            userChoice = input('Your choice: ')

            if userChoice is '1':
                validChoice = True
                login = Login()
                login.display()
            elif userChoice is '2':
                validChoice = True
                register = Register()
                register.display()
            elif userChoice is '3':
                validChoice = True
                pass
            else:
                # invalid input
                print("Sorry! That's not a valid input. Try again")

# the login menu
class Login(Menu):
    def display(self):


# the register menu
class Register(Menu):
    def display(self):
        pass


#test
m = MainMenu()
m.display()
