#!/usr/bin/env python3

import configparser
import json
import re

class Init():

    def __init__(self) -> None:
        cf = configparser.ConfigParser()
        cf.read("config.ini")

        if "mode" in cf.sections():
            self.run_mode = cf["mode"]["run"]
            self.run_port = cf["mode"]["port"] # always on API
            self.run_interval = cf["mode"]["interval"]
        else:
            self.run_mode = "web"
            self.run_port = "6000"
            self.run_interval = "5"
        
        if "sqlite" in cf.sections():
            self.sqlite_path = cf["sqlite"]["path"]
            self.sqlite_history = cf["sqlite"]["history"]
        else:
            self.sqlite_path = "history.db"
            self.sqlite_history = 500

        # generate dictionary of branch with url and token

        self.branches_info = list()
        for section in cf.sections():
            if re.search(r'branch_\d+', section) != None:
                self.branches_info.append({
                    "name": cf[section]["branch_name"],
                    "url": "http://" + cf[section]["branch_ip"] + ":" + cf[section]["branch_port"],
                })

        # edit the config.js file in static folder here
        f = open("static/config.js", "r+")
        source = f.read()
        source = re.sub(
            '(?<=interval \= )\d+', 
            self.run_interval, 
            source,
        )
        source = re.sub(
            '(?<=port \= )\d+', 
            self.run_port, 
            source,
        )
        source = re.sub(
            '(?<=branches_list = ).*(?=;)',
            json.dumps(self.branches_info),
            source,
        )
        f.seek(0)
        f.write(source)
        f.truncate()
        f.close()


    def jsonified(self):
        json_result = {
            "interval": self.run_interval,
        }
        return json.dumps(json_result)
