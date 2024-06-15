import sqlite3

connection = sqlite3.connect('testdata.db', check_same_thread=False)

def insert_farmer(phone, name, password, location=None):
    command = f"INSERT INTO FARMER VALUES('{phone}', '{name}', '{password}', '{location}');"

    connection.execute(command)
    connection.commit()


def update_location_farmer(phone, location):
    command = f"UPDATE FARMER SET LOCATION='{location}' WHERE PHONE='{phone}';"

    connection.execute(command)
    connection.commit()

def get_login_details_farmer(phone, password):
    command = f"SELECT * FROM FARMER WHERE PHONE='{phone}' AND PASSWORD='{password}';"
    # print(command)

    cursor = connection.cursor()

    cursor.execute(command)
    result = cursor.fetchone()

    # print(result)

    if not isinstance(result, type(None)):
        if len(result) != 0:
            return True

    return False

def insert_expert(phone, name, email, password, location=None):
    command = f"INSERT INTO EXPERT VALUES('{phone}', '{name}', '{email}', '{password}', '{location}');"

    connection.execute(command)

    connection.commit()


def update_location_expert(email, location):
    command = f"UPDATE EXPERT SET LOCATION='{location}' WHERE EMAIL='{email}';"

    connection.execute(command)
    connection.commit()

def get_login_details_expert(email, password):
    command = f"SELECT * FROM EXPERT WHERE EMAIL='{email}' AND PASSWORD='{password}';"
    # print(command)

    cursor = connection.cursor()

    cursor.execute(command)
    result = cursor.fetchone()

    # print(result)

    if not isinstance(result, type(None)):
        if len(result) != 0:
            return True

    return False

# connection.execute("INSERT INTO EXPERT (PHONE, NAME, EMAIL, PASSWORD, LOCATION) VALUES (?, ?, ?, ?, ?)",
#                    ("1111111111", "Bob Expert", "bob@example.com", "expertpass", "37.7749,-122.4194"))
# connection.execute("INSERT INTO EXPERT (PHONE, NAME, EMAIL, PASSWORD, LOCATION) VALUES (?, ?, ?, ?, ?)",
#                    ("2222222222", "Alice Wise", "alice@example.com", "wisepass", "38.8951,-77.0364"))
# connection.execute("INSERT INTO EXPERT (PHONE, NAME, EMAIL, PASSWORD, LOCATION) VALUES (?, ?, ?, ?, ?)",
#                    ("3333333333", "Charlie Advisor", "charlie@example.com", "advisepass", "34.0522,-118.2437"))
# connection.execute("INSERT INTO EXPERT (PHONE, NAME, EMAIL, PASSWORD, LOCATION) VALUES (?, ?, ?, ?, ?)",
#                    ("4444444444", "David Consultant", "david@example.com", "consultpass", "40.7128,-74.0060"))
# connection.execute("INSERT INTO EXPERT (PHONE, NAME, EMAIL, PASSWORD, LOCATION) VALUES (?, ?, ?, ?, ?)",
#                    ("5555555555", "Eve Guru", "eve@example.com", "gurupass", "41.8781,-87.6298"))
# connection.commit()
