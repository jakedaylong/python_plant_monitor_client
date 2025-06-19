import sqlite3

def init_conn():
    conn = sqlite3.connect('plant_info.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS planter_info (
                id INTEGER PRIMARY KEY,
                planter_number INTEGER NOT NULL,
                wetness INTEGER NOT NULL,
                humidity FLOAT NOT NULL,
                air_temp FLOAT NOT NuLL
                )
                ''')
    return conn

def push_data(conn, planter_data):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO planter_info (planter_number, wetness, humidity, air_temp) VALUES (1, ?, ?, ?)
        ''', (planter_data['wetness'], planter_data['humidity'],planter_data['temp']))
    
    conn.commit()