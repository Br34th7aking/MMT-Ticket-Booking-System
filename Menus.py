# this file contains the code for app menus
# author: abhijit raj

from abc import ABC, abstractmethod
import json
from logos import LOGOS


class Menu(ABC):
    '''
    This is an abstract menu class that other menus will inherit from.
    '''
    @abstractmethod
    def display(self):
        pass

class MainMenu(Menu):
    '''
    Main Menu will be visible when the user starts the app
    '''
    def display(self):
        print(LOGOS["mainmenu"])
        print(" " * 30 + "Your #1 Travel Website")
        print('*' * 100)
        print('Choose one of the following: ')
        print('1 to login')
        print('2 to register')
        print('3 to read FAQ')

    def getUserChoice(self):
        '''
        returns the action taken by the user
        '''
        userChoice = input('Enter your choice: ')
        return userChoice

# the login menu
class Login(Menu):

    def display(self):
        print(LOGOS["login"])
        print('*' * 100)

    def getLoginDetails(self):
        '''Takes the username and password inputs and returns them '''
        userType = input('Enter 1 for customer, 2 for company, 3 for admin: ')
        while userType is not '1' and userType is not '2' and userType is not '3':
            userType = input('Please select valid user type. 1 for customer, 2 for company, 3 for admin: ')
        username = input('Enter your username: ')
        password = input('Enter your password: ')

        return username, password, userType


class Register(Menu):
    '''
    This class displays the register menu for the user.
    Two types of users can register from this menu:
    1 - customer who can book tickets on our platform
    2 - companies who will provide services (either air or bus. rail services are fixed)
    '''
    def display(self):
        print(LOGOS["register"])
        print("*" * 100)

    def checkExistingRecord(self, property, val, userType):
        '''
        checks if a user with given property already exists.
        returns True when such a user is found.
        '''

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
        '''
        returns True if the phone number entered is valid
        '''
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in phone:
            if (i not in digits):
                return False
        if len(phone) is not 10:
            return False

        return True

    def registerCustomer(self):
        '''
        Helper function for signUp function.
        Used to input and validate data from a new customer.
        returns a tuple containing all the valid customer data.
        '''
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
        if gender is '1':
            gender = 'M'
        elif gender is '2':
            gender = 'F'

        phone = input('Enter your 10-digit phone number: ')
        while not self.isValidPhoneNumber(phone):
            phone = input('Enter a valid phone number: ')

        return username, email, password, gender, phone

    def registerCompany(self):
        '''
        Helper function for signUp function.
        Used to input and validate data from a new company.
        returns a tuple containing all the valid company data.
        '''
        companyName = input('Enter the name of your company: ').upper()
        while self.checkExistingRecord("companyName", companyName, '2'):
            companyName = input('Sorry, that company is already registered in the system. Try another: ').upper()

        password = input('Enter your password(minimum 6 characters): ')
        while(len(password) < 6):
            password = input('Weak password. Enter minimum 6 characters: ')

        serviceType = input('What travel services do you offer? 1 for air, 2 for bus: ')
        while(serviceType is not '1' and serviceType is not '2'):
            serviceType = input('Invalid input. Please enter 1 for air, 2 for bus: ')
        if (serviceType is '1'):
            serviceType = 'AIR'
        elif serviceType is '2':
            serviceType = 'BUS'
        else:
            serviceType = 'RAIL' # this is fixed for IRCTC only

        helpline = input('Enter your 10-digit helpline number: ')
        while not self.isValidPhoneNumber(helpline):
            helpline = input('Enter a valid phone number: ')

        return companyName, password, serviceType, helpline

    def signUp(self):
        userType = input('Enter 1 for customer, 2 for company: ')
        while (userType is not '1' and userType is not '2'):
            userType = input('That is not a valid user type. Please enter 1 or 2')

        if (userType == '1'):
            # customer
            newCustomerDetails = self.registerCustomer()
            return userType, newCustomerDetails
        elif (userType == '2'):
            # company
            newCompanyDetails = self.registerCompany()
            return userType, newCompanyDetails


class CustomerDashboard(Menu):
    '''displayed to a customer after they login'''
    def display(self, username):
        print(LOGOS['home'])
        print('*' * 10 + "Customer Dashboard" + '*' * 10)
        print('\n')
        print('Hello {}, select one option from below: '.format(username))
        print('Enter 1 to book a flight.')
        print('Enter 2 to book a train ticket.')
        print('Enter 3 to book a bus ticket.')
        print('Enter 4 to view your profile. ')
        print('Enter 5 to change password.')
        print('Enter 6 to view booking history.')
        print('Enter 7 to view cancelled tickets. ')
        print('Enter 8 to cancel a ticket.')
        print('Enter 9 to view last transaction.')
        print('Enter 10 to view upcoming journeys.')
        print('Enter 11 to log out.')

    def getUserChoice(self):
        userChoice = input('Your choice: ')
        return userChoice

class CompanyDashboard(Menu):
    '''displayed to a company after they login'''
    def display(self):
        print(LOGOS['home'])
        print("*" * 50)
        print("Enter 1 to view your profile. ")
        print("Enter 2 to add coupons. ")
        print("Enter 3 to view coupons you currently offer. ")
        print("Enter 4 to remove a coupon. ")
        print("Enter 5 to log out. ")
    def getUserChoice(self):
        userChoice = input('Your choice: ')
        return userChoice
class AdminDashboard(Menu):
    '''displayed to the admin after they login'''
    def display(self):
        pass
#test
# m = MainMenu()
# m.display()
# l = Login()
# l.display()
# r = Register()
# r.display()
