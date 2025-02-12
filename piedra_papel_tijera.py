import random

print("-------------------------------")
print("Piedra,papel o tijera")
print("-------------------------------")
print("1. piedra")
print("2. papel")
print("3. tijera")
print("-------------------------------")

# input
usuario = int (input("Dijite la opcion deseada: "))

# Processing
maquina = random.randint(1,3)

if usuario < 1 or usuario > 4:
    print("Por favor juegue nuevamente")
    r = "Opción no válida."
else:
    # el usuario escogió una opción válida
    if maquina == 1:
        if usuario == 1:
            r = "Empate"
        elif usuario == 2:
            r = "Ganaste"
        else:
            r = "Perdiste"
    elif maquina == 2:
        if usuario == 1:
            r = "Perdiste"
        elif usuario == 2:
            r = "Empate"
        else:
            r = "Ganaste"
    else:
        if usuario == 1:
            r = "ganaste"
        elif usuario == 2:
            r = "Perdiste"
        else:
            r = "Empate"

# salida
print("-------------------------------")
print("---------Resultado ------------")
print("--- " + r + " ----")
print("Usuario: " + str(usuario))
print("Máquina: " + str(maquina))
print("-------------------------------")










