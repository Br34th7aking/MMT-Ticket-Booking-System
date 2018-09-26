from abc import ABC, abstractmethod

class User(ABC):
    ''' abstract class for user '''
    @abstractmethod
    def viewProfile(self):
        pass


class Customer(User):

    def __init__(self, username, email, password, gender, phone, memberSince, bookingHistory=[], \
    cancellationHistory=[], lastTransaction=[]):
        pass

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
