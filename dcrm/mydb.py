# this is for once, run it and all done

import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd='mistrs2P',

)

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrm")
print('All done!')
# All done