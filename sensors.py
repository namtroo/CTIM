#!/usr/bin/env python3
 
import json
import config
import psutil
import time
import platform
import socket
import re
import uuid

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

class Windows:
    
    def __init__(self):
        import wmi
        self.w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        self.temperature_infos = self.w.Sensor()
        self.cpu_temp = None
        self.gpu_temp = None
        self.disk_temp = None

    def get_temperature(self):
        for sensor in self.temperature_infos:
            if sensor.SensorType == 'Temperature':
                if 'CPU' in sensor.Name:
                    self.cpu_temp = sensor.Value
                elif 'GPU' in sensor.Name:
                    self.gpu_temp = sensor.Value
                elif 'Disk' in sensor.Name:
                    self.disk_temp = sensor.Value

class Linux:

    def __init__(self):
        self.cpu_temp = None
        self.gpu_temp = None
        self.disk_temp = None

    def get_temperature(self):
        # not all the time we have coretemp
        sensors_dict = psutil.sensors_temperatures()
        for sensor_key in sensors_dict.keys():
            if "pch" in sensor_key: #TODO: add more keyword here for detection
                self.gpu_temp = sensors_dict[sensor_key][0].current
            if "coretemp" in sensor_key:
                self.cpu_temp = sensors_dict[sensor_key][0].current
            if "nvme" in sensor_key: #TODO: add more keyword here for detection
                self.disk_temp = sensors_dict[sensor_key][0].current

class Init:
    
    def __init__(self, config: config.Init):
        platform_name = platform.uname()[0]
        
        # globals()[platform_name]
        if platform_name == "Windows":
            self.client = Windows()
        elif platform_name == "Linux":
            self.client = Linux()
        else:
            pass

        self.interval = config.run_interval

        self.platform = platform.system()
        self.platform_release = platform.release()
        self.platform_version = platform.version()
        self.architecture = platform.machine()
        self.hostname = socket.gethostname()
        self.ip_address = str()
        self.mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.processor = platform.processor()
        self.total_ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"

    def json_temp(self):
        # initialize with number of CPU and number of GPU from detector
        json_result = {
            "time": round(time.time() * 1000),
            "cpu_temp": self.client.cpu_temp, 
            "gpu_temp": self.client.gpu_temp, 
            "disk_temp": self.client.disk_temp,
        }
        return json.dumps(json_result)

    def json_specs(self):
        json_result = {
            "platform": self.platform,
            "processor": self.processor,
            "total_ram": self.total_ram, 
            "platform_release": self.platform_release,
            "platform_version": self.platform_version,
            "architecture": self.architecture,
            "hostname": self.hostname,
            "ip_address": self.ip_address,
            "mac_address": self.mac_address,
        }
        return json.dumps(json_result)

    def update(self):
        while True:
            time.sleep(int(self.interval))
            self.ip_address = get_local_ip()
            self.client.get_temperature()