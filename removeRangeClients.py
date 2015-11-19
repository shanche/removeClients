import MySQLdb
from hostInfo import *

#####################INPUTS################################################
lowerLimit = 1000
upperLimit = 100000
###########################################################################

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()

if (lowerLimit > upperLimit):
    print("Please check the range settings!!!")
    

exClientID = []
exSubacctID = []

cur.execute("SELECT bankaba,bankaccount, clientid, subacctid, availablebalance  FROM clients WHERE availablebalance > " + str(lowerLimit) + " AND availablebalance < " + str(upperLimit))
db.commit()
ClientToExclude = cur.fetchall()[0:]
exClientID = []
exSubacctID = []
    

for row in ClientToExclude:
    if (bool(row[2])):
        exClientID.append(row[2])
        exSubacctID.append(row[3])
            
for i in range(len(exClientID)):
    cur.execute("INSERT algo_exclude_clients (clientID, subacctID, effective, reason) VALUE (\'" + exClientID[i] + "\', \'" + exSubacctID[i] + "\', 'Y', \'Range\')")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")

db.close()
