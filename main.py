def decabin():
	x = int(raw_input("Escribe un número en base decimal: "))
	num = x
	if num < 0:
		isNeg = True
		num = abs(num)else:
		isNeg = False
	result =""
	if num == 0:
		result = 0
	while num > 0:
		result = str(num % 2) + result
		num = int(num/2)
		if isNeg:
		result = "-" + result
	print(str(x) + " en binario es " + result)

def binadec():
	binario = str(raw_input("Escribe un número en base binaria: "))
	result = 0
	isBin = True
	isNeg = False
	if binario[0] == "-":
		isNeg = True
	for i in range(1, len(binario)+1):
		if binario[-i] == "1":
			result += 2**(i-1)
		elif binario[-i] == "0":
			result += 0
		elif binario[-i] == "-" and i == len(binario):
			result += 0
		else:
			print("El número no está en base binaria.")
			isBin = False
			break;
	if isNeg:
		result = -result
	if isBin:
		print(binario + " en base decimal es " + str(result))
