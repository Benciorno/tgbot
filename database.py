import sqlite3


database = sqlite3.connect('profiler.db')
cursor = database.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS profile(
    telegram_id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag VARCHAR(30),
    number INTEGER,
    name VARCHAR(100),
    birthdate VARCHAR(100),
    description VARCHAR(100)
)
''')
database.commit()
database.close()