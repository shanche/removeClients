import MySQLdb
from hostInfo_yoda import *

#####################INPUTS################################################
kpClientID = []
kpSubacctID = []
# the clientid and subacctid must inserted together, even if it is empty
kpClientID.append("104790450688") 
kpSubacctID.append("")
###########################################################################

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()

cur.execute("SELECT DISTINCT clientID, subacctid FROM clients")
allClientData = cur.fetchall()[0:]

exClientID = []
exSubacctID = []

for row in allClientData:
    if (row[0] in kpClientID):
        if (row[1] == kpSubacctID[kpClientID.index(row[0])]):
            exClientID.append()
            exSubacctID.append()

for row in allClientData:    
    cur.execute("INSERT algo_exclude_clients (clientID, subacctID, effective, reason) VALUE (\'" + row[0] + "\', \'" + row[1] + "\', 'Y', \'Not include\')")
    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients where reason = \'Not include\'")
db.commit()
rmClients = cur.fetchall()[0:]

print(str(len(rmClients)) + " clients have been removed from the allocation!!!")

db.close()
