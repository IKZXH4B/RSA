import math
import time
import random
from fractions import gcd

count = 1
coprimes = []
encoded = []
decoded = []

def generate_keys(n):
	while count != n-1:
		count += 1
		x = gcd(count, n) #calcula o mdc
		if x == 1:
			if verify_prime(count) == True: #verifica se os numeros são primos antes de adiciona-los a lista
				coprimes.append(count)
			

	e = coprimes[random_number(len(coprimes))] #gera o valor e a partir de um numero aleatorio

	d = find_d(e,z)


def convert_ascii(text): #converte texto para uma lista com os caracteres em ascii
	ascii_values = []
	for character in text:
		ascii_values.append(ord(character))
	return ascii_values

def random_number(x): #gera um numero aleatorio a ser usado para definir e
	i = random.randint(0,x)
	return i

def verify_prime(x): #função para verificar se um numero é primo
	if x > 1:
		for i in range(2, x // 2):
			if (x % i) == 0:
				return False
				break
		else:
			return True
	else:
		return False

def find_d(e, totiente): #procura o d
	i = 2
	while True:
		if e * i % totiente == 1:
			return i
			break
		else:
			i += 1

print('''====================
+ [1] Gerar chaves +
+ [2] Codificar    +
+ [3] Decodificar  +
====================
''')

response = int(input('>>> '))

print()

if response == 1:
	p = int(input('Digite o valor de p: '))

	q = int(input('Digite o valor de q: '))

	start = time.time() #inicia o timer

	n = p * q

	z = (p-1)*(q-1)

	while count != n-1:
		count += 1
		x = gcd(count, n) #calcula o mdc
		if x == 1:
			if verify_prime(count) == True: #verifica se os numeros são primos antes de adiciona-los a lista
				coprimes.append(count)

	e = coprimes[random_number(len(coprimes))] #gera o valor e a partir de um numero aleatorio

	d = find_d(e,z)

	print(f'valor de p: {p}')

	print(f'valor de q: {q}')

	print(f'valor de n: {n}')

	print(f'valor de z: {z}')

	print(f'valor de e: {e}')

	print(f'valor de d: {d}')

	end = time.time() #termina o timer

	print(end - start) #mostra o tempo de execução

if response == 2:
	n = int(input('Digite o valor de n: '))
	print()

	e = int(input('Digite o valor de e: '))
	print()

	text = convert_ascii(input('Digite o seu texto: '))
	print()

	start = time.time()

	for character in text: 
		i = (character ** e) % n
		encoded.append(i)
		print(f'{i}', end=' ')

	end = time.time()

	print()

	print(end - start)

if response == 3:
	n = int(input('Digite o valor de n: '))
	print()

	d = int(input('Digite o valor de d: '))
	print()

	text = input('Digite o seu texto: ')

	start = time.time()

	numbers = (text.split(' '))

	for i in numbers:
		encoded.append(int(i))

	for number in encoded:
		i = (number ** d) % n
		print(f'{i}', end=' ')
	
	end = time.time()

	print()

	print(end - start)
