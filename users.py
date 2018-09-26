from abc import ABC, abstractmethod
from logos import LOGOS
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

    def updateProfile():
        pass
    def bookFlight(self):
        pass
    def bookTrainTicket(self):
        pass
    def bookBusTicket(self):
        pass
    def cancelTicket(self):
        pass
    def viewBookingHistory(self):
        pass
    def viewLastTransaction(self):
        pass
    def viewCancellationHistory(self):
        pass
    def createDict(self):
        '''returns a dictionary containing the customer data'''
        return self.__dict__


class Company(User):
    def __init__(self, companyName, password, serviceType, helpline, memberSince):
        self.companyName = companyName
        self.password = password
        self.serviceType = serviceType
        self.helpline = helpline
        self.memberSince = memberSince
        self.discountCoupons = []
    def viewProfile(self):
        pass
    def addCoupon(self):
        pass
    def removeCoupons(self):
        pass
    def changeFare(self):
        pass
    def createDict(self):
        '''returns a dictionary containing company attributes '''
        return self.__dict__
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
a = Customer('1','1','1','1','1', '1')
a.viewProfile()
