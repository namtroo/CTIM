#!/usr/bin/env python3

import configparser

class Init():

    def __init__(self) -> None:
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        if "mode" in cf.sections():
            self.run_mode = cf["mode"]["run"]
            self.run_interval = cf["mode"]["interval"]
            self.run_role = cf["mode"]["role"]
        else:
            self.run_mode = "web"
            self.run_interval = "5"
            self.run_role = "branch"

        if "spec" in cf.sections():
            self.has_cpu = cf["spec"]["cpu"]
            self.has_gpu = cf["spec"]["gpu"]
            self.has_hdd = cf["spec"]["hdd"]
        else:
            self.has_cpu = True
            self.has_gpu = True
            self.has_hdd = True
        
        if "sqlite" in cf.sections():
            self.sqlite_path = cf["sqlite"]["path"]
        else:
            self.sqlite_path = "history.db"

        if "telegram" in cf.sections():
            self.has_telegram = True
            self.telegram_token = cf["telegram"]["token"]
            self.telegram_chat_id = cf["telegram"]["chat_id"]
        else:
            self.has_telegram = False

        if "exporter" in cf.sections():
            self.has_exporter = True
            self.export_format = cf["exporter"]["format"]
        else:
            self.has_exporter = False

        # generate API key here
        if "api" in cf.sections():
            if cf["api"]["key"] != "":
                self.has_api = True
                self.api_key = cf["api"]["key"]
            else:
                self.has_api = False
        else:
            self.has_api = False
        
        

