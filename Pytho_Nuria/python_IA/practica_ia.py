#Quiero hacer una aplicación (de consola) con python que permita preguntar al usuario una ciudad de vacaciones.  
#Si la ciudad es Madrid, Sevilla o Valencia le dirá que no hay plazas .#
#Si la ciudad es Córdoba, Segovia o Toledo le dice que puede ir la próxima semana. #
#si pregunta por otra ciudad que no sea las mencionadas le dirá que no conoce esa ciudad. #
#La aplicación debe seguir preguntando hasta que el usuario escriba "salir".#

def consultar_ciudad_vacaciones():
    while True:
        # Pedir al usuario que introduzca una ciudad
        ciudad = input("Introduce una ciudad para tus vacaciones (o escribe 'salir' para terminar): ").lower()

        # Comprobar si el usuario quiere salir
        if ciudad == "salir":
            print("Gracias por utilizar la aplicación. ¡Adiós!")
            break
        
        # Comprobar si la ciudad es Madrid, Sevilla o Valencia
        elif ciudad in ["madrid", "sevilla", "valencia"]:
            print(f"No hay plazas disponibles en {ciudad.capitalize()}.")

        # Comprobar si la ciudad es Córdoba, Segovia o Toledo
        elif ciudad in ["córdoba", "segovia", "toledo"]:
            print(f"Puedes viajar a {ciudad.capitalize()} la próxima semana.")

        # Para cualquier otra ciudad
        else:
            print(f"No conocemos la ciudad de {ciudad.capitalize()}.")
consultar_ciudad_vacaciones()
