#Estructuras de control en Python (2):condicional y bucles
#condicional: if, elif, else ---- switch...case no existe en Python
#bucles: for, while - si sabemos cuántas veces se va a repetir usamos for, si no sabemos usamos while
#operador de asignación: =
#operador de comparación: == (igualdad), != (diferente), >, <, >=, <=
#operadores lógicos: and, or, not --- & || !

""" edad=int(input("Dime cuántos años tienes: "))
if edad>=18 and edad<65:
    print("Eres mayor de edad")
elif edad>=65:
    print("Eres jubilado")
else:
    print("Eres menor o jubilado")  """
    
#Bucles
#mostrar un mensaje 5 veces
""" for i in range(5):
    print("Prueba", i+1)  """    

veces=0 #contador
while True:
    respuesta=input("dime la capital de chipre: ")
    veces+=1 #incremento
    if respuesta.lower()=="nicosia":
        print("Correcto. Lo has conseguido en", veces, "intentos")     
        break #sale del bucle
    else:
        print("Incorrecto. Sigue intentándolo")


    