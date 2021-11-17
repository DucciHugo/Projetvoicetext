import asyncio
import socketio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print('connection established')

@sio.event
async def my_message(data):
    print('message received with ', data)

@sio.event
async def disconnect():
    print('disconnected from server')


async def envoie(data):
    await sio.emit('msg',data)

async def main():
    await sio.connect('http://localhost:5000')
    await sio.wait()

def run():
   asyncio.run(main())


run()
envoie("coucou")
