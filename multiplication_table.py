from datetime import datetime
from random import random

import logging

MAX_TIME_PER_PROBLEM = 3  # number of seconds

logging.basicConfig(level=logging.WARNING)

def read_number(question: str):
	result = None
	
	while result is None:
		answer = input(question)
		try:
			result = int(answer)
		except ValueError:
			print('Tohle není číslo. Zkus to znovu')
			
	return result
	
def get_grade(num_mistakes, country):
	return 1 + min(num_mistakes, 4)

limit_int = read_number('Do kolika umíš násobit? ')
num_problems = read_number('Kolik chceš příkladů? ')
num_mistakes = 0

time_beginning = datetime.now()

for i in range(num_problems):
	first = round(random() * limit_int) + 1
	second = round(random() * 10)
	result = read_number(f'{i+1}/{num_problems}: Kolik je {first} * {second}? ')
	expected = first * second
	
	if result == expected:
		print('PARÁDA')
	else:
		print(f'NIC MOC, SPRÁVNĚ TO JE {expected}')
		
		num_mistakes += 1

time_end = datetime.now()

logging.debug(f'from {time_beginning} to {time_end}')
logging.debug(f'time delta: {time_end-time_beginning}')

# speed in problems/s
speed = num_problems / (time_end - time_beginning).total_seconds()
time_per_problem = 1/speed

znamka = get_grade(num_mistakes, 'cz')

if time_per_problem < MAX_TIME_PER_PROBLEM and znamka == 1:
	stars = '*'
else:
	stars = ''

print('')
print(f'Měl(a) jsi {num_mistakes} chyb')
print(f'Tvoje rychlost byla {speed} příkladů za sekundu')
print(f'Jeden příklad ti trval průměrně {time_per_problem} sekund')
print('')
print(f'Tvoje známka je {znamka}{stars}')

if stars:
	print('GRATULUJI!!!')
