import sqlite3

def init_db():
    conn = sqlite3.connect("checkin_system.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS visitors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT, 
                        email TEXT, 
                        purpose TEXT, 
                        checkin_time TEXT,
                        status TEXT DEFAULT 'Pending')''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS admins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE, 
                        password TEXT)''')
    
    conn.commit()
    conn.close()

init_db()
