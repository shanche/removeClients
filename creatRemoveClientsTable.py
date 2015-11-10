# Put all the clients in the table, set effective as "N"
# Written by SHAN CHE, Nov. 10, 2015

import MySQLdb
from hostInfo import *
from random import randint

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()
randSelect = False

cur.execute("SELECT DISTINCT clientID, subacctid FROM clients")
allClientData = cur.fetchall()[0:]


cur.execute("DROP TABLE algo_exclude_clients")
db.commit()

cur.execute("CREATE TABLE algo_exclude_clients(clientID VARCHAR(45),subacctID VARCHAR(45),effective VARCHAR(1),reason VARCHAR(255))")
db.commit()

for row in allClientData:
    if (bool(row[0])):
        cur.execute("INSERT INTO algo_exclude_clients (clientID, subacctID, effective, reason) VALUE (\'" + row[0] + "\', \'" + row[1] + "\', \'N\', \'\')")        
        db.commit()

cur.execute("SELECT * FROM algo_exclude_clients ")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been put in the TABLE algo_exclude_clients!!!")
