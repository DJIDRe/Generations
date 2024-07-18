def moreAge():
    name = str(input("ingresa tu nombre: "))
    age = int(input("ingresa tu edad: "))
    print(f'el usuario se llama {name} y tendra {age+5}')

def showThirdList():
    fruit=["manzana", "platano", "frutilla", "mango", "kiwi"]
    return print(fruit[2])

def isEvenOrOdd():
    check_number = lambda num: "par" if num % 2 == 0 else "impar"
 
    number = int(input("Enter a number: "))
    result = check_number(number)
 
    print(number, "es un", result, "numero.")

def canVote():
    vote = lambda num: "Si puedes votar ya que tienes" if num >= 18 else "No puedes votar ya que tienes"

    age = int(input("Por favor, ingresa tu edad: "))
    youCanVote = vote(age)
    print(youCanVote,age)


def waterEvullition():
    solid = lambda num: "Solida" if num<=0 else "Liquida"
    gas = lambda num: "Gaseosa" if num>=100 else "Liquida"

    water = int(input("ingresa una temperatura en °C: "))
    isSolid = solid(water)
    isGas = gas(water)

    if water>=0:
        isGas = gas(water)
        print(isGas)
    else:
        isSolid = solid(water)
        print(isSolid)

def positiveNegative():
    checkNumberSign = lambda number: print("el numero es positivo") if number>0 else \
    print("el numero es negativo") if number<0 else print ("el numero es 0")

    num = int(input("ingresa un numero: "))
    checkNumberSign(num)

def bothPositive():
    firstNum = int(input("ingresa un numero: "))
    secondNum = int(input("ingresa un numero: "))

    if firstNum and secondNum>0:
        print("ambos son positivos")
    else: 
        print("no son positivos")

def bothVoteLicense():
    age = int(input("ingresa una edad: "))
    hasLicense = str(input("tiene licencia? (escriba si o no) "))

    if age>=18 and hasLicense=="si":
        print("tu puedes votar")
    else:
        print("no puedes votar ")

def ifEvenOrOdd():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in lst:
        if i>0 or i%2==0:
            print("su numero es: " + str(i/2))
        if i>0 or i%2==1:
            print("su numero es: " + str(3*i+1))
        else:
            print("el string es: " + str(i)) 



#if __name__ == "__main__":
#    ifEvenOrOdd()