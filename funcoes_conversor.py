
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
		digitos_inteiros.insert(0,resto)
		quociente = num[0] // 2
		if quociente <= 1:
			digitos_inteiros.insert(0,quociente)
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
	if len(num) != 1:
		digitos = digitos_inteiros + "." + digitos_decimais
		return digitos
	else:
		return digitos_inteiros
def conversor_para_decimal(num):
	num = num.replace("."," ")
	num = num.split()
	digitos_inteiros = list(num[0])
	soma2 = 0
	expoente = len(digitos_inteiros) - 1
	if len(num) != 1:
		digitos_decimais = list(num[1])
	for i in range(len(digitos_inteiros)):
		digitos_inteiros[i] = int(digitos_inteiros[i])
	for i in range(len(digitos_inteiros)):
		digitos_inteiros[i] = digitos_inteiros[i] * 2 **(expoente - i)
	soma1 = sum(digitos_inteiros)
	if len(num) != 1:
		for i in range(len(digitos_decimais)):
			digitos_decimais[i] = int(digitos_decimais[i])
		for i in range(len(digitos_decimais)):
			digitos_decimais[i] = digitos_decimais[i] * 2 ** (-(i + 1))
		soma2 = sum(digitos_decimais)
	digitos = soma1 + soma2
	return digitos
