#!/usr/bin/env python3
import sqlite3
from datetime import datetime

class Writer:
    def __init__(self, db_name): #db_name will define in config.py
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS system_info
                            (id INTEGER PRIMARY KEY,
                            date DATETIME NOT NULL,
                            cpu_info REAL NOT NULL,
                            gpu_info REAL NOT NULL,
                            disk_info REAL NOT NULL,
                            mem_info REAL NOT NULL,
                            net_info REAL NOT NULL
                            )''')
        self.conn.commit()

    def insert_data(self, cpu_info, gpu_info, disk_info, mem_info, net_info):
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cur.execute("INSERT INTO system_info (cpu_info, gpu_info, disk_info, mem_info, net_info, date) VALUE (?, ?, ?, ?, ?, ?)",
                    (cpu_info, gpu_info, disk_info, mem_info, net_info, date_time))
        self.conn.commit()

    def get_data(self):
        self.cur.execute("SELECT * FROM system_info")
        rows = self.cur.fetchall()
        return rows

    def close_connection(self):
        self.cur.close()
        self.conn.close()