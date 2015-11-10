from creatRemoveClientsTable import *

lowerLimit = 1000

exClientID = []
exSubacctID = []

cur.execute("SELECT bankaba,bankaccount, clientid, subacctid, availablebalance  FROM clients WHERE availablebalance > " + str(lowerLimit))
db.commit()
ClientToExclude = cur.fetchall()[0:]
exClientID = []
exSubacctID = []
    

for row in ClientToExclude:
    if (bool(row[2])):
        exClientID.append(row[2])
        exSubacctID.append(row[3])
            
for i in range(len(exClientID)):
    cur.execute("UPDATE algo_exclude_clients SET effective = \'Y\' WHERE clientID = \'" + exClientID[i] + "\'AND subacctID = \'" + exSubacctID[i] + "\'")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")
