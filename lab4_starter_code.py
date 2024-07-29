
# Part 1: Setup ----------------------------------------------------------------

# import the python-specific sqlite library 
import sqlite3  

# make a connection between this .py file & the locally stored database
connection = sqlite3.connect("SuperAwesomeCompanyDataset.db")

# create a cursor object
cursor = connection.cursor()

# Already made the database and table ------------------------------------------

# Keep the new table code commented out if the database already has a table of 
# the same name (otherwise it will throw an error)
##cursor.execute("""CREATE TABLE dataset (
		##id INTEGER, 
		##project_name TEXT,
                ##business_unit TEXT,
                ##region TEXT,
                ##revenue_target_5_year REAL,
                ##revenue_2019 REAL,
                ##revenue_2020 REAL,
                ##revenue_2021 REAL,
                ##revenue_2022 REAL,
                ##revenue_2023 REAL,
                ##target_launch_date TEXT,
                ##actual_launch_date TEXT
                
	##)""")  
# SQLite dates: TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS")
# Excel: yyyy-mm-dd hh:mm:ss.ss

# Also already added MOST of the data  -----------------------------------------

### example of inserting a single row
##cursor.execute("""INSERT INTO dataset VALUES(
		##10001, 'CARING ZEBRA', 'RSP', 'America', 20000000, 3500000, 2000000,
                ##2500000, 3500000, 3800000, '2018-06-30 00:00:00.00', '2018-06-10 00:00:00.00')""")

### inserting multiple rows is a two step process:
### 1) data is a list of tuples (each tuple holds all data for one project)
##data = [
    ##(10002,'UNCOVERED RECORD','ENT','EMEA',95000000,14000000,14500000,18000000, 20000000,25000000,'2015-06-01 00:00:00.00','2015-06-30 00:00:00.00'),
    ##(10003,'BORING LINE','URO','Japan',150000000,25000000,24000000,26750000,35000000,40000000,'2016-01-01 00:00:00.00','2016-01-01 00:00:00.00'), 
    ##(10004,'VAST SENSE','SUR','China',25000000,0,0,3000000,9000000,15000000,'2021-01-01 00:00:00.00','2021-01-01 00:00:00.00'), 
    ##(10005,'VENOMOUS SCARF','SUR','Japan',40000000,3400000,5000000,7000000,8500000,12000000,'2019-06-01 00:00:00.00','2019-07-15 00:00:00.00'), 
    ##(10006,'CALM SCARECROW','SUR','Japan',115000000,22000000,20500000,21500000,25000000,27500000,'2015-06-01 00:00:00.00','2015-06-01 00:00:00.00'), 
    ##(10007,'PRICEY COMMITTEE','RSP','America',38000000,5800000,5700000,6500000,8000000,8500000,'2019-01-01 00:00:00.00','2019-03-01 00:00:00.00'), 
    ##(10008,'POSSIBLE FLAVOR','URO','America',30000000,5000000,4200000,4950000,5300000,5990000,'2017-01-01 00:00:00.00','2018-01-01 00:00:00.00'), 
    ##(10009,'UNARMED WATCH','ENT','Japan',100000000,15500000,20000000,22000000,23500000,24000000,'2018-07-01 00:00:00.00','2018-06-01 00:00:00.00'),
    ##(10010,'BORED SIDEWALK','SUR','China',20000000,3000000,2900000,3500000,4000000,4500000,'2019-01-01 00:00:00.00','2019-03-01 00:00:00.00'),
    ##(10011,'GIANT REWARD','RSP','EMEA',15000000,0,200000,2500000,4000000,7000000,'2020-01-01 00:00:00.00','2020-12-01 00:00:00.00'), 
    ##(10012,'IMPERFECT STEAM','RSP','South America',8000000,800000,780000,850000,900000,950000,'2019-01-30 00:00:00.00','2019-01-01 00:00:00.00'),
    ##(10013,'SOLID PROFIT','URO','EMEA',150000000,27000000,28000000,33000000,35500000,48000000,'2017-12-01 00:00:00.00','2018-01-15 00:00:00.00'),
    ##(10014,'HABITUAL DIME','SUR','EMEA',100000000,10000000,12000000,15000000,20000000,24000000,'2019-01-01 00:00:00.00','2019-06-25 00:00:00.00'),
    ##(10015,'UNDISTURBED FAIRIES','ENT','South America',20000000,0,0,1200000,8000000,15000000,'2020-06-01 00:00:00.00','2021-09-01 00:00:00.00'),
    ##(10016,'CIVIC JAR','URO','China',90000000,18000000,15500000,17000000,19500000,22000000,'2019-01-01 00:00:00.00','2018-12-01 00:00:00.00'),
    ##(10017,'PUZZLED SILK','URO','China',115000000,20500000,19000000,22000000,25500000,29500000,'2018-01-01 00:00:00.00','2018-01-01 00:00:00.00'),
    ##(10018,'LAME RAINSTORM','URO','EMEA',305000000,50000000,52000000,55000000,60000000,75000000,'2018-01-01 00:00:00.00','2017-10-01 00:00:00.00'),
    ##(10019,'TESTY SNAILS','RSP','EMEA',150000000,12500000,24000000,30000000,37500000,50000000,'2019-02-15 00:00:00.00','2019-06-15 00:00:00.00'),
    ##(10020,'DELIRIOUS EAR','ENT','America',85000000,1500000,16000000,22000000,24500000,27000000,'2019-01-30 00:00:00.00','2019-12-01 00:00:00.00'),
    ##(20002,'ENERGIZED ARM','SUR','America',100000000,17000000,17900000,18500000,21000000,25000000,'2017-01-01 00:00:00.00','2018-06-01 00:00:00.00'),
    ##(20003,'OMNISCIENT JAM','ENT','America',65000000,2000000,5000000,10000000,15000000,25000000,'2019-03-01 00:00:00.00','2019-04-01 00:00:00.00'),
    ##(20004,'WINGED CHALK','RSP','Japan',200000000,45000000,46500000,49000000,52000000,58000000,'2016-01-01 00:00:00.00','2016-01-01 00:00:00.00')]
### 2) special version of cursor.execute() used to push many rows of data at once
##cursor.executemany("INSERT INTO dataset VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

### commit pushes command update into the database
connection.commit()

# Look at table in DB Browser as is (what do you see?)

# Part 2: Finish where the last intern left off --------------------------------

# 2.1) Insert two new rows of data to account for newer projects (Friendly Cart and Tasteless Umbrella)
cursor.execute("""INSERT INTO dataset VALUES (20001, 'FRIENDLY CART', 'SUR', 'America', 1000000, 0, 0, 0, 0, 300000, '2023-06-01 00:00:00.00', '2023-11-15 00:00:00.00')""")
cursor.execute("""INSERT INTO dataset VALUES (20005, 'TASTELESS UMBRELLA', 'ENT', 'EMEA', 10000000, 0, 0, 0, 0, 5000000, '2021-02-01 00:00:00.00', '2023-02-15 00:00:00.00')""")

# 2.2) Print all the column names from the table
all_data = cursor.execute("SELECT * FROM dataset")

column_names = []
headers = all_data.description
for column in headers:
    column_names.append(column[0])
print(column_names)

# 2.3) Print out all data from all rows in the table in the console
for row in all_data:
    print(row)

# Part 3: Improve the dataset --------------------------------------------------

# 3.1) Add a new column in the table for forecast_accuracy
cursor.execute("ALTER TABLE dataset ADD COLUMN forecast_accuracy TEXT")

# Commit the changes to the database
connection.commit()

# 3.2) Do a little math to determine the value that will be inserted into this new column for every row: For each row, compare if target_launch_date >= actual_launch_date then project is "On Time", else project is "Behind Schedule"
cursor.execute("""UPDATE dataset
                SET forecast_accuracy = 'On Time'
                WHERE target_launch_date >= actual_launch_date""")
                  
cursor.execute("""UPDATE dataset
                SET forecast_accuracy = 'Behind Schedule'
                WHERE target_launch_date < actual_launch_date""")
                
connection.commit( )

# 3.3) Print out all the data in all rows, but sort the output by project name in ascending order 
sorted_data = cursor.execute("SELECT * FROM dataset ORDER BY project_name")
for row in sorted_data:
    print(row)

# 3.4) Add a new column named “actual_revenue_5_year” with the data type REAL to the table
cursor.execute("ALTER TABLE dataset ADD COLUMN actual_revenue_5_year REAL")

# Commit the changes to the database
connection.commit()

# 3.5) For each row, update the value in the actual_revenue_5_year column with the summation of revenue from 2019 through 2023 
new_sorted_data = cursor.execute("SELECT * FROM dataset ORDER BY id")
data = new_sorted_data.fetchall()

for i in range(25):
      current_id = data[i][0]
      total = data[i][5]+data[i][6]+data[i][7]+data[i][8]+data[i][9]
      
      cursor.execute(f"""UPDATE dataset
                         SET actual_revenue_5_year={total}
                         WHERE id=={current_id}""")
connection.commit()

# 3.6) print out the rows of only the projects that are "On Time", and sort the output by the actual_revenue_5_year column in descending order (DESC)
final_data = cursor.execute("""SELECT *
                              FROM dataset
                              WHERE forecast_accuracy='On Time'
                              ORDER BY actual_revenue_5_year DESC""")
for row in final_data:
    print(row)
    

# 3.7) Rename the table from "dataset" to "dataset_feb2024" so the next user 
# understands this dataset was last updated in february 2024
cursor.execute("ALTER TABLE dataset RENAME TO dataset_feb2024")
connection.commit()

# Best practice: close the connection when done with the database --------------
connection.close()
