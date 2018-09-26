from abc import ABC, abstractmethod
from logos import LOGOS
from miscellaneous import *
from datetime import date

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
        source = input('Enter source city: ')
        destination = input('Enter destination city: ')
        print('Enter date of journey: ')
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
        pass
    def bookBusTicket(self):
        pass
    def cancelTicket(self):
        pass
    def viewBookingHistory(self):
        pass
    def viewLastTransaction(self):
        print(LOGOS['home'])
        print('*' * 10 + "Customer Dashboard" + '*' * 10)
        print('\n')
        print('Your Last Transaction Details: ')
        print("%-30s %-35s" %(self.lastTransaction[1][0], self.lastTransaction[1][1]))
        print("%-30s %-35s" %(self.lastTransaction[6][0], self.lastTransaction[6][1]))
        print("%-30s %-35s" %(self.lastTransaction[7][0], self.lastTransaction[7][1]))
        print("%-30s %-35s" %(self.lastTransaction[2][0], self.lastTransaction[2][1]))
        print("%-30s %-35s" %(self.lastTransaction[4][0], self.lastTransaction[4][1]))
        print("%-30s %-35s" %(self.lastTransaction[5][0], self.lastTransaction[5][1]))
        print("%-30s %-35s" %(self.lastTransaction[3][0], self.lastTransaction[3][1]))
    def viewCancellationHistory(self):
        pass
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
        pass
    def viewCoupon(self):
        pass
    def removeCoupon(self):
        pass
    def createDict(self):
        '''returns a dictionary containing company attributes '''
        return self.__dict__
    def setCoupons(self, coupons):
        self.discountCoupons = coupons
class Admin(User):
    def viewProfile(self):
        pass
    def viewAllCustomers(self):
        pass
    def viewAllCompanies(self):
        pass
    def viewCustomerDetails(self, customer):
        pass
    def viewCompanyDetails(self, company):
        pass
    def addCoupons(self, company):
        pass

#test
# a = Customer('1','1','1','1','1', '1')
# a.bookFlight()
