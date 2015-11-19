# Put all the clients in the table, set effective as "N"
# Written by SHAN CHE, Nov. 10, 2015

import MySQLdb
#from hostInfo_prod import *
from hostInfo_yoda import *

db = MySQLdb.connect(host = host_,user = user_, passwd = password_, db = datebase_)
cur = db.cursor()




cur.execute("DROP TABLE algo_exclude_clients")
db.commit()

cur.execute("CREATE TABLE algo_exclude_clients(clientID VARCHAR(45),subacctID VARCHAR(45),effective VARCHAR(1),reason VARCHAR(255))")
db.commit()


db.close()
