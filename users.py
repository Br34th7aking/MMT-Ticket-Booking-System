from abc import ABC, abstractmethod

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
        pass
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
    def __init__(self, companyName, serviceType, helpline, memberSince, discountCoupons):
        pass
    def viewProfile(self):
        pass
    def addCoupon(self):
        pass
    def removeCoupons(self):
        pass
    def changeFare(self):
        pass

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
print(a.createDict())
