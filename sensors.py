import platform
import wmi
import psutil

class Window:
    def __init__(self):
        self.w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        self.temperature_infos = self.w.Sensor()
        self.cpu_temp = None
        self.gpu_temp = None
        self.disk_temp = None
        self.get_temperature()

    def get_temperature(self):
        for sensor in self.temperature_infos:
            if sensor.SensorType == 'Temperature':
                if 'CPU' in sensor.Name:
                    self.cpu_temp = sensor.Value
                elif 'GPU' in sensor.Name:
                    self.gpu_temp = sensor.Value
                elif 'Disk' in sensor.Name:
                    self.disk_temp = sensor.Value

    def cpu_info(self):
        return self.cpu_temp

    def gpu_info(self):
        return self.gpu_temp

    def disk_info(self):
        return self.disk_temp

class Linux:

    def __init__(self):
        self.cpu_temp = None
        self.gpu_temp = None
        self.disk_temp = None
        self.get_temperature()

    def get_temperature(self):
        for sensor in psutil.sensors_temperatures().values():
            for info in sensor:
                if 'coretemp' in info.label and not self.cpu_temp:
                    self.cpu_temp = info.current
                elif 'amdgpu' in info.label and not self.gpu_temp:
                    self.gpu_temp = info.current
                elif 'nvme' in info.label and not self.disk_temp:
                    self.disk_temp = info.current

    def cpu_info(self):
        return self.cpu_temp

    def gpu_info(self):
        return self.gpu_temp

    def disk_info(self):
        return self.disk_temp

def get_sensor_class():
    system = platform.system()
    if system == 'Windows':
        return Window
    elif system == 'Linux':
        return Linux
    else:
        raise NotImplementedError(f'Sensor class not implemented for {system} platform')