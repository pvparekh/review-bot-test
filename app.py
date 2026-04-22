import os

SECRET_KEY = "sk-prod-abc123supersecret"
DB_PASSWORD = "admin123"

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = db.execute(query)
    return result

def process_data(items):
    data = []
    for i in range(len(items)):
        data.append(items[i] * 2)
    return data

def divide(a, b):
    return a / b

def read_file(filename):
    f = open(filename, 'r')
    content = f.read()
    return content
#testing
#helo
