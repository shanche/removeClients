import MySQLdb
from hostInfo import *

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()


kpClientID = []
kpSubacctID = []

# the clientid and subacctid must inserted together, even if it is empty
kpClientID.append("104790450688") 
kpSubacctID.append("")




cur.execute("UPDATE algo_exclude_clients SET effective = \'Y\' ")
db.commit()

for i in range(len(kpClientID)):
    cur.execute("UPDATE algo_exclude_clients SET effective = \'N\', reason = \'Not keep\' WHERE clientID = \'" + kpClientID[i] + "\'AND subacctID = \'" + kpSubacctID[i] + "\'")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")

db.close()
