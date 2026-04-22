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
#inline comments gets computed using diff with flags/suggestions by putting diff into claude api once, those comments NEED to match the correct lines but arent mapping correctly to github code. HOWEVER, the content of the inline commnets are correct and those comments go into claude for a second pass to create a summary of the issues.

#First call — reads the diff, finds issues, returns JSON like [{file, position, severity, comment}] — these are the intended inline comments
#Second call — takes that list of issues and writes a formatted markdown summar
