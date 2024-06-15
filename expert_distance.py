import sqlite3
from math import radians, sin, cos, sqrt, atan2

LOC = None

# Define the haversine function
def haversine(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    R = 6371.0
    return R * c

# Define the function to find closest experts
def find_closest_experts(farmer_lat, farmer_lon, num_experts=3):
    connection = sqlite3.connect("testdata.db")
    cursor = connection.cursor()

    cursor.execute("SELECT PHONE, NAME, LOCATION FROM EXPERT")

    experts = []
    for row in cursor.fetchall():
        phone, name, location = row
        location = location.replace("(", "").replace(")", "")
        lat, lon = map(float, location.split(','))
        distance = haversine(farmer_lat, farmer_lon, lat, lon)
        experts.append((phone, name, distance))

    experts.sort(key=lambda x: x[2])
    closest_experts = experts[:num_experts]

    connection.close()
    return closest_experts

# Define the function to get farmer and closest experts
def get_farmer_and_closest_experts(farmer_phone):
    global LOC
    connection = sqlite3.connect("testdata.db")
    cursor = connection.cursor()

    cursor.execute("SELECT LOCATION FROM FARMER WHERE PHONE=?", (farmer_phone,))
    
    location = cursor.fetchone()
    if isinstance(location, type(None)):
        location = LOC
    else:
        LOC = location
    # print(location)
    farmer_location = location[0]
    farmer_location = farmer_location.replace("(", "").replace(")", "")

    if farmer_location is None or "none" in farmer_location.lower():
        farmer_lat, farmer_lon = 0, 0
    else:
        farmer_lat, farmer_lon = map(float, farmer_location.split(','))

    closest_experts = find_closest_experts(farmer_lat, farmer_lon, num_experts=3)

    cursor.execute("SELECT * FROM FARMER WHERE PHONE=?", (farmer_phone,))
    farmer_details = cursor.fetchone()

    connection.close()

    return closest_experts

# # Create tables and insert data
# connection = sqlite3.connect("test2data.db")

# connection.execute(
# '''CREATE TABLE FARMER
# (
# PHONE VARCHAR(10) PRIMARY KEY NOT NULL,
# NAME VARCHAR(50) NOT NULL, 
# PASSWORD VARCHAR(20) NOT NULL,
# LOCATION VARCHAR(100)
# );''')

# connection.execute(
# '''CREATE TABLE EXPERT
# (
# PHONE VARCHAR(10) PRIMARY KEY NOT NULL,
# NAME VARCHAR(50) NOT NULL, 
# EMAIL VARCHAR(50) NOT NULL,
# PASSWORD VARCHAR(20) NOT NULL,
# LOCATION VARCHAR(100) NOT NULL
# );''')

# # Inserting data into FARMER table
# connection.execute("INSERT INTO FARMER (PHONE, NAME, PASSWORD, LOCATION) VALUES (?, ?, ?, ?)",
#                    ("1234567890", "John Doe", "password123", "37.7749,-122.4194"))
# connection.execute("INSERT INTO FARMER (PHONE, NAME, PASSWORD, LOCATION) VALUES (?, ?, ?, ?)",
#                    ("0987654321", "Jane Smith", "securepass", "38.8951,-77.0364"))
# connection.execute("INSERT INTO FARMER (PHONE, NAME, PASSWORD, LOCATION) VALUES (?, ?, ?, ?)",
#                    ("5555555555", "Bob Farmer", "farmerpass", "34.0522,-118.2437"))
# connection.execute("INSERT INTO FARMER (PHONE, NAME, PASSWORD, LOCATION) VALUES (?, ?, ?, ?)",
#                    ("6666666666", "Alice Farmer", "farmpass", "40.7128,-74.0060"))
# connection.execute("INSERT INTO FARMER (PHONE, NAME, PASSWORD, LOCATION) VALUES (?, ?, ?, ?)",
#                    ("7777777777", "Charlie Farmer", "farming123", "41.8781,-87.6298"))

# # Inserting data into EXPERT table
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
# connection.close()

# # Get details of a farmer and the three closest experts
# farmer_details, closest_experts = get_farmer_and_closest_experts("1234567890")

# # Print the results
# print("Selected Farmer Details:")
# print(f"Phone: {farmer_details[0]}, Name: {farmer_details[1]}, Password: {farmer_details[2]}, Location: {farmer_details[3]}\n")

# print("Closest Experts:")
# for expert in closest_experts:
#     print(f"Name: {expert[1]}, Phone: {expert[0]}, Distance: {expert[2]}")
