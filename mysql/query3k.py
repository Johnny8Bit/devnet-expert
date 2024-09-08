
import mysql.connector
import time


def open_db_session():
  
    db_session = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="WiFi"
    )
    return db_session


def query_db(session):
   
    cursor = session.cursor()

    query = ("SELECT Ap.ApName, Slot.RadioMac, Slot.Clients "
             "FROM Slot JOIN Ap ON Ap.ApName=Slot.ApName "
             "WHERE Slot.Status='enabled' AND Slot.Mode='client-serving' AND Slot.Band='6'")
  
    cursor.execute(query)

    for ap_name, radio_mac, clients in cursor:
        print(f"AP: {ap_name} with radio MAC {radio_mac} has {clients} clients")

    cursor.close()



if __name__ == '__main__':

    db = open_db_session()

    tic = time.time()
    query_db(db)
    toc = time.time()
    
    print(toc - tic)

    db.close()

