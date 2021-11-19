import psutil
import time
import socketio

def raspberry_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  used_memory = round((psutil.virtual_memory()[2]),2)
  free_memory = round(100 - used_memory,2)
  return used_memory,free_memory,cpu_usage


info=[]
with open('/sys/class/thermal/thermal_zone0/temp', 'r') as ftemp:
    current_temp = int(ftemp.read()) / 1000
    info.append(current_temp)

print(info)

