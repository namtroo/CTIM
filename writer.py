#!/usr/bin/env python3
import config
import query
import json

import sqlite3
import time


class Init:

    def __init__(self, config: config.Init): #db_name will define in config.py
        self.db_name = config.sqlite_path
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.interval = config.run_interval
        self.history = config.sqlite_history
        self.branches_info = config.branches_info
        self.create_table()

    def create_table(self):
        # create extra table for statistics here
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS sensors_history
            (id INTEGER PRIMARY KEY,
            branch_name STRING NOT NULL,
            date DATETIME NOT NULL,
            cpu_temp REAL NOT NULL,
            gpu_temp REAL NOT NULL,
            disk_temp REAL NOT NULL)'''
        )
        self.conn.commit()

    # functions with multiple variables

    # insert data using query instead of direct sensors
    # good for networking stuff

    def insert_data(self):
        # loop over all config
        for branch in self.branches_info:
            q = query.Init(branch["url"])
            result = q.start("sensors")
            sensors_json = json.loads(result)
            self.cur.execute("INSERT INTO sensors_history (branch_name, cpu_temp, gpu_temp, disk_temp, date) VALUES (?, ?, ?, ?, ?)",
                        (branch["name"], sensors_json["cpu_temp"], sensors_json["gpu_temp"], sensors_json["disk_temp"], sensors_json["time"]))
        self.conn.commit()

    def close_connection(self):
        self.cur.close()
        self.conn.close()

    def clean(self):
        # clean the db if amount of line is greater than in config.ini
        # how often to clean
        self.cur.execute("SELECT COUNT(*) FROM sensors_history")
        rows_count = self.cur.fetchall()[0][0]
        if rows_count > int(self.history):
            number_to_del = rows_count - int(self.history)
            # do something with old entries here
            self.cur.execute(
                '''delete from sensors_history where id IN 
                (SELECT id from sensors_history order by newsid asc limit ?)
                ''', (number_to_del)
            )

    def update(self):
        time.sleep(1) # wait for sensor API up
        while True: # continuous write
            # get sensors data from web API
            for i in range(10): # self clean every 10 insertions
                time.sleep(int(self.interval))
                self.insert_data()
                print("insert data")
            self.clean()        