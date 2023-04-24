B = [ ]
D = [ ]
num = input("Digite um número decimal:")
num = num.replace(".", " ")
num = num.split()
num[0] = int(num[0])
if len(num) != 1:
	num[1] = "0." + num[1]
	num[1] = float(num[1])
while True:
	resto = num[0] % 2
	B.append(resto)
	quociente = num[0] // 2
	if quociente == 1:
		B.append(quociente)
		break
	num[0] = quociente
x = len(B)
if len(num) != 1:
	while True:
		resto = num[1] * 2
		if resto > 1:
			D.append(1)
			resto -= 1
			num[1] = resto
		elif resto < 1:
			D.append(0)
			num[1] = resto
		elif resto == 1:
			D.append(1)
			break
y = 0
for i in range(x):
	x -= 1
	print(f"{B[x]}",end="")
if len(num) != 1:
	print(".",end="")
	while True:
		print(f"{D[y]}",end="")
		if y == (len(D) - 1):
			break
		y += 1
print()