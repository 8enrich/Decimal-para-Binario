def conversor_para_binario(num):
	digitos_inteiros = []
	digitos_decimais = []
	num = num.replace(".", " ")
	num = num.split()
	num[0] = int(num[0])
	if len(num) != 1:
		num[1] = "0." + num[1]
		num[1] = float(num[1])
	while True:
		resto = num[0] % 2
		digitos_inteiros.append(resto)
		quociente = num[0] // 2
		if quociente == 1:
			digitos_inteiros.append(quociente)
			break
		num[0] = quociente
	if len(num) != 1:
		while True:
			resto = num[1] * 2
			if resto > 1:
				digitos_decimais.append(1)
				resto -= 1
				num[1] = resto
			elif resto < 1:
				digitos_decimais.append(0)
				num[1] = resto
			elif resto == 1:
				digitos_decimais.append(1)
				break
	digitos_inteiros = "".join(map(str, digitos_inteiros))
	digitos_decimais = "".join(map(str, digitos_decimais))
	digitos = digitos_inteiros + "." + digitos_decimais
	return digitos


a = input("Digite um número decimal para ser convertido para binário: ")
print(conversor_para_binario(a))
