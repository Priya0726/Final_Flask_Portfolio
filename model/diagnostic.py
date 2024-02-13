import sqlite3

# Create or connect to the database
conn = sqlite3.connect('mental_health.db')
c = conn.cursor()

# Create table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS responses (
                id INTEGER PRIMARY KEY,
                tiredness TEXT,
                irritability TEXT,
                stress TEXT,
                meaning_of_life TEXT,
                hopelessness TEXT,
                appetite_issues TEXT,
                sleep_issues TEXT
            )''')

def analyze_responses():
    c.execute('SELECT * FROM responses')
    responses = c.fetchall()

    total_responses = len(responses)
    always_count = 0
    sometimes_count = 0
    never_count = 0

    for response in responses:
        tiredness = response[1]
        if tiredness == 'always':
            always_count += 1
        elif tiredness == 'sometimes':
            sometimes_count += 1
        elif tiredness == 'never':
            never_count += 1

    if always_count > sometimes_count and always_count > never_count:
        return 'likely to have depression'
    elif sometimes_count > always_count and sometimes_count > never_count:
        return 'possibly'
    else:
        return 'most likely do not have depression'

def insert_response(tiredness, irritability, stress, meaning_of_life, hopelessness, appetite_issues, sleep_issues):
    c.execute('''INSERT INTO responses (tiredness, irritability, stress, meaning_of_life, hopelessness, appetite_issues, sleep_issues)
                VALUES (?, ?, ?, ?, ?, ?, ?)''', (tiredness, irritability, stress, meaning_of_life, hopelessness, appetite_issues, sleep_issues))
    conn.commit()

# Example usage
insert_response('always', 'sometimes', 'never', 'sometimes', 'always', 'never', 'sometimes')
result = analyze_responses()
print('Result:', result)

# Close the database connection
conn.close()
