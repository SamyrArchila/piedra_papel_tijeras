import random

print("----------------------")
print("Piedra,papel o tijera")
print("----------------------")
print("1. piedra")
print("2. papel")
print("3. tijera")
print("----------------------")

usuario = int(input("Ingrese el numero correspondiente a su decision: "))
maquina = random.randint(1,3)

if usuario not in [1, 2, 3]:
    print("No valido")
else:
    if usuario == 1:
        print("Elegiste: Piedra")
    elif usuario == 2:
        print("Elegiste: papel")
    elif usuario == 3:
        print("Elegiste: tijera")

    if maquina == 1:
        print("La maquina eligio: Piedra")
    elif maquina == 2:
        print("La maquina eligio: papel")
    elif maquina == 3:
        print("La maquina eligio: tijera")

    if usuario == maquina:
        print("Empate")
    elif usuario == 1 and maquina == 1:
        print("Ganaste")
    elif usuario == 2 and maquina == 2:
        print("Ganaste")
    elif usuario == 3 and maquina == 3:

    









