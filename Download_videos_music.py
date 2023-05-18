from pytube import YouTube
import os
import time
from colorama import init,Fore,Back
from pyfiglet import Figlet
import platform

def download(url,op):
	try:
		yt = YouTube(url)
		print(f'{Fore.MAGENTA}Title: {Fore.GREEN} {yt.title}\n{Fore.MAGENTA}Author: {Fore.GREEN}{yt.author}')
		if op == 1:
			lista = yt.streams.filter(type="video")
			for indice in range(len(lista)):print(f'{Fore.YELLOW}{indice+1}<<{lista[indice].mime_type}:resolution {lista[indice].resolution}')

		elif op == 2:
			lista = yt.streams.filter(type="audio")
			for indice in range(len(lista)):print(f'{Fore.YELLOW}{indice+1}<<{lista[indice].mime_type}:resolution {lista[indice].abr}')
		try:
			op = int(input('Enter option :\n>'))
			path = open('cache.txt','r').read()
			try:
				lista[op-1].download(path)
				input(f'{Fore.MAGENTA}Download Completed')
			except:
				input(f'{Fore.RED}!Warning!')
		except:
			print('Option Incorrect')
	except:
		input(f'{Fore.RED}The url is incorrect')

def option():
	with open('cache.txt','r') as help:
		print(f'{Fore.MAGENTA}Example {help.read()} (Write the slash => /)')
		path = input(f'{Fore.GREEN}Enter the path : ')
		if os.path.exists(path):
			with open('cache.txt','w') as file1:
				file1.write(path)
				file1.close()
		else:
			input(f'{Fore.RED}The path is incorrect ')
		help.close()


def generate():
	with open('cache.txt','w') as file:
		file.write(os.getcwd())
		file.close()


generate()

while True:
	init()
	if platform.system() == "Linux":
		os.system('clear')
	else:
		os.system('cls')

	print(f'{Fore.BLUE}{Figlet(font="slant").renderText("Download video and Music")}')
	print(f"\t{Fore.GREEN}-------------------------------------------")
	print(f"\t {Fore.RED}\t>{Fore.GREEN}The plataform is : {platform.system()}{Fore.RED}<")
	print(f"\t{Fore.GREEN}-------------------------------------------\n\n")
	print(f"{Fore.MAGENTA}Github : {Fore.YELLOW}https://github.com/yosoyretro")
	print(f'{Fore.MAGENTA}Author del codigo :{Fore.RED} El chico programador\n')

	print(f'{Fore.YELLOW}1)Download Video\n2)Download Music\n3)Update the path the file\n4)exit{Fore.GREEN}\n')
	try:
		op = int(input('Enter the option : '))
		if  op == 1 or op == 2:
			url = input(f'{Fore.GREEN}Enter the url : ')
			download(url,op)
		elif op == 3:
			option()
		elif op == 4:
			input(f'{Fore.WHITE}Thacks.....')
			break
		else:
			print('The option is Incorrect ')
	except:
		print(f"{Fore.RED}the type of enter must be integer")
		time.sleep(2)
