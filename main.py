# this is the main file of the program
# author: abhijit raj

from Menus import *
from users import *
from miscellaneous import *
from datetime import date
username = '' # no logged user
password = ''

startMenu = MainMenu()

startMenu.display()

userChoice = startMenu.getUserChoice()

while userChoice is not '1' and userChoice is not '2' and userChoice is not '3':
    userChoice = input('Invalid choice. Please enter 1, 2, or 3: ')
if userChoice is '1':
    # user wants to log in
    loginMenu = Login()
    loginMenu.display()
    username, password = loginMenu.getLoginDetails()

elif userChoice is '2':
    # user wants to register a new account
    registerMenu = Register()
    registerMenu.display()
    userType, signUpData = registerMenu.signUp()
    if userType == '1':
        #create a new customer and add to customer database
        username = signUpData[0]
        email = signUpData[1]
        password = signUpData[2]
        gender = signUpData[3]
        phone = signUpData[4]
        memberSince = str(date.today())
        customer = Customer(username, email, password, gender, phone, memberSince)
        customerDict = customer.createDict()
        file = open("customerData.json", "r")
        data = json.load(file)
        data.append(customerDict)
        file = open("customerData.json", "w")
        json.dump(data, file)
    elif userType == '2':
        # create a new company and add to company database
        pass
elif userChoice is '3':
    # display the FAQ
    pass
