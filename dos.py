import requests
from colorama import Fore, Style
site = input("Введите сайт: ")
i = 1
while True:
	response = requests.get(f"{site}").text
	print(response)
	print(Fore.GREEN + f"Пакет послан {i}")
	print(Style.RESET_ALL)
	i = i + 1