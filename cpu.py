import psutil
import time
import socketio

def raspberry_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  used_memory = round((psutil.virtual_memory()[2]),2)
  free_memory = round(100 - used_memory,2)
  return used_memory,free_memory,cpu_usage

def send_infos():
  while(1):
    global start_timer
    start_timer = time.time()
    memory = raspberry_usage()
    print(memory[0]+","+memory[1]+","+memory[2])


send_infos()