import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database=''
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE bna (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), "
                 "gender VARCHAR(7), age INTEGER(3), "
                 "weight DECIMAL(5, 1), height DECIMAL(5, 1), activity INTEGER(1), "
                 "tdee DECIMAL(6, 2), bulk DECIMAL(6, 2), cut DECIMAL(6, 2))")

mydb.commit()
