from abc import ABC, abstractmethod

class Trip(ABC):
    '''abstract trip class '''
    def planner(self, source, destination, date):
        pass

class Flight(Trip):
    def planner(self, source, destination, date):
        pass

class BusJourney(Trip):
    def planner(self, source, destination, date):
        pass
class TrainJourney(Trip):
    def planner(self, source, destination, date):
        pass

class Ticket():
    def __init__(self, pnr, ticketType, bookedBy, company, fare, source, destination,\
    dateOfJourney, passengerDetails = []):
        self.pnr = pnr
        self.ticketType = ticketType
        self.bookedBy = bookedBy
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

    def details(self):
        ''' returns a dictionary that can be stored in the database '''
        ticketData = {}
        ticketData['pnr'] = self.pnr
        ticketData['ticketType'] = self.getTicketType()
        ticketData['bookedBy'] = self.bookedBy
        ticketData['company'] = self.company
        ticketData['fare'] = self.fare
        ticketData['source'] = self.source
        ticketData['destination'] = self.destination
        ticketData['dateOfJourney'] = self.dateOfJourney
        ticketData['passengerDetails'] = self.passengerDetails

        return ticketData

class Coupon:
    pass


#test
# t = Ticket(1000, 2, "abhijit", "IRCTC", "200", 'dhanbad', 'daltonganj', "2018-09-26", ['abhijit', 'kajal'])
# print(t.details())
