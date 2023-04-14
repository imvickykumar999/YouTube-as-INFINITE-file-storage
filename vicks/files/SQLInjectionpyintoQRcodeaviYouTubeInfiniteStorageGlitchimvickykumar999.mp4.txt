
# https://colab.research.google.com/drive/1QBMU9-v5jowlzg3fncjlrUKirWTHtKjq#scrollTo=es8m5ragAPDT

import sqlite3

conn = sqlite3.connect('test.db')

print ("Opened database successfully");

conn.execute('''
CREATE TABLE COMPANY (
  ID INT PRIMARY KEY NOT NULL,
  NAME TEXT NOT NULL,
  AGE INT NOT NULL,
  ADDRESS CHAR(50),
  SALARY REAL
)
''')

conn.execute('''
INSERT INTO COMPANY (
  ID, NAME, AGE, ADDRESS, SALARY
  ) VALUES (
    1, 'Paul', 32, 'California', 20000.00
  )
''')

conn.execute('''
INSERT INTO COMPANY (
  ID, NAME, AGE, ADDRESS, SALARY
  ) VALUES (
    2, 'Allen', 25, 'Texas', 15000.00
  )
''')

conn.execute('''
INSERT INTO COMPANY (
  ID, NAME, AGE, ADDRESS, SALARY
  ) VALUES (
    3, 'Teddy', 23, 'Norway', 20000.00
  )
''')

conn.execute('''
INSERT INTO COMPANY (
  ID, NAME, AGE, ADDRESS, SALARY
  ) VALUES (
    4, 'Mark', 25, 'Rich-Mond', 65000.00
  )
''')

conn.commit()

conn = sqlite3.connect('test.db')

NAME = input('Enter NAME : ')
ADDRESS = input('Enter ADDRESS : ')

command = f'''
SELECT * FROM COMPANY
WHERE NAME='{NAME}' AND ADDRESS='{ADDRESS}'
'''

print(command)
cursor = conn.execute(command)

for row in cursor:
  print(row)

conn.close()

# -------------------- OUTPUT:

'''
Enter NAME : ' OR 1=1 --
Enter ADDRESS : 123

SELECT * FROM COMPANY
WHERE NAME='' OR 1=1 --' AND ADDRESS='123'

(1, 'Paul', 32, 'California', 20000.0)
(2, 'Allen', 25, 'Texas', 15000.0)
(3, 'Teddy', 23, 'Norway', 20000.0)
(4, 'Mark', 25, 'Rich-Mond', 65000.0)
'''
