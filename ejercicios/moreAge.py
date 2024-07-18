def moreAge():
    name = str(input("ingresa tu nombre: "))
    age = int(input("ingresa tu edad: "))
    print(f'el usuario se llama {name} y tendra {age+5}')

if __name__ == "__main__":
    moreAge()