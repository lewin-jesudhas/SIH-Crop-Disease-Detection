# import sqlite3

# # Connect to the database (or create it if it doesn't exist)
# conn = sqlite3.connect('tomato_care.db')
# c = conn.cursor()

# # Create tables
# c.execute('''
#     CREATE TABLE conditions (
#         id INTEGER PRIMARY KEY,
#         condition TEXT,
#         description TEXT
#     )
# ''')

# c.execute('''
#     CREATE TABLE pesticides (
#         id INTEGER PRIMARY KEY,
#         condition_id INTEGER,
#         pesticide TEXT,
#         FOREIGN KEY (condition_id) REFERENCES conditions(id)
#     )
# ''')

# c.execute('''
#     CREATE TABLE fertilizers (
#         id INTEGER PRIMARY KEY,
#         condition_id INTEGER,
#         fertilizer TEXT,
#         FOREIGN KEY (condition_id) REFERENCES conditions(id)
#     )
# ''')

# # Insert data
# conditions_data = [
#     ('Early Blight', 'Warm and humid weather, caused by Alternaria solani. Affects leaves, stems, fruit, and other parts.'),
#     ('Late Blight', 'Cool, wet conditions, caused by Phytophthora infestans. Affects leaves, stems, fruit, and other parts.'),
#     ('Healthy Plant', 'Vibrant green leaves, sturdy stalks, no drooping. Well-nurtured and cared for.')
# ]

# pesticides_data = [
#     (1, 'Mancozeb'),
#     (1, 'Chlorothalonil'),
#     (1, 'Azoxystrobin + Difenoconazole'),
#     (2, 'Copper Oxychloride Fungicide'),
#     (2, 'Trichoderma viride'),
#     (2, 'Sulphur-Based Fungicides'),
#     (2, 'Biofungicides with Neem Extracts'),
#     (3, 'Bicarbonate-Based Fungicides'),
#     (3, 'Trichoderma harzianum')
# ]

# fertilizers_data = [
#     (1, 'Espoma Tomato-tone Organic Fertilizer'),
#     (1, 'Miracle-Gro Water Soluble Tomato Plant Food'),
#     (2, 'Neem Cake'),
#     (2, 'Vermicompost'),
#     (2, 'NPK Fertilizers')
# ]

# c.executemany('INSERT INTO conditions (condition, description) VALUES (?, ?)', conditions_data)
# c.executemany('INSERT INTO pesticides (condition_id, pesticide) VALUES (?, ?)', pesticides_data)
# c.executemany('INSERT INTO fertilizers (condition_id, fertilizer) VALUES (?, ?)', fertilizers_data)

# # Commit changes and close connection
# conn.commit()
# conn.close()

import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('tomato_care.db')
c = conn.cursor()

# Drop tables if they exist
c.execute('DROP TABLE IF EXISTS conditions')
c.execute('DROP TABLE IF EXISTS pesticides')
c.execute('DROP TABLE IF EXISTS fertilizers')

# Create tables
c.execute('''
    CREATE TABLE conditions (
        id INTEGER PRIMARY KEY,
        condition TEXT,
        description TEXT
    )
''')

c.execute('''
    CREATE TABLE pesticides (
        id INTEGER PRIMARY KEY,
        condition_id INTEGER,
        pesticide TEXT,
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
    )
''')

c.execute('''
    CREATE TABLE fertilizers (
        id INTEGER PRIMARY KEY,
        condition_id INTEGER,
        fertilizer TEXT,
        FOREIGN KEY (condition_id) REFERENCES conditions(id)
    )
''')

# Insert data
conditions_data = [
    ('Early Blight', 'Warm and humid weather, caused by Alternaria solani. Affects leaves, stems, fruit, and other parts.'),
    ('Late Blight', 'Cool, wet conditions, caused by Phytophthora infestans. Affects leaves, stems, fruit, and other parts.'),
    ('Healthy Plant', 'Vibrant green leaves, sturdy stalks, no drooping. Well-nurtured and cared for.')
]

pesticides_data = [
    (1, 'Mancozeb'),
    (1, 'Chlorothalonil'),
    (1, 'Azoxystrobin + Difenoconazole'),
    (2, 'Copper Oxychloride Fungicide'),
    (2, 'Trichoderma viride'),
    (2, 'Sulphur-Based Fungicides'),
    (2, 'Biofungicides with Neem Extracts'),
    (3, 'Bicarbonate-Based Fungicides'),
    (3, 'Trichoderma harzianum')
]

fertilizers_data = [
    (1, 'Espoma Tomato-tone Organic Fertilizer'),
    (1, 'Miracle-Gro Water Soluble Tomato Plant Food'),
    (2, 'Neem Cake'),
    (2, 'Vermicompost'),
    (2, 'NPK Fertilizers'),
    (3, 'Neem Cake'),
    (3, 'Vermicompost'),
    (3, 'NPK Fertilizers')
]

c.executemany('INSERT INTO conditions (condition, description) VALUES (?, ?)', conditions_data)
c.executemany('INSERT INTO pesticides (condition_id, pesticide) VALUES (?, ?)', pesticides_data)
c.executemany('INSERT INTO fertilizers (condition_id, fertilizer) VALUES (?, ?)', fertilizers_data)

# Commit changes
conn.commit()

# Display tables
c.execute('SELECT * FROM conditions')
conditions_data = c.fetchall()
print("Conditions Table:")
print("ID | Condition       | Description")
print("-----------------------------")
for row in conditions_data:
    print(f"{row[0]:2d} | {row[1]:15s} | {row[2]}")

c.execute('SELECT * FROM pesticides')
pesticides_data = c.fetchall()
print("\nPesticides Table:")
print("ID | Condition ID | Pesticide")
print("-----------------------------")
for row in pesticides_data:
    print(f"{row[0]:2d} | {row[1]:12d} | {row[2]}")

c.execute('SELECT * FROM fertilizers')
fertilizers_data = c.fetchall()
print("\nFertilizers Table:")
print("ID | Condition ID | Fertilizer")
print("-----------------------------")
for row in fertilizers_data:
    print(f"{row[0]:2d} | {row[1]:12d} | {row[2]}")

# Close connection
conn.close()
