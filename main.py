print ("Conversor de Binário/Decimal")
print ("C para cancelar algum comando")
print ("T para terminar")
from funcoes_conversor import *
Binários = ["1","0","."]
Números = ["1","2","3","4","5","6","7","8","9","0","."]
comando = "a"
while True:
	if comando == "T" or comando == "t":
		break
	x = 0
	base = input("Digite a base para conversão:")
	if base == "2":
		while True:
			x = 0
			a = input("Digite um número decimal para ser convertido para binário: ")
			if a == "T" or a == "t":
				comando = "T"
				break
			elif a == "C" or a == "c":
				break
			else:
				a = list(a)
				for i in range(len(a)):
					if a[i] not in Números:
						print("Número decimal inválido")
						break
					elif a[i] in Números:
						x += 1
				if x == len(a):
					a = "".join(map(str,a))
					print (conversor_para_binario(a))
					break
			base = input("Deseja alterar a base escolhida?[S/N]")
			if base == "S" or base == "s":
				break
			elif base == "N" or base == "n":
				base = "2"
			elif base == "T" or base == "t":
				comando = "T"
				break
			elif base == "C" or base == "c":
				base = "2"
			else:
				print ("Comando desconhecido")
	elif base == "10":
		while True:
			x = 0
			b = input("Digite um número binário para ser convertido para decimal: ")
			if b == "T" or b == "t":
				comando = "T"
				break
			elif b == "C" or b == "c":
				break
			else:
				b = list(b)
				for i in range(len(b)):
					if b[i] not in Binários:
						print("Número binário inválido")
						break
					elif b[i] in Binários:
						x += 1
				if x == len(b):
					b = "".join(map(str,b))
					print (conversor_para_decimal(b))
					break
			base = input("Deseja alterar a base escolhida?[S/N]")
			if base == "S" or base == "s":
				break
			elif base == "N" or base == "n":
				base = "10"
			elif base == "T" or base == "t":
				comando = "T"
				break
			elif base == "C" or base == "c":
				base = "10"
			else:
				print ("Comando desconhecido")
	elif base == "T" or base == "t":
		comando = "T"
	elif base == "C" or base == "c":
		print ("Nada para retornar")
	else:
		print ("Comando desconhecido")
