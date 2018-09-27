# MMT-Ticket-Booking-System
A console application that provides basic ticket booking functionality


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
