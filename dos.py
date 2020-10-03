import requests
from colorama import Fore, Style, Back
site = input("Введите сайт: ")
i = 1
while True:
	response = requests.get(f"http://{site}").text
	print(Fore.YELLOW + response)
	print(Fore.GREEN + f"Пакет послан {i}")
	print(Style.RESET_ALL)
	i = i + 1