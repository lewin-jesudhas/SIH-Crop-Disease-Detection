# # import sqlite3

# # # Connect to the database
# # conn = sqlite3.connect('tomato_care.db')
# # c = conn.cursor()

# # # Define a function to display data for a specific condition
# # def display_condition_data(condition):
# #     c.execute('SELECT * FROM conditions WHERE condition=?', (condition,))
# #     condition_data = c.fetchone()

# #     if condition_data:
# #         print(f"Condition: {condition_data[1]}")
# #         print(f"Description: {condition_data[2]}\n")

# #         c.execute('SELECT pesticide FROM pesticides INNER JOIN conditions ON conditions.id = pesticides.condition_id WHERE conditions.condition=?', (condition,))
# #         pesticides_data = c.fetchall()
# #         print("Pesticides:")
# #         for row in pesticides_data:
# #             print(row[0])

# #         c.execute('SELECT fertilizer FROM fertilizers INNER JOIN conditions ON conditions.id = fertilizers.condition_id WHERE conditions.condition=?', (condition,))
# #         fertilizers_data = c.fetchall()
# #         print("\nFertilizers:")
# #         for row in fertilizers_data:
# #             print(row[0])
# #     else:
# #         print(f"No data found for condition: {condition}\n")

# # # Extract data for Healthy Plant
# # display_condition_data('Healthy Plant')

# # # Extract data for Early Blight
# # display_condition_data('Early Blight')

# # # Extract data for Late Blight
# # display_condition_data('Late Blight')

# # # Close connection
# # conn.close()

# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('tomato_care.db')
# c = conn.cursor()

# # Define a function to display data for a specific condition
# def display_condition_data(condition):
#     c.execute('SELECT * FROM conditions WHERE condition=?', (condition,))
#     condition_data = c.fetchone()

#     if condition_data:
#         print(f"Condition: {condition_data[1]}")
#         print(f"Description: {condition_data[2]}\n")

#         c.execute('''
#             SELECT pesticide 
#             FROM pesticides 
#             LEFT JOIN conditions ON conditions.id = pesticides.condition_id 
#             WHERE conditions.condition=?
#         ''', (condition,))
#         pesticides_data = c.fetchall()
#         print("Pesticides:")
#         for row in pesticides_data:
#             print(row[0])

#         c.execute('''
#             SELECT fertilizer 
#             FROM fertilizers 
#             LEFT JOIN conditions ON conditions.id = fertilizers.condition_id 
#             WHERE conditions.condition=?
#         ''', (condition,))
#         fertilizers_data = c.fetchall()
#         print("\nFertilizers:")
#         for row in fertilizers_data:
#             print(row[0])
#     else:
#         print(f"No data found for condition: {condition}\n")

# # Extract data for Healthy Plant
# display_condition_data('Healthy Plant')

# # Extract data for Early Blight
# display_condition_data('Early Blight')

# # Extract data for Late Blight
# display_condition_data('Late Blight')

# # Close connection
# conn.close()

import sqlite3

# Connect to the database
conn = sqlite3.connect('tomato_care.db', check_same_thread=False)
c = conn.cursor()

# Define a function to display data for a specific condition
def get_condition_data(condition):
    c.execute('SELECT * FROM conditions WHERE condition=?', (condition,))
    condition_data = c.fetchone()

    result = {}

    if condition_data:
        result["condition"] = condition_data[1]
        result["description"] = condition_data[2]

        c.execute('''
            SELECT pesticide 
            FROM pesticides 
            LEFT JOIN conditions ON conditions.id = pesticides.condition_id 
            WHERE conditions.condition=?
        ''', (condition,))
        pesticides_data = c.fetchall()
        temp = ""
        for row in pesticides_data:
            temp += row[0] + "\n"

        result["pesticides"] = temp

        temp = ""

        c.execute('''
            SELECT fertilizer 
            FROM fertilizers 
            LEFT JOIN conditions ON conditions.id = fertilizers.condition_id 
            WHERE conditions.condition=?
        ''', (condition,))
        fertilizers_data = c.fetchall()
        
        
        for row in fertilizers_data:
            temp += row[0] + "\n"
        # conn.close()

        result["fertilizers"] = temp

        return result
    else:
        result = None
        # conn.close()

        return result