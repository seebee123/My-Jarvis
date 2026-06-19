import psutil
import socket

def get_cpu():
    return psutil.cpu_percent()

def get_ram():
    return psutil.virtual_memory().percent

def get_battery():
    battery = psutil.sensors_battery()

    if battery:
        return battery.percent, battery.power_plugged

    return None, None

def get_pc_name():
    return socket.gethostname()