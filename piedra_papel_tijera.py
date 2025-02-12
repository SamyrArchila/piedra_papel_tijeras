import random

print("----------------------")
print("1)piedra")
print("2)papel")
print("3)tijera")
print("----------------------")

usu = int(input("Ingrese el numero correspondiente a su decision"))
maq = random.randint(1,3)

if usu >= 4:
    print("No valido")
else:
    if usu == 1:
        print("Elegiste: Piedra")
    elif usu == 2:
        print("Elegiste: papel")
    elif usu == 3:
        print("Elegiste: tijera")

    if maq == 1:
        print("La maquina eligio: Piedra")
    elif maq == 2:
        print("La maquina eligio: papel")
    elif maq == 3:
        print("La maquina eligio: tijera")

    if usu == maq
    print("Empate")
    elif usu == and maq
