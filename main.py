#!/usr/bin/env python3

import config
import sensors
import exporter
import writer
import time

from flask import Flask, render_template, make_response
from flask_cors import CORS
from threading import Thread

if __name__ == "__main__":
    cf = config.Init()
    new_sensors = sensors.Init(cf)
    new_exporter = exporter.Init(cf)
    new_writer = writer.Init(cf)

    # threading reading, write to history here
    Thread(target=new_sensors.update).start()
    Thread(target=new_writer.update).start()

    # change to CherryPy to maintain  OOP approach here
    app = Flask(__name__)
    CORS(app)

    if len(cf.branches_info) > 0:
        @app.route("/", methods=["GET"])
        def main_app():
            return render_template("index.html")

    @app.route("/sensors", methods=["GET"])
    def main_api():
        resp = make_response(new_sensors.json_temp())
        resp.content_type = "application/json"
        return resp

    @app.route("/configs", methods=["GET"])
    def main_configs():
        resp = make_response(cf.jsonified())
        resp.content_type = "application/json"
        return resp

    @app.route("/specs", methods=["GET"])
    def main_specs():
        resp = make_response(new_sensors.json_specs())
        resp.content_type = "application/json"
        return resp

    @app.route("/export", methods=["GET"])
    def main_export():
        new_exporter.write_csv()
        return

    # app.jinja_env.auto_reload = True
    # app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.run(host='0.0.0.0', port=cf.run_port)
    