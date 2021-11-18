import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connexion au serveur etablie !')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('Deconnecter du serveur')

def envoie(data):
   sio.emit('msg',data)

def connexion():
   sio.connect('http://localhost:5000')

def deconnexion():
   sio.disconnect()

