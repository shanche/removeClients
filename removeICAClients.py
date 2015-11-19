import MySQLdb
from hostInfo_yoda import *

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()


exClientID = []
exSubacctID = []

cur.execute("SELECT clientid, subacctid FROM clients WHERE statement <> \'FICA\'")
db.commit()
ClientToExclude = cur.fetchall()[0:]

for row in ClientToExclude:
    if (bool(row[0])):
        exClientID.append(row[0])
        exSubacctID.append(row[1])

for i in range(len(exClientID)):
    cur.execute("INSERT algo_exclude_clients (clientID, subacctID, effective, reason) VALUE (\'" + exClientID[i] + "\', \'" + exSubacctID[i] + "\', 'Y', \'removeICA\')")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")

db.close()
