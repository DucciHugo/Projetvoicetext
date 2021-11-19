import psutil
import time
import socketio

# standard Python
sio = socketio.Client()
start_timer = None
HOST = 'http://localhost:5000/'


def raspberry_usage():
  cpu_usage = psutil.cpu_percent(interval=1)
  used_memory = round((psutil.virtual_memory()[2]),2)
  free_memory = round(100 - used_memory,2)
  print('memory % used:', psutil.virtual_memory()[2])
  print('memory % free:',free_memory)
  print('cpu  % used', cpu_usage)
  return used_memory,free_memory,cpu_usage

def send_infos():
  while(1):
    global start_timer
    start_timer = time.time()
    memory = raspberry_usage()
    sio.emit('system_usage-'+sio.io.engine.id,{
      'memoryUsed' :  memory[0],
      'memoryFree' :  memory[1],
      'cpuUsed' :  memory[2]
    })
    time.sleep(3)

@sio.event
def connect():
    print('connection established')
    send_infos()

@sio.event
def disconnect():
  print('connection lost...')
 
@sio.on('message')
def on_message(data):
  print('I received a message!'+ data)



if name == 'main':
    sio.connect('http://localhost:5000')
    sio.wait()