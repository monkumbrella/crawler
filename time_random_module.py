from time import *
from random import randint

for i in range(0,3):
	seconds = randint(2,5)
	print(seconds)
	sleep(seconds)
	print(f'i wait {seconds}')
