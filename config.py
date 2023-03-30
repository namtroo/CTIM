#!/usr/bin/env python3

import configparser

class Init():

    def __init__(self) -> None:
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        if "telegram" in cf.sections():
            self.has_telegram = True
            self.telegram_token = cf["telegram"]["token"]
            self.telegram_chat_id = cf["telegram"]["chat_id"]
        else:
            self.has_telegram = False
        
        if "mode" in cf.sections():
            self.run_mode = cf["mode"]["run"]
        else:
            self.run_mode = "web"
        
        if "sqlite" in cf.sections():
            self.sqlite_path = cf["sqlite"]["path"]
        else:
            self.sqlite_path = "history.db"

        if "exporter" in cf.sections():
            self.has_exporter = True
            self.export_format = cf["exporter"]["format"]
        else:
            self.has_exporter = False

