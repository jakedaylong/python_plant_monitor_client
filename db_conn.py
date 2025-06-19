'''Database connection and operations for storing planter information.'''
import sqlite3


def init_conn():
    '''Initialize the database connection and create the table if it does not exist.'''
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
    '''Push data to the database.'''
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO planter_info (planter_number, wetness, humidity, air_temp) VALUES (1, ?, ?, ?)
        ''', (planter_data['wetness'], planter_data['humidity'],planter_data['temp']))
    
    conn.commit()