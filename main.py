# Convertir desde una base dada por el usuario a base decimal
def convertiradec():
    baseType = int(raw_input("Desde que base quiere convertir: "))
    num = str(raw_input("Escriba el numero: "))
    result = 0
    chequeoBase = True
    isNeg = False
    if num[0] == "-":
        isNeg = True
    for i in range(1, len(num)+1):
            for n in range(1, baseType):
                if num[-i] == str(n):
                    result += n*baseType**(i-1)
                elif num[-i] == "-" and i != len(num):
                    print("El numero no esta en la base dada.")
                    chequeoBase = False
                    break;
                if num[-i] != "-":
                    if int(num[-i]) >= baseType:
                        print("El numero no esta en la base dada.")
                        chequeoBase = False
                        break;
            if chequeoBase == False:
                break;
    if isNeg:
        result = -result
    if chequeoBase:
        print(num + " en base decimal es " + str(result))
