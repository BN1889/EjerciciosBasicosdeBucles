# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Introduce una palabra: ")
for i in range(10):
    print(word)
    
# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

agno = int(input("¿Cuántos años tienes? "))
for i in range(agno):
    print("Has cumplido " + str(i+1) + " años")
    
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
# impares desde 1 hasta ese número separados por comas.

numero = int(input('introduce un numero entero positivo: '))
for i in range(1, numero+1, 2):
    print(i, end='  , ')
    
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

inversion  = float(input("¿Cantidad a invertir?:  "))
interes = float(input("¿Interés porcentual anual?:  "))
agnos = int(input("Años?: "))
for i in range(agnos):
    inversion *= 1 + interes / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(inversion, 2)))
    
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
    
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
    
frase = input('introduce una frase: ')
letra = input('introduce una letra: ')
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
