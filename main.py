# BODYBUILDER'S NUTRITION APPLICATION
import mysql.connector

#Make DB connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database=''
)


# Begin application
# Enter information as specified
print("BODYBUILDER'S NUTRITION APPLICATION"
      "\nPlease note this calculator uses the metric system.")
print('•••••••••••••••••••••••••••••••••••')
print(f"LET'S GET TO KNOW YOU")

bmr = 0
tdee = 0
name = input('Please enter your name (optional) ')
gender = input('Are you a male or female? ')
weight = float(input(f'Please enter your weight(kg) '))
height = float(input(f'Please enter your height(cm) '))
age = int(input('Please enter your age '))


# Calculate basal metabolic rate
if gender.lower() == "male":
    bmr = (13.7 * weight) + (5 * height) - (6.8 * age) + 66
elif gender.lower() == 'female':
    bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655

print('•••••••••••••••••••••••••••••••••••')
print(f'{name.capitalize()} Your basal metabolic rate is {int(bmr)}'.strip())
print('This is the number of calories that you burn as your '
      'body performs basic life-sustaining function.')


# Provide a measure of actvity
print('•••••••••••••••••••••••••••••••••••')
print('ACTIVITY LEVEL')
print('•••••••••••••••••••••••••••••••••••')
activity_multiplier = {1: 'Sedentary (little to no exercise + work a desk job) ',
                       2: 'Lightly Active : (light exercise 1-3 days / week)',
                       3: 'Moderately Active : (moderate exercise 3-5 days / week)',
                       4: 'Very Active : (heavy exercise 6-7 days / week)',
                       5: 'Extremely Active: (very heavy exercise, hard labor job, training 2x / day)'}

for i in activity_multiplier:
    print(i, ':', activity_multiplier[i])
print()
activity = int(input("How active are you?"
                     '\nSelect 1-5 from the above.'
                     '\n'))

while not 1 <= activity <= 5:
    print('•••••••••••••••••••••••••••••••••••')
    print('ACTIVITY LEVEL')
    print('•••••••••••••••••••••••••••••••••••')
    for i in activity_multiplier:
        print(i, ':', activity_multiplier[i])
    print()


# Calculate total daily energy expenditure
if activity == 1:
    tdee = bmr * 1.2
elif activity == 2:
    tdee = bmr * 1.375
elif activity == 3:
    tdee = bmr * 1.55
elif activity == 4:
    tdee = bmr * 1.725
elif activity == 5:
    tdee = bmr * 1.9

print()
print('•••••••••••••••••••••••••••••••••••')
print(f"Your Total Daily Energy Expenditure is {int(tdee)} calories. "
      f"You must consume this to maintain your weight")
print('•••••••••••••••••••••••••••••••••••')


# Calculate number of calories to gain and lose weight
bulk = int(tdee + (0.2 * tdee))
cut = int(tdee - (0.2 * tdee))
print(f"In order to gain weight you must consume {bulk} calories a day.")
print(f"In order to lose weight you must consume {cut} calories daily.")


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


mycursor = mydb.cursor()

p1 = Person(name, gender, age, weight, height, activity, tdee, bulk, cut)


# Insert user info into MySQL DB
sqlformula = "INSERT INTO bna (name, gender, age, weight, height, activity, tdee, bulk, cut) " \
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
user = (p1.name, p1.gender, p1.age, p1.weight,
        p1.height, p1.activity, p1.tdee, p1.bulk, p1.cut)

mycursor.execute(sqlformula, user)


mydb.commit()