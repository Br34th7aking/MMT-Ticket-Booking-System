# this file contains the code for app menus
from abc import ABC, abstractmethod
import json
from logos import LOGOS


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
        userChoice = input('Enter your choice: ')
        return userChoice

# the login menu
class Login(Menu):
    def display(self):
        print(LOGOS["login"])
        print('*' * 100)
        self.getLoginDetails()
    def getLoginDetails(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        return username, password

# the register menu
class Register(Menu):
    def display(self):
        print(LOGOS["register"])
        print("*" * 100)
        self.signUp()

    def checkExistingRecord(self, property, val, userType):
        # checks if user with property already exists
        # returns true if user with property exists
        # property can be email or username
        if userType is '1':
            # check in customer database
            data = json.load(open('customerData.json', 'r'))
            if not data:
                return False # there is no record
            for user in data:
                if (user[property] == val):
                    return True
            return False
        else:
            # check in company database
            data = json.load(open('companyData.json', 'r'))
            if not data:
                return False
            for company in data:
                if (company[property] == val):
                    return True
            return False

    def isValidPhoneNumber(self, phone):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in phone:
            if (i not in digits):
                return False
        if len(phone) is not 10:
            return False

        return True

    def registerCustomer(self):
        #helper function for signUp
        # returns all the valid input data
        username = input('Enter your username: ')
        # check no such user exists
        while (self.checkExistingRecord("username", username, '1')):
            username = input('Sorry, that username is taken. Please enter another: ')

        email = input('Enter your email: ')
        # check if email is unique
        while self.checkExistingRecord("email", email, '1'):
            email = input('Sorry, that email is already registered. Please enter another: ')

        password = input('Enter your password(minimum 6 characters): ')
        while(len(password) < 6):
            password = input('Weak password. Enter minimum 6 characters: ')

        gender = input('Enter your gender. 1 for male, 2 for female: ')
        while(gender is not '1' and gender is not '2'):
            gender = input('Invalid input. Please enter 1 for male, 2 for female: ')

        phone = input('Enter your 10-digit phone number: ')
        while not self.isValidPhoneNumber(phone):
            phone = input('Enter a valid phone number: ')

        return username, email, password, gender, phone

    def registerCompany(self):
        companyName = input('Enter the name of your company: ').upper()
        while self.checkExistingRecord("companyName", companyName, '2'):
            companyName = input('Sorry, that company is already registered in the system. Try another: ').upper()

        serviceType = input('What travel services do you offer? 1 for air, 2 for bus: ')
        while(serviceType is not '1' and serviceType is not '2'):
            serviceType = input('Invalid input. Please enter 1 for air, 2 for bus: ')

        helpline = input('Enter your 10-digit helpline number: ')
        while not self.isValidPhoneNumber(helpline):
            helpline = input('Enter a valid phone number: ')

        return companyName, serviceType, helpline

    def signUp(self):
        userType = input('Enter 1 for customer, 2 for company: ')
        while (userType is not '1' and userType is not '2'):
            userType = input('That is not a valid user type. Please enter 1 or 2')

        if (userType == '1'):
            # customer
            newCustomerDetails = self.registerCustomer()
            return newCustomerDetails
        elif (userType == '2'):
            # company
            newCompanyDetails = self.registerCompany()
            return newCompanyDetails



#test
# m = MainMenu()
# m.display()
# l = Login()
# l.display()
# r = Register()
# r.display()
