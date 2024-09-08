import mysql.connector


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


def write_db(session):

  cursor = session.cursor()

  query = ("INSERT INTO Ap VALUES "
           "('AP3', 'zz.zz.zz.zz.zz.zz', 'Site 2'), "
           "('AP4', 'yy.yy.yy.yy.yy.yy', 'Site 2')")
  cursor.execute(query)

  query = ("INSERT INTO Slot VALUES "
           "('11.11.11.11.11.11', 'AP3', '2.4', 'enabled', 'client-serving', '2', '32', '0'), "
           "('12.12.12.12.12.12', 'AP3', '5', 'enabled', 'client-serving', '67', '80', '1'), "
           "('13.13.13.13.13.13', 'AP3', '5', 'disabled', 'monitor', '0', '0', '2'), "
           "('21.21.21.21.21.21', 'AP4', '2.4', 'disabled', 'client-serving', '0', '0', '0'), "
           "('22.22.22.22.22.22', 'AP4', '5', 'enabled', 'client-serving', '9', '20', '1'), "
           "('23.23.23.23.23.23', 'AP4', '6', 'enabled', 'client-serving', '3', '4', '3')")
  cursor.execute(query)
  
  cursor.close()


if __name__ == '__main__':

  db = open_db_session()

  write_db(db)
  query_db(db)

  db.close()

