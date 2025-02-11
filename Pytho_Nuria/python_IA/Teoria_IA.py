print ('La IA en Python')
import random

def juego_adivinanza():
    # Generar un número aleatorio entre 0 y 10
    numero_aleatorio = random.randint(0, 10)
    
    intentos = 5  # Número de intentos permitidos
    print("Adivina el número (entre 0 y 10). Tienes 5 intentos.")
    
    for i in range(1, intentos + 1):
        try:
            # Pedir al usuario que introduzca un número
            numero_usuario = int(input(f"Intento {i}: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Comprobar si el número introducido es correcto
        if numero_usuario == numero_aleatorio:
            print(f"¡Felicidades! Has acertado el número en {i} intentos.")
            break
        else:
            print("Número incorrecto.")
            
    else:
        # Si se agotan los intentos, mostrar un mensaje
        print(f"Lo siento, has agotado tus {intentos} intentos. El número era {numero_aleatorio}.")

# Ejecutar el juego
juego_adivinanza()


import random

def juego_adivinanza_while():
    # Generar un número aleatorio entre 0 y 10
    numero_aleatorio = random.randint(0, 10)
    
    intentos = 5  # Número de intentos permitidos
    print("Adivina el número (entre 0 y 10). Tienes 5 intentos.")
    
    for i in range(1, intentos + 1):
        try:
            # Pedir al usuario que introduzca un número
            numero_usuario = int(input(f"Intento {i}: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        # Comprobar si el número introducido es correcto
        if numero_usuario == numero_aleatorio:
            print(f"¡Felicidades! Has acertado el número en {i} intentos.")
            break
        else:
            print("Número incorrecto.")
            
    else:
        # Si se agotan los intentos, mostrar un mensaje
        print(f"Lo siento, has agotado tus {intentos} intentos. El número era {numero_aleatorio}.")

# Ejecutar el juego
juego_adivinanza()
