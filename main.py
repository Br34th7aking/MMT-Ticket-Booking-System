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
    username, password, userType = loginMenu.getLoginDetails()
    # if user exists, take him to homepage
    # else ask again
    loginOk = False
    if userType is '1' or userType is '2':
        data = json.load(open('customerData.json', 'r'))
    else:
        data = json.load(open('companyData.json', 'r'))
    while not loginOk:
        for user in data:
            if user['username'] == username and user['password'] == password:
                loginOk = True
                break
        if not loginOk:
            print('Invalid username or password. Try again.')
            loginMenu.display()
            username, password, userType = loginMenu.getLoginDetails()

    # this part of code is accessible after user is logged in


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
        file.close()
        data.append(customerDict)
        file = open("customerData.json", "w")
        json.dump(data, file)
        file.close()
    elif userType == '2':
        # create a new company and add to company database
        companyName = signUpData[0]
        password = signUpData[1]
        serviceType = signUpData[2]
        helpline = signUpData[3]
        memberSince = str(date.today())
        company = Company(companyName, password, serviceType, helpline, memberSince)
        companyDict = company.createDict()
        file = open("companyData.json", "r")
        data = json.load(file)
        file.close()
        data.append(companyDict)
        file = open("companyData.json", "w")
        json.dump(data, file)
        file.close()
elif userChoice is '3':
    # display the FAQ
    pass
