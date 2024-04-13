import sqlite3


# Connect to SQlite 
connection = sqlite3.connect('student.db')

# Create a cursor object to insert record, create table 
cursor = connection.cursor()

# Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));

"""

cursor.execute(table_info)

# Insert some more records
cursor.execute("""Insert into STUDENT values('Ava', 'Data Science', 'A')""")
cursor.execute("""Insert into STUDENT values('Abhirami', 'Data Science', 'B')""")
cursor.execute("""Insert into STUDENT values('Rhyn', 'Data Science', 'A')""")
cursor.execute("""Insert into STUDENT values('Rhea', 'DEVOPS', 'A')""")
cursor.execute("""Insert into STUDENT values('Arjun', 'DEVOPS', 'A')""")

# Display all the records 
print("The inserted records are")
data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()