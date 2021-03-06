# this is the main file of the program
# author: abhijit raj

from Menus import *
from users import *
from miscellaneous import *
from datetime import date

username = '' # no logged user
password = ''

startMenu = MainMenu()


systemRunning = True
while systemRunning:
    startMenu.display()

    userChoice = startMenu.getUserChoice()
    userChoices = ['1', '2', '3', '4']
    while userChoice not in userChoices:
        userChoice = input('Invalid choice. Please enter 1, 2, 3 or 4: ')
    if userChoice is '1':
        # user wants to log in
        loginMenu = Login()
        loginMenu.display()
        username, password, userType = loginMenu.getLoginDetails()
        # if user exists, take him to homepage
        # else ask again
        loginOk = False
        currentUserDict = {}
        if userType is '1' or userType is '3':
            data = json.load(open('customerData.json', 'r'))
            userId = 'username'
        else:
            data = json.load(open('companyData.json', 'r'))
            userId = 'companyName'
        while not loginOk:
            for user in data:
                if user[userId] == username and user['password'] == password:
                    loginOk = True
                    currentUserDict = user
                    break
            if not loginOk:
                print('Invalid username or password. Try again.')
                loginMenu.display()
                username, password, userType = loginMenu.getLoginDetails()
        # this part of code is accessible after user is logged in
        if userType is '1':
            # open customer dashboard
            #seed data from file into the object
            currentUser = Customer(currentUserDict['username'], currentUserDict['email'], \
            currentUserDict['password'], currentUserDict['gender'], currentUserDict['phone'], currentUserDict['memberSince'])
            currentUser.setBookingHistory(currentUserDict['bookingHistory'])
            currentUser.setCancellationHistory(currentUserDict['cancellationHistory'])
            currentUser.setLastTransaction(currentUserDict['lastTransaction'])

            dashboard = CustomerDashboard()

            choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

            loggedIn = True
            while(loggedIn):

                dashboard.display(username)
                choice = dashboard.getUserChoice()
                while choice not in choices:
                    print('Sorry! Enter a valid option(1 to 10).')
                    choice = dashboard.getUserChoice()
                if choice == '11':
                    username = ''
                    password = ''
                    print(LOGOS['mainmenu'])
                    print("*" * 50)
                    print('Thank you for using MMT. You have been logged out')
                    loggedIn = False
                elif choice == '10':
                    currentUser.viewUpcomingJourneys()
                    goback = input('Press Enter to go back...')
                elif choice is '9':
                    currentUser.viewLastTransaction()
                    goback = input('Press Enter to go back...')
                elif choice is '8':
                    currentUser.cancelTicket()
                    goback = input('Press Enter to go back...')
                elif choice is '7':
                    currentUser.viewCancellationHistory()
                    goback = input('Press Enter to go back...')
                elif choice is '6':
                    currentUser.viewBookingHistory()
                    goback = input('Press Enter to go back...')
                elif choice is '5':
                    currentUser.changePassword()
                    file = open('customerData.json', 'r')
                    data = json.load(file)
                    file.close()
                    for user in data:
                        if user['username'] == currentUser.username:
                            user['password'] = currentUser.password
                            break
                    file = open('customerData.json', 'w')
                    json.dump(data, file)
                    file.close()
                    goback = input('Press any key to go back...')
                elif choice is '4':
                    currentUser.viewProfile()
                    goback = input('Press Enter to go back...')
                elif choice is '3':
                    currentUser.bookBusTicket()
                    goback = input('Press Enter to go back...')
                elif choice is '2':
                    currentUser.bookTrainTicket()
                    goback = input('Press Enter to go back...')
                elif choice is '1':
                    currentUser.bookFlight()
                    goback = input('Press Enter to go back...')


        elif userType is '2':
            # open company dashboard
            # take the data of current company
            currentUser = Company(currentUserDict['companyName'], currentUserDict['password'], \
            currentUserDict['serviceType'], currentUserDict['helpline'], currentUserDict['memberSince'])
            currentUser.setCoupons(currentUserDict['discountCoupons'])

            dashboard = CompanyDashboard()
            choices = ['1', '2', '3', '4', '5']
            loggedIn = True
            while loggedIn:
                dashboard.display(username)
                choice = dashboard.getUserChoice()
                while choice not in choices:
                    print('Sorry! Enter a valid option (1 to 5).')
                    choice = dashboard.getUserChoice()
                if choice is '1':
                    currentUser.viewProfile()
                    goback = input('Press Enter to go back...')
                elif choice is '2':
                    currentUser.addCoupon()
                    goback = input('Press Enter to go back...')
                elif choice is '3':
                    currentUser.viewCoupon()
                    goback = input('Press Enter to go back...')
                elif choice is '4':
                    currentUser.removeCoupon()
                    goback = input('Press Enter to go back...')
                else:
                    print(LOGOS['mainmenu'])
                    print("*" * 50)
                    print('Thank you for using MMT. You have been logged out')
                    loggedIn = False

        else:
            # open admin dashboard
            currentUser = Admin(currentUserDict['username'], currentUserDict['email'], \
            currentUserDict['password'], currentUserDict['gender'], currentUserDict['phone'], currentUserDict['memberSince'])
            currentUser.setBookingHistory(currentUserDict['bookingHistory'])
            currentUser.setCancellationHistory(currentUserDict['cancellationHistory'])
            currentUser.setLastTransaction(currentUserDict['lastTransaction'])

            dashboard = AdminDashboard()
            choices = ['1', '2', '3', '4', '5', '6']
            loggedIn = True
            while loggedIn:
                dashboard.display(username)
                choice = dashboard.getUserChoice()
                while choice not in choices:
                    print('Sorry! Enter a valid option (1 to 6).')
                    choice = dashboard.getUserChoice()
                if choice is '1':
                    currentUser.viewAllCustomers()
                    goback = input('Press Enter to go back...')
                elif choice is '2':
                    currentUser.viewAllCompanies()
                    goback = input('Press Enter to go back...')
                elif choice is '3':
                    currentUser.viewCustomerDetails()
                    goback = input('Press Enter to go back...')
                elif choice is '4':
                    currentUser.viewCompanyDetails()
                    goback = input('Press Enter to go back...')
                elif choice is '5':
                    currentUser.addCoupon()
                else:
                    loggedIn = False
                    print("You've been logged out! Thank you for using MMT")

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
        print('Q. Who wrote this system?')
        print("Hey! That'd be me, Abhijit. I am a student at IIIT Delhi (year 2018).")
        print('Q. How did you make those cool logos?')
        print("Well, I didn't. I generated them using an online tool called ascii-art-generator, and a very cool website from Christopher Johnson. Look him up.")
        print('Q. Why did you build this thing?')
        print("Assignment, ofcourse! It was a lot of fun too!")
        print("Q. What course is this assignment part of?")
        print("Object Oriented Programming And Design, CSE600a2")
    else:
        systemRunning = False
