from creatRemoveClientsTable import *

exClientID = []
exSubacctID = []

cur.execute("SELECT clientid, subacctid FROM clients WHERE statement = \'FICA\'")
db.commit()
ClientToExclude = cur.fetchall()[0:]

for row in ClientToExclude:
    if (bool(row[0])):
        exClientID.append(row[0])
        exSubacctID.append(row[1])

for i in range(len(exClientID)):
    cur.execute("UPDATE algo_exclude_clients SET effective = \'Y\' WHERE clientID = \'" + exClientID[i] + "\'AND subacctID = \'" + exSubacctID[i] + "\'")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")
