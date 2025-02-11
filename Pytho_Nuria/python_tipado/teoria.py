#Tipado en Python
texto='hola qué tal' #texto es de tipo string
numero=3 #numero es de tipo entero
decimal=3.5 #decimal es de tipo float
descuento=True #booleano es de tipo booleano
#conjunto. orden, repetición, mismo tipo de dato, inmutable
lista=[1,2,3] #lista es de tipo lista
tupla=(1,2,3) #tupla es de tipo tupla
diccionario={'nombre':'Juan','edad':23} #diccionario es de tipo diccionario #json
conjunto={1,2,3} #conjunto es de tipo conjunto
def singular():
    #si tienes descuento, al total le aplicas un 20%
    if(descuento==True):
        total=numero*decimal*0.8
        print('tienes descuento')
    else:
        total=numero*decimal
    print('El total es:',total)
#ejecutar la función. llamándola
singular()
