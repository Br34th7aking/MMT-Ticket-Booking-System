# MMT-Ticket-Booking-System
A console application that provides basic ticket booking functionality


## How to run the application
Open a command window and navigate to the project folder. There you will see a file 'main.py'

To run it, use the following code:
```
python3 main.py
```

## Classes
List of all classes with short descriptions

### Menu
This is an abstract class from which other menu classes inherit

### Main Menu
This class is used to create the start menu when the program is launched

Methods include:
#### display()
To display a list of choices

#### getUserChoice()
returns the choice selected by the user

### Login
This class creates the login menu for a user

Methods include:
#### display()
To display a list of choices

#### getLoginDetails()
returns the username, password and userType entered by the user

### Register
This class creates the register menu for a user

Methods include:
#### display()
To display a list of choices

#### checkExistingRecord()
returns True if no matching user found in the database, else False

#### isValidPhoneNumber()
returns True if phone number entered is a valid string, else False

#### registerCustomer()
This method creates a new user and adds him to the customer database

#### registerCompany()
This method creates a new company object and adds it to the company database

#### signUp()
Common method that either calls registerCustomer() or registerCompany() depending on userType

### CustomerDashboard
This class creates the dashboard for a customer

Methods include:
#### display()
To display a list of choices

#### getUserChoice()
returns the choice made by the user

### CompanyDashboard
This class creates the dashboard for a company

Methods include:
#### display()
To display a list of choices

#### getUserChoice()
returns the choice made by the user

### AdminDashboard
creates the dashboard for admin user

Methods include:
#### display()
To display a list of choices

#### getUserChoice()
returns the choice made by the user

### User
Abstract user class

Methods include:
#### viewProfile()
to display the user profile

### Customer
Class to create a customer object

#### Attributes
1. username
2. email
3. password
4. gender
5. phone
6. memberSince - a string representing the date of joining
7. bookingHistory - a list containing the entire booking history
8. cancellationHistory - a list containing the details of all cancelled tickets
9. lastTransaction - a list containing details of the last transaction

#### Methods
1. **viewProfile()**
2. **changePassword()**
3. **bookFlight()**
4. **bookTrainTicket()**
5. **bookBusTicket()**
6. **cancelTicket()**
7. **calculateRefund()**
8. **viewBookingHistory()**
9. **viewLastTransaction()**
10. **viewCancellationHistory()**
11. **viewUpComingJourney()**
12. **setBookingHistory()**
13. **setLastTransaction()**
14. **setCancellationHistory()**
15. **createDict()** - returns a dictionary containing the object properties

### Company
Class to create a company object

#### Attributes
1. companyName
2. password
3. serviceType - can be AIR, BUS or RAIL(fixed for IRCTC)
4. helpline
5. memberSince
6. discountCoupons - a list containing coupons offered by the company

#### Methods
1. **viewProfile()**
2. **addCoupon()**
3. **viewCoupon()**
4. **removeCoupon()**
5. **createDict()**
6. **setCoupons()**

### Admin
Class for admin user

#### Attributes
1. username
2. email
3. password
4. gender
5. phone
6. memberSince
7. bookingHistory
8. cancellationHistory
9. lastTransaction

#### Methods
1. **viewProfile()**
2. **viewAllCustomers()**
3. **viewAllCompanies()**
4. **viewCustomerDetails()**
5. **viewCompanyDetails()**
6. **addCoupon()**
7. **setBookingHistory()**
8. **setCancellationHistory()**
9. **setLastTransaction()**
