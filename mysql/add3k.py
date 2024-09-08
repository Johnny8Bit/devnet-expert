#Adds 3000 random APs in to database

import mysql.connector
import random


def open_db_session():
  
    db_session = mysql.connector.connect(
        host="localhost",
        user="",
        password="",
        database="WiFi"
    )
    return db_session


def random_mac():
  
    values = "0123456789ABCDEF"
    random_string = ""
    for length in range(0, 12):
        random_string += random.choice(values)

    mac = ".".join(random_string[x:x + 2] for x in range(0, len(random_string), 2))

    return mac


def random_site():

    return random.choice(["Site1", "Site2", "Site3"])


def random_band():

    return random.choice(["2.4", "5", "6"])


def random_status():

    return random.choice(["enabled", "disabled"])


def random_mode():

    return random.choice(["client-serving", "monitor"])


def random_clients():

    return random.randint(0, 100)


def random_utilization():

    return random.randint(0, 100)


def write_db(session):

    cursor = session.cursor()

    for ap_count in range(1, 3001):
        ap_name = f"AP-{ap_count}"
        query = (f"REPLACE INTO Ap VALUES ('{ap_name}', '{random_mac()}', '{random_site()}')")
        cursor.execute(query)
    
    session.commit()

    for ap_count in range(1, 3001):
        ap_name = f"AP-{ap_count}"
        for slot_count in range(1, 5):
            query = (f"REPLACE INTO Slot VALUES ('{random_mac()}', '{ap_name}', '{random_band()}', '{random_status()}', '{random_mode()}', '{random_clients()}', '{random_utilization()}', {slot_count})")
            cursor.execute(query)

    session.commit()

    cursor.close()


if __name__ == '__main__':

    db = open_db_session()

    write_db(db)

    db.close()