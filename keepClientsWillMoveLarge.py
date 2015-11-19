import MySQLdb
from hostInfo import *
#####################INPUTS################################################
percent = 0.6
###########################################################################

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()

cur.execute("SELECT clientid, subacctid FROM algo_exclude_clients where effective = \'Y\'")
db.commit()
rmClients = cur.fetchall()[0:]

cur.execute("SELECT fdiccert,bankaba,bankaccount,SUM(amount) AS currentbalance FROM fisagl WHERE account=1000 GROUP BY fdiccert,bankaba,bankaccount ORDER BY fdiccert,bankaba,bankaccount")
db.commit()
bankBalance = cur.fetchall()[0:]
Bank = {}
for row in bankBalance:
    if (bool(row[1])):
        Bank.update({row[1] + row[2]:abs(float(row[3]))})
    


cur.execute("SELECT clientid, subacctid, bankaba, bankaccount, SUM(Amount) AS Amount FROM fisagl WHERE account=\'1001\' GROUP BY clientid, subacctid, bankaba, bankaccount ORDER BY clientid DESC")
db.commit()
curAlloc = cur.fetchall()[0:]
ClientBank = {}
for row in curAlloc:
    if (bool(row[0])):
        ClientBank.update({row[0] + row[1] + row[2] + row[3]:abs(float(row[4]))})   


for row in rmClients:
    if (bool(row[0])):
        for key in Bank.keys():        
            if (bool(ClientBank.get(row[0] + row[1] + key)) & bool(Bank.get(key))):
                if ((ClientBank.get(row[0] + row[1] + key)/Bank.get(key)) > percent):
                    cur.execute("UPDATE algo_exclude_clients SET effective = \'N\', reason = \'Important client\' WHERE clientID = \'" + row[0] + "\'AND subacctID = \'" + row[1] + "\'")
                    db.commit()

cur.execute("SELECT * FROM algo_exclude_clients WHERE reason = \'Important client\' ")
db.commit()
kpClients = cur.fetchall()[0:]

print(str(len(kpClients)) + " important clients have been disabled in the TABLE algo_exclude_clients!!!")

db.close()


                    

                
    
 
