#!/usr/bin/env python3

# export as document, images, pdf

import config
import pandas
import sqlite3

class Init:
    def __init__(self, config: config.Init) -> None:
        self.sqlite_path = config.sqlite_path
        pass

    # export from sqlite database
    # write to CSV

    def write_csv(self):
        conn = sqlite3.connect(self.sqlite_path, isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)
        db_df = pandas.read_sql_query("SELECT * FROM sensors_history", conn)
        db_df.to_csv('sensors_history.csv', index=False)