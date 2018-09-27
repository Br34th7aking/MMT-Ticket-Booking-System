from abc import ABC, abstractmethod
import random
import json

class Trip(ABC):
    '''abstract trip class '''
    def planner(self, source, destination, date):
        pass

class Flight(Trip):
    def planner(self, source, destination, date):
        pnr = self.generatePNR()
        ticketType = "AIR"
        company, farePerPerson = self.companyAndFare()
        src = source
        dest = destination
        doj = date
        passengerDetails = self.fillPassengerDetails()
        fare = farePerPerson * len(passengerDetails)

        #create a ticket
        ticket = Ticket(pnr, ticketType, company, fare, src, dest, doj, passengerDetails)

        ticketData = ticket.__dict__
        return ticketData
    def generatePNR(self):
        return random.randint(1000000000, 9999999999)  # create a random 10 digit pnr
    def companyAndFare(self):
        data = json.load(open('companyData.json', 'r'))
        listOfCompanies = []
        discountPercent = 0
        for company in data:
            discountPercent = 0
            if company['serviceType'] == "AIR":
                if len(company['discountCoupons']) is not 0:
                    randomCouponNumber = random.randint(0, len(company['discountCoupons'])-1)
                    discountPercent = company['discountCoupons'][randomCouponNumber]['discount']
                listOfCompanies.append([company['companyName'], discountPercent])

        baseFare = 2000
        companyAndFare = []
        for company in listOfCompanies:
            companyName = company[0]
            discountPercent = company[1]
            fare = baseFare + random.randint(1000, 9999)
            fare -= (discountPercent * fare) / 100
            companyAndFare.append([companyName, fare, discountPercent])

        print("Following are the list of companies and ticket prices.")
        print('%-15s %-15s %-15s' % ("Company", "Fare", "Discount"))
        print('%-15s %-15s %-15s' % ("*******", "****", "********"))
        for i in companyAndFare:
            print("%-15s %-15s %-3s %%" %(i[0], i[1], i[2]))
        company = input('Enter your choice(company name): ').upper()

        for i in companyAndFare:
            if i[0] == company:
                fare = i[1]
                break
        return company, fare
    def fillPassengerDetails(self):
        numPassengers = int(input('Enter number of passengers: '))
        totalPassengers = []
        i = 0
        while i < numPassengers:
            name = input('Enter name of passenger {}: '.format(i+1))
            age = input('Enter age of passenger {}: '.format(i+1))
            gender = input('Enter gender of passenger {}(M or F): '.format(i+1))
            i += 1
            passenger = [name, age, gender]
            totalPassengers.append(passenger)
        return totalPassengers

class BusJourney(Trip):
    def planner(self, source, destination, date):
        pnr = self.generatePNR()
        ticketType = "BUS"
        company, farePerPerson = self.companyAndFare()
        src = source
        dest = destination
        doj = date
        passengerDetails = self.fillPassengerDetails()
        fare = farePerPerson * len(passengerDetails)

        #create a ticket
        ticket = Ticket(pnr, ticketType, company, fare, src, dest, doj, passengerDetails)

        ticketData = ticket.__dict__
        return ticketData
    def generatePNR(self):
        return random.randint(1000000000, 9999999999)  # create a random 10 digit pnr
    def companyAndFare(self):
        data = json.load(open('companyData.json', 'r'))
        listOfCompanies = []
        discountPercent = 0
        for company in data:
            discountPercent = 0
            if company['serviceType'] == "BUS":
                if len(company['discountCoupons']) is not 0:
                    randomCouponNumber = random.randint(0, len(company['discountCoupons'])-1)
                    discountPercent = company['discountCoupons'][randomCouponNumber]['discount']
                listOfCompanies.append([company['companyName'], discountPercent])

        baseFare = 200
        companyAndFare = []
        for company in listOfCompanies:
            companyName = company[0]
            discountPercent = company[1]
            fare = baseFare + random.randint(100, 1000)
            fare -= (discountPercent * fare) / 100
            companyAndFare.append([companyName, fare, discountPercent])

        print("Following are the list of companies and ticket prices.")
        print('%-15s %-15s %-15s' % ("Company", "Fare", "Discount"))
        print('%-15s %-15s %-15s' % ("*******", "****", "********"))
        for i in companyAndFare:
            print("%-15s %-15s %-3s %%" %(i[0], i[1], i[2]))
        company = input('Enter your choice(company name): ').upper()

        for i in companyAndFare:
            if i[0] == company:
                fare = i[1]
                break
        return company, fare
    def fillPassengerDetails(self):
        numPassengers = int(input('Enter number of passengers: '))
        totalPassengers = []
        i = 0
        while i < numPassengers:
            name = input('Enter name of passenger {}: '.format(i+1))
            age = input('Enter age of passenger {}: '.format(i+1))
            gender = input('Enter gender of passenger {}(M or F): '.format(i+1))
            i += 1
            passenger = [name, age, gender]
            totalPassengers.append(passenger)
        return totalPassengers

class TrainJourney(Trip):
    def planner(self, source, destination, date):
        pnr = self.generatePNR()
        ticketType = "RAIL"
        company, farePerPerson = self.companyAndFare()
        src = source
        dest = destination
        doj = date
        passengerDetails = self.fillPassengerDetails()
        fare = farePerPerson * len(passengerDetails)

        #create a ticket
        ticket = Ticket(pnr, ticketType, company, fare, src, dest, doj, passengerDetails)

        ticketData = ticket.__dict__
        return ticketData
    def generatePNR(self):
        return random.randint(1000000000, 9999999999)  # create a random 10 digit pnr
    def companyAndFare(self):
        company = "IRCTC"
        data = json.load(open('companyData.json', 'r'))
        discountPercent = 0
        for comp in data:
            if comp['companyName'] == 'IRCTC':
                if len(comp['discountCoupons']) is not 0:
                    randomCouponNumber = random.randint(0, len(comp['discountCoupons'])-1)
                    discountPercent = comp['discountCoupons'][randomCouponNumber]['discount']

        baseFare = 500
        fare = baseFare + random.randint(100, 5000)
        fare -= (discountPercent * fare) / 100
        discountPercent = str(discountPercent)
        print('You will get a discount of {} %.'.format(discountPercent))
        return company, fare
    def fillPassengerDetails(self):
        numPassengers = int(input('Enter number of passengers: '))
        totalPassengers = []
        i = 0
        while i < numPassengers:
            name = input('Enter name of passenger {}: '.format(i+1))
            age = input('Enter age of passenger {}: '.format(i+1))
            gender = input('Enter gender of passenger {}(M or F): '.format(i+1))
            i += 1
            passenger = [name, age, gender]
            totalPassengers.append(passenger)
        return totalPassengers

class Ticket():
    def __init__(self, pnr, ticketType, company, fare, source, destination,\
    dateOfJourney, passengerDetails = []):
        self.pnr = pnr
        self.ticketType = ticketType
        self.company = company
        self.fare = fare
        self.dateOfJourney = dateOfJourney
        self.passengerDetails = passengerDetails
        self.source = source
        self.destination = destination

    def getDateOfJourney(self):
        return self.dateOfJourney

    def getPNR(self):
        return self.pnr

    def getTicketType(self):
        if (self.ticketType == '1'):
            return 'Flight Ticket'
        elif self.ticketType == '2':
            return 'Train Ticket'
        else:
            return 'Bus Ticket'

    def getFare(self):
        return self.fare

    def createDict(self):
        ''' returns a dictionary that can be stored in the database '''
        return self.__dict__

class Coupon:
    def __init__(self, couponCode, discount, company, validTillDate):
        self.couponCode = couponCode
        self.discount = discount
        self.company = company
        self.validTillDate = validTillDate

    def getCouponData(self):
        return self.couponCode, self.discount, self.company, self.validTillDate
#test
# t = Ticket(1000, 2, "abhijit", "IRCTC", "200", 'dhanbad', 'daltonganj', "2018-09-26", ['abhijit', 'kajal'])
# print(t.details())
# f = Flight()
# f.planner('Delhi', 'Daltonganj', '26-11-2018')
