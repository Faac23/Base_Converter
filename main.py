# Convertir desde una base dada por el usuario a base decimal
def convertiradec(baseType):
    aceptables = ["-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    chequeoBase = True
    isNeg = False
    result = 0
    num = str(raw_input("Escriba el numero: "))
    if num[0] == "-":
        isNeg = True
    for i in range(1, len(num)+1):
        for n in range(1, baseType):
            if num[-i] in aceptables:
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
            else:
                print("El numero no esta en la base dada.")
                chequeoBase = False
                break;
        if chequeoBase == False:
                break;
    if isNeg:
        result = -result
    if chequeoBase:
        print(num + " en base decimal es " + str(result))
def isIntable(string):
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    notNum = False
    for i in range(len(string)):
        if not string[i] in digitos:
            notNum = True
    if notNum:
        print("No es un numero natural.")
    else:
        string = int(string)
        convertiradec(string)
#Starts
choice = str(raw_input("Si quiere convertir a base decimal escriba 'a decimal'. Si quiere convertir desde base decimal escriba 'de decimal'. "))
if choice.lower() == "a decimal":
    baseInput = str(raw_input("Desde que base quiere convertir: "))
    isIntable(baseInput)
elif choice.lower() == "de decimal":
    print("Proximamente")
else:
    print("No te entendí, intenta nuevamente.")
