from abc import ABC, abstractmethod
from logos import LOGOS
from miscellaneous import *
from datetime import date
import random

class User(ABC):
    ''' abstract class for user '''
    @abstractmethod
    def viewProfile(self):
        pass


class Customer(User):

    def __init__(self, username, email, password, gender, phone, memberSince):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.phone = phone
        self.memberSince = memberSince
        self.bookingHistory = []
        self.cancellationHistory = []
        self.lastTransaction = []

    def viewProfile(self):
        print(LOGOS['profile'])
        print("*" * 50)
        print('Username: ', self.username)
        print('Email: ', self.email)
        print('Gender: ', self.gender)
        print('Phone: ', self.phone)
        print('Member Since: ', self.memberSince)
        # implement how user goes to previous menu

    def changePassword(self):
        password = input('Enter new password(minimum 6 characters): ')
        while(len(password) < 6):
            password = input('Weak password. Enter minimum 6 characters: ')
        self.password = password

    def bookFlight(self):
        print(LOGOS['flight'])
        source = input('Enter source city: ')
        destination = input('Enter destination city: ')
        print('Enter date of journey: ')
        year = int(input('Year = '))
        month = int(input('Month = '))
        while(month > 12):
            print('Invalid month. Enter a value between 1 and 12')
            month = int(input('Month = '))
        day = int(input('Day = '))
        while(day > 31):
            print('Invalid day. Enter a value between 1 and 31')
            day = int(input('Day = '))
        doj = date(year, month, day)
        while(doj < date.today()):
            print('That date is in the past. Enter a correct date')
            year = int(input('Year = '))
            month = int(input('Month = '))
            day = int(input('Day = '))
            doj = date(year, month, day)

        f = Flight()
        ticketData = f.planner(source, destination, str(doj))

        self.bookingHistory.append(ticketData)
        self.lastTransaction = [[key, value] for key, value in ticketData.items()] # overwrite last transaction
        print("%-50s" %("Booking Details"))
        print("%-30s %-35s" %(self.lastTransaction[1][0], self.lastTransaction[1][1]))
        print("%-30s %-35s" %(self.lastTransaction[6][0], self.lastTransaction[6][1]))
        print("%-30s %-35s" %(self.lastTransaction[7][0], self.lastTransaction[7][1]))
        print("%-30s %-35s" %(self.lastTransaction[2][0], self.lastTransaction[2][1]))
        print("%-30s %-35s" %(self.lastTransaction[4][0], self.lastTransaction[4][1]))
        print("%-30s %-35s" %(self.lastTransaction[5][0], self.lastTransaction[5][1]))
        print("%-30s %-35s" %(self.lastTransaction[3][0], self.lastTransaction[3][1]))
        confirm = input('Enter Y to confirm and make payment, N to cancel...').upper()
        while (confirm != 'Y') and (confirm != 'N'):
            confirm = input('Invalid Input. Enter Y to confirm and make payment, N to cancel...').upper()
        if confirm == 'Y':
            #write data to file
            data = json.load(open('customerData.json', 'r'))
            for user in data:
                if user['username'] == self.username:
                    user['bookingHistory'] = self.bookingHistory
                    user['lastTransaction'] = self.lastTransaction
                    break
            file = open('customerData.json', 'w')
            json.dump(data, file)
            file.close()
            print('Congratulations! Your ticket has been booked. Your PNR number is {}'.format(self.lastTransaction[0][1]))
            print('We wish you a happy and safe journey!')
    def bookTrainTicket(self):
        print(LOGOS['train'])
        source = input('Enter source city: ')
        destination = input('Enter destination city: ')
        print('Enter date of journey: ')
        year = int(input('Year = '))
        month = int(input('Month = '))
        while(month > 12):
            print('Invalid month. Enter between 1 and 12')
            month = int(input('Month = '))
        day = int(input('Day = '))
        while(day > 31):
            print('Invalid day. Enter between 1 and 31')
            day = int(input('Day = '))
        doj = date(year, month, day)
        while(doj < date.today()):
            print('That date is in the past. Enter a correct date')
            year = int(input('Year = '))
            month = int(input('Month = '))
            day = int(input('Day = '))
            doj = date(year, month, day)

        t = TrainJourney()
        ticketData = t.planner(source, destination, str(doj))

        self.bookingHistory.append(ticketData)
        self.lastTransaction = [[key, value] for key, value in ticketData.items()] # overwrite last transaction
        print("%-50s" %("Booking Details"))
        print("%-30s %-35s" %(self.lastTransaction[1][0], self.lastTransaction[1][1]))
        print("%-30s %-35s" %(self.lastTransaction[6][0], self.lastTransaction[6][1]))
        print("%-30s %-35s" %(self.lastTransaction[7][0], self.lastTransaction[7][1]))
        print("%-30s %-35s" %(self.lastTransaction[2][0], self.lastTransaction[2][1]))
        print("%-30s %-35s" %(self.lastTransaction[4][0], self.lastTransaction[4][1]))
        print("%-30s %-35s" %(self.lastTransaction[5][0], self.lastTransaction[5][1]))
        print("%-30s %-35s" %(self.lastTransaction[3][0], self.lastTransaction[3][1]))
        confirm = input('Enter Y to confirm and make payment, N to cancel...').upper()
        while (confirm != 'Y') and (confirm != 'N'):
            confirm = input('Invalid Input. Enter Y to confirm and make payment, N to cancel...').upper()
        if confirm == 'Y':
            #write data to file
            data = json.load(open('customerData.json', 'r'))
            for user in data:
                if user['username'] == self.username:
                    user['bookingHistory'] = self.bookingHistory
                    user['lastTransaction'] = self.lastTransaction
                    break
            file = open('customerData.json', 'w')
            json.dump(data, file)
            file.close()
            print('Congratulations! Your ticket has been booked. Your PNR number is {}'.format(self.lastTransaction[0][1]))
            print('We wish you a happy and safe journey!')
    def bookBusTicket(self):
        print(LOGOS['bus'])
        source = input('Enter source city: ')
        destination = input('Enter destination city: ')
        print('Enter date of journey: ')
        year = int(input('Year = '))
        month = int(input('Month = '))
        while(month > 12):
            print('Invalid month. Enter between 1 and 12.')
            month = int(input('Month = '))
        day = int(input('Day = '))
        while(day > 31):
            print('Invalid day. Enter between 1 and 31.')
            day = int(input('Day = '))
        doj = date(year, month, day)
        while(doj < date.today()):
            print('That date is in the past. Enter a correct date')
            year = int(input('Year = '))
            month = int(input('Month = '))
            day = int(input('Day = '))
            doj = date(year, month, day)

        b = BusJourney()
        ticketData = b.planner(source, destination, str(doj))

        self.bookingHistory.append(ticketData)
        self.lastTransaction = [[key, value] for key, value in ticketData.items()] # overwrite last transaction
        print("%-50s" %("Booking Details"))
        print("%-30s %-35s" %(self.lastTransaction[1][0], self.lastTransaction[1][1]))
        print("%-30s %-35s" %(self.lastTransaction[6][0], self.lastTransaction[6][1]))
        print("%-30s %-35s" %(self.lastTransaction[7][0], self.lastTransaction[7][1]))
        print("%-30s %-35s" %(self.lastTransaction[2][0], self.lastTransaction[2][1]))
        print("%-30s %-35s" %(self.lastTransaction[4][0], self.lastTransaction[4][1]))
        print("%-30s %-35s" %(self.lastTransaction[5][0], self.lastTransaction[5][1]))
        print("%-30s %-35s" %(self.lastTransaction[3][0], self.lastTransaction[3][1]))
        confirm = input('Enter Y to confirm and make payment, N to cancel...').upper()
        while (confirm != 'Y') and (confirm != 'N'):
            confirm = input('Invalid Input. Enter Y to confirm and make payment, N to cancel...').upper()
        if confirm == 'Y':
            #write data to file
            data = json.load(open('customerData.json', 'r'))
            for user in data:
                if user['username'] == self.username:
                    user['bookingHistory'] = self.bookingHistory
                    user['lastTransaction'] = self.lastTransaction
                    break
            file = open('customerData.json', 'w')
            json.dump(data, file)
            file.close()
            print('Congratulations! Your ticket has been booked. Your PNR number is {}'.format(self.lastTransaction[0][1]))
            print('We wish you a happy and safe journey!')
    def cancelTicket(self):
        pnr = input('Enter pnr of ticket to cancel')
        pnrExists = False
        for ticket in self.bookingHistory:
            if (str(ticket['pnr']) == pnr):
                pnrExists = True
                if ticket not in self.cancellationHistory:
                    # ticket was not already cancelled
                    print('Ticket with PNR {} will be cancelled.'.format(ticket['pnr']))
                    refund = self.calculateRefund(ticket)
                    print('Refund amount will be Rs. {}'.format(refund))
                    response = input('Enter y on n: ').upper()
                    while (response != 'Y') and (response != 'N'):
                        response = input('Enter y on n: ').upper()
                    if (response == 'Y'):
                        self.cancellationHistory.append(ticket)
                        self.lastTransaction = ["Ticket with PNR {} was cancelled.".format(ticket['pnr'])]
                        # update the file records
                        data = json.load(open('customerData.json', 'r'))
                        for user in data:
                            if user['username'] == self.username:
                                user['cancellationHistory'] = self.cancellationHistory
                                user['lastTransaction'] = self.lastTransaction
                                break
                        file = open('customerData.json', 'w')
                        json.dump(data, file)
                        file.close()
                        print('Your ticket was cancelled. Refund of {} initiated. Thank you for using our services.'.format(refund))
                    elif (response == 'N'):
                        print('You chose to not cancel the ticket. Have a happy journey!')
                else:
                    print('Ticket already cancelled!')
                break
    def calculateRefund(self, ticket):
        [year, month, day] = ticket['dateOfJourney'].split('-')
        if (date(int(year), int(month), int(day)) <= date.today()):
            refund = 0
        else:
            if (ticket['ticketType'] == "AIR"):
                refund = int(ticket['fare']) - 400
            elif (ticket['ticketType'] == "RAIL"):
                refund = int(ticket['fare']) - 60
            else:
                refund = int(ticket['fare']) - 80
        return refund
    def viewBookingHistory(self):
        print("Booking history")
        print('***************')
        for recordDict in self.bookingHistory:
            details = [[key, value] for key, value in recordDict.items()]
            print("%-30s %-35s" %(details[0][0], details[0][1]))
            print("%-30s %-35s" %(details[1][0], details[1][1]))
            print("%-30s %-35s" %(details[6][0], details[6][1]))
            print("%-30s %-35s" %(details[7][0], details[7][1]))
            print("%-30s %-35s" %(details[4][0], details[4][1]))
            print("\n")
    def viewLastTransaction(self):
        print('Last Transaction Details')
        print('************************')
        if (len(self.lastTransaction) == 1):
            # last transaction was a cancellaton
            print(self.lastTransaction[0])
        elif (len(self.lastTransaction) == 0):
            print('User has not done any transactions')
        else:
            print("%-30s %-35s" %(self.lastTransaction[0][0], self.lastTransaction[0][1]))
            print("%-30s %-35s" %(self.lastTransaction[1][0], self.lastTransaction[1][1]))
            print("%-30s %-35s" %(self.lastTransaction[6][0], self.lastTransaction[6][1]))
            print("%-30s %-35s" %(self.lastTransaction[7][0], self.lastTransaction[7][1]))
            print("%-30s %-35s" %(self.lastTransaction[2][0], self.lastTransaction[2][1]))
            print("%-30s %-35s" %(self.lastTransaction[4][0], self.lastTransaction[4][1]))
            print("%-30s %-35s" %(self.lastTransaction[5][0], self.lastTransaction[5][1]))
            print("%-30s %-35s" %(self.lastTransaction[3][0], self.lastTransaction[3][1]))
    def viewCancellationHistory(self):
        print("Cancellations history")
        print('*********************')
        for recordDict in self.cancellationHistory:
            details = [[key, value] for key, value in recordDict.items()]
            print("%-30s %-35s" %(details[0][0], details[0][1]))
            print("%-30s %-35s" %(details[1][0], details[1][1]))
            print("%-30s %-35s" %(details[6][0], details[6][1]))
            print("%-30s %-35s" %(details[7][0], details[7][1]))
            print("%-30s %-35s" %(details[4][0], details[4][1]))
            print("\n")

    def viewUpcomingJourneys(self):
        '''returns all the upcoming journeys that the user has '''
        #upcoming journeys = those bookings with date > today and those not in setCancellationHistory
        print('Your upcoming journeys')
        print('*' * 50)
        print('\n')
        upcoming = []
        for ticket in self.bookingHistory:
            if ticket not in self.cancellationHistory:
                [year, month, day] = ticket['dateOfJourney'].split('-')
                if date(int(year), int(month), int(day)) >= date.today():
                    upcoming.append(ticket)
        #display
        for ticketDict in upcoming:
            details = [[key, value] for key, value in ticketDict.items()]
            print("%-30s %-35s" %(details[0][0], details[0][1]))
            print("%-30s %-35s" %(details[1][0], details[1][1]))
            print("%-30s %-35s" %(details[6][0], details[6][1]))
            print("%-30s %-35s" %(details[7][0], details[7][1]))
            print("%-30s %-35s" %(details[4][0], details[4][1]))
            print("\n")

    def createDict(self):
        '''returns a dictionary containing the customer data'''
        return self.__dict__

    def setBookingHistory(self, history):
        self.bookingHistory = history
    def setCancellationHistory(self, history):
        self.cancellationHistory = history
    def setLastTransaction(self, transaction):
        self.lastTransaction = transaction

class Company(User):
    def __init__(self, companyName, password, serviceType, helpline, memberSince):
        self.companyName = companyName
        self.password = password
        self.serviceType = serviceType
        self.helpline = helpline
        self.memberSince = memberSince
        self.discountCoupons = []
    def viewProfile(self):
        print(LOGOS['profile'])
        print("*" * 50)
        print('Company Name: ', self.companyName)
        print('Service Type: ', self.serviceType)
        print('Help Line: ', self.helpline)
    def addCoupon(self):
        discount = int(input('Enter discount percentage (1 to 100)'))
        company = self.companyName
        couponCode = self.companyName + str(discount)
        #validity date will be from 2018 to 2025
        validyear = random.randint(2018, 2025)
        validmonth = random.randint(1, 12)
        validday = random.randint(1, 28)
        validDate = str(date(validyear, validmonth, validday))
        c = Coupon(couponCode, discount, company, validDate)
        cDict = c.__dict__

        data = json.load(open('companyData.json', 'r'))
        for company in data:
            if (company['companyName'] == self.companyName):
                company['discountCoupons'].append(cDict)
                break
        file = open('companyData.json', 'w')
        json.dump(data, file)
        file.close()
        print('Coupon added successfully.')
    def viewCoupon(self):
        print('Current Discount Coupons')
        print('************************')
        data = json.load(open('companyData.json', 'r'))
        for company in data:
            if (company['companyName'] == self.companyName):
                self.discountCoupons = company['discountCoupons']
                break
        for coupon in self.discountCoupons:
            couponData = [[key,value] for key, value in coupon.items()]
            for details in couponData:
                print('%-30s %-30s' % (details[0], details[1]))
            print('\n')
    def removeCoupon(self):
        couponCode = input('Enter the coupon code: ').upper()
        for coupon in self.discountCoupons:
            if (coupon['couponCode'] == couponCode):
                self.discountCoupons.remove(coupon)
                break
        data = json.load(open('companyData.json', 'r'))
        for company in data:
            if (company['companyName'] == self.companyName):
                company['discountCoupons'] = self.discountCoupons
                break
        file = open('companyData.json', 'w')
        json.dump(data, file)
        file.close()
        print('Coupon removed successfully.')
    def createDict(self):
        '''returns a dictionary containing company attributes '''
        return self.__dict__
    def setCoupons(self, coupons):
        self.discountCoupons = coupons
class Admin(User):
    def __init__(self, username, email, password, gender, phone, memberSince):
        self.username = username
        self.email = email
        self.password = password
        self.gender = gender
        self.phone = phone
        self.memberSince = memberSince
        self.bookingHistory = []
        self.cancellationHistory = []
        self.lastTransaction = []
    def viewProfile(self):
        pass
    def viewAllCustomers(self):
        '''displays a list of all usernames registered in the system'''
        data = json.load(open('customerData.json', 'r'))
        customers = []
        for user in data:
            if user['username'] != 'admin':
                customers.append(user['username'])
        print("%-50s" %("List of All Customers"))
        print("%-50s" %("*" * 50))
        for customerName in customers:
            print("%-50s" %(customerName))

    def viewAllCompanies(self):
        '''displays a list of companies based on choice: air, bus, all '''
        print('Enter 1 to see all airlines')
        print('Enter 2 to see all bus operators')
        print('Enter 3 to see all companies')
        choice = input('Your choice: ')
        data = json.load(open('companyData.json', 'r'))
        companies = []
        if choice is '1':
            # display airlines
            for company in data:
                if company['serviceType'] == "AIR":
                    companies.append(company['companyName'])
            print("%-50s" %("List of All Registered Airlines"))
            print("%-50s" %("*" * 50))
            for companyName in companies:
                print("%-50s" %(companyName))
        elif choice is '2':
            #display buses
            for company in data:
                if company['serviceType'] == "BUS":
                    companies.append(company['companyName'])
            print("%-50s" %("List of All Registered Bus Operators"))
            print("%-50s" %("*" * 50))
            for companyName in companies:
                print("%-50s" %(companyName))
        else:
            # display all
            for company in data:
                companies.append([company['companyName'], company['serviceType']])
            print("%-50s" %("List of All Companies"))
            print("%-50s" %("*" * 50))
            print("\n")
            print("%-30s %-30s" % ("Company", "Service Type"))
            print("%-30s %-30s" % ("*******", "************"))
            for company in companies:
                print("%-30s %-30s" %(company[0], company[1]))
    def viewCustomerDetails(self):
        customerName = input('Enter customer name')
        data = json.load(open('customerData.json', 'r'))
        userExists = False
        currentUserDict = {}
        for user in data:
            if (user['username'] == customerName):
                currentUserDict = user
                userExists = True
                break
        if not userExists:
            print('No such user exists!')
        else:
            currentUser = Customer(currentUserDict['username'], currentUserDict['email'], \
            currentUserDict['password'], currentUserDict['gender'], currentUserDict['phone'], currentUserDict['memberSince'])
            currentUser.setBookingHistory(currentUserDict['bookingHistory'])
            currentUser.setCancellationHistory(currentUserDict['cancellationHistory'])
            currentUser.setLastTransaction(currentUserDict['lastTransaction'])
            currentUser.viewProfile()
            currentUser.viewBookingHistory()
            currentUser.viewCancellationHistory()
            currentUser.viewLastTransaction()

    def viewCompanyDetails(self):
        companyName = input('Enter company name').upper()
        data = json.load(open('companyData.json', 'r'))
        companyExists = False
        currentCompanyDict = {}
        for company in data:
            if (company['companyName'] == companyName):
                currentCompanyDict = company
                userExists = True
                break
        if not userExists:
            print('No such company exists in our records!')
        else:
            print('Company Details')
            print('***************')
            print('\n')
            for key, value in currentCompanyDict.items():
                print ('%-30s %-30s' %(key, value))
    def addCoupon(self):
        data = json.load(open('companyData.json', 'r'))
        companies = []
        for company in data:
            companies.append(company['companyName'])
        companyName = input('Enter company name: ').upper()
        while companyName not in companies:
            print('No such company in our database.')
            companyName = input('Enter company name correctly: ').upper()
        discount = int(input('Enter the discount'))
        couponCode = companyName + str(discount)
        #validity date will be from 2018 to 2025
        validyear = random.randint(2018, 2025)
        validmonth = random.randint(1, 12)
        validday = random.randint(1, 28)
        validDate = str(date(validyear, validmonth, validday))
        c = Coupon(couponCode, discount, companyName, validDate)
        cDict = c.__dict__

        for company in data:
            if company['companyName'] == companyName:
                company['discountCoupons'].append(cDict)
                break
        file = open('companyData.json', 'w')
        json.dump(data, file)
        file.close()
        print('Coupon added successfully')

    def setBookingHistory(self, history):
        self.bookingHistory = history
    def setCancellationHistory(self, history):
        self.cancellationHistory = history
    def setLastTransaction(self, transaction):
        self.lastTransaction = transaction

#test
# a = Customer('1','1','1','1','1', '1')
# a.bookFlight()
