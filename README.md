# BODYBUILDER'S NUTRITION APPLICATION

## Introduction:
### The Bodybuilder's Nutrition Application (BNA) is a passion project of mine created from an adoration for health & fitness. As someone who enjoys working out, a big challenge for me revolves around keeping a straight diet. For this purpose, along with the enjoyment I find in software development; I built this application.
### The aim of BNA is to keep track of users' biometrics and provide them with suggestions for their dietary fitness goals. These goals are reduced to key fundamentals: bulking calories and cutting calories. 'Bulking' pertains to the bodybuilding practice of consuming more calories than one weighs in the aim of building muscle mass. 'Cutting' on the other hand, is the practice of consuming fewer calories in order to lose [fat] mass. And so, BNA ultimately provides users with a metric in the form of the number of calories that they must consume in order to gain or lose weight. The accuracy of these values is determined by the [Harris-Benedict Equation](https://www.sciencedirect.com/science/article/abs/pii/S0261561420306166). 
### This application was built using Python and integrations with MySQL. The application can be divided into two portions: the biometrics data acquisition, and the data insertion. 

## Requirements:
### This application requires the following requirements:
* mysql-connector-python (latest)
* mysql-connector-python-rf (latest)
* MySQL Community Server (latest)
* Python 3.7 (or later)
* pip (latest)
### It is worth noting that two MySQL Python packages are recommended to be installed. This is because there can occasionally be issues with one or the other package. Installing both allows for optimal success.

## Installation:
1. Download and install the latest version of MySQL from the [MySQL community downloads webpage](https://dev.mysql.com/downloads/mysql/)
2. Set up a database connection within the MySQL Workbench
3. Ensure you have the latest version of Python and pip installed


## Instructions:
### Part 1: Connect to your database and set-up table within the 'createtable.py' file
1. Create a variable for your database by providing the hostname, username, password and database name specific to your MySQL database
```
# Make DB connection
mydb = mysql.connector.connect(
    host='',
    user='',
    passwd='',
    database=''
)
```
2. Define the cursor from which you can subsequently execute SQL commands in Python
`mycursor = mydb.cursor()`
3. Run a command that generates the table in which biometrics data will be stored
```
mycursor.execute("CREATE TABLE bna (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), "
                 "gender VARCHAR(7), age INTEGER(3), "
                 "weight DECIMAL(5, 1), height DECIMAL(5, 1), activity INTEGER(1), "
                 "tdee DECIMAL(6, 2), bulk DECIMAL(6, 2), cut DECIMAL(6, 2))")

mydb.commit()
```
Note that you must `commit` the changes before running the script
4. You should now have a table set up in your MySQL database which you can find in the Workbench by running
`SELECT * FROM bna;`

## Part 2: Biometric data acquisition using Python
1. Run the main.py file
2. You will be prompted to provide your name, gender, weight, height and age
```
name = input('Please enter your name (optional) ')
gender = input('Are you a male or female? ')
weight = float(input(f'Please enter your weight(kg) '))
height = float(input(f'Please enter your height(cm) '))
age = int(input('Please enter your age '))
```
3. From this data, a value for your basal metabolic ratio will be provided. This varies based on gender as seen below
```
# Calculate basal metabolic rate
if gender.lower() == "male":
    bmr = (13.7 * weight) + (5 * height) - (6.8 * age) + 66
elif gender.lower() == 'female':
    bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
```
For example, David, a 175cm, 70kg, 26-year-old male would receive the following output:
```
David Your basal metabolic rate is 1723
This is the number of calories that you burn as your body performs basic life-sustaining function.
```
4. You are then prompted to provide a measure of activity level based on descriptive variables
```
1 : Sedentary (little to no exercise + work a desk job) 
2 : Lightly Active : (light exercise 1-3 days / week)
3 : Moderately Active : (moderate exercise 3-5 days / week)
4 : Very Active : (heavy exercise 6-7 days / week)
5 : Extremely Active: (very heavy exercise, hard labor job, training 2x / day)
```
5. David may describe himself as very active (4) to which he would receive the following output:
```
Your Total Daily Energy Expenditure is 2972 calories. You must consume this to maintain your weight
```
6. Furthermore, the key values of interest are provided:
```
In order to gain weight you must consume 3567 calories a day.
In order to lose weight you must consume 2378 calories daily.
```

## Part 3: Insertion into MySQL database
1. To account for multiple individuals using BNA, we can simplify the insertion process by treating users as a class. Hence, we would treat each metric as a variable and generate a user by instantiating the 'Person' class
```
# Store user details in a class object
class Person:
    def __init__(self, name, gender, age, weight, height, activity, tdee, bulk, cut):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.activity = activity
        self.tdee = tdee
        self.bulk = bulk
        self.cut = cut
```
2. We can then place the MySQL cursor
```
mycursor = mydb.cursor()
```
3. In order to collate a single user's data we must instantiate the Person class
```
p1 = Person(name, gender, age, weight, height, activity, tdee, bulk, cut)
```
4. We can then execute the SQL `INSERT` command
```
sqlformula = "INSERT INTO bna (name, gender, age, weight, height, activity, tdee, bulk, cut) " \
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
user = (p1.name, p1.gender, p1.age, p1.weight,
        p1.height, p1.activity, p1.tdee, p1.bulk, p1.cut)

mycursor.execute(sqlformula, user)


mydb.commit()
```
5. Here we create a variable that specifies placeholders for each value (sqlformula). We then create a variable called user that borrows values from when the Person class was instantiated
6. We finally commit the changes to the database and we can finally analyse the data within MySQL

## Maintainers:
* Dylan Sreenivasan - Creator (dylansree28@gmail.com)
###### Please note that development has slowed down for this project
###### For all queries, please contact the above email address.
