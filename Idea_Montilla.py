#Desafío entregable 3 (Clase 4 y 5)
#"Instrucciones e iteración"

#1) Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
#Mostrar una suma de los dos números
#Mostrar una resta de los dos números (el primero menos el segundo)
#Mostrar una multiplicación de los dos números
#Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.

x=int(input("Ingrese el primer numero y presione enter: "))
y=int(input("Ingrese el segundo numero y presione enter: "))

opcion=int(input("""Eliga la opción de su preferencia:
      1. Mostrar una suma de los dos numeros
      2. Mostrar una resta de los dos numeros (el primero menos el segundo)
      3. Mostrar una multiplicación de los dos numeros
      4. Si elige esta opcion se interrumpirá la impresion del menu y el programa finalizara
      
      
      ¿Que desea ejecutar?: """))

if opcion ==1:
    print("La suma de los dos números es:",str(x+y))
elif opcion ==2:
    print("La resta de los dos números es:",str(x-y))
elif opcion ==3:
    print("La multiplicación de los dos números es:",str(x*y))
elif opcion ==4:
    print("Programa finalizado")
else:
    print("Opcion no valida")
 

#2) Escribí un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

 
numero=int(input("Escriba un numero impar: "))

while numero %2==0:
    numero=int(input("Escriba un numero impar: "))
    
               
print("Programa finalizado")

#3) Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

#Podes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.


i=list(range(1,100,2))
suma=sum(i)
print(f"La suma de todos los numeros enteros impares es: {suma}")



#4) Escribí un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:


    
media=0
numeros= int(input("¿Cuantos numeros desea introducir? : ") )
for x in range(numeros):
    media += int(input("Introduce un numero: ") )

print(f"""Se han introducido {numeros} números.
      La suma total de los numeros es: {media}
      la media aritmetica es: {media/numeros}""")
print("Programa finalizado")


#5)Escribí un programa que pida al usuario un número entero del 0 al 9, y que mientras
#el número no sea correcto se repita el proceso. Luego debe comprobar si el número
#se encuentra en la lista de números y notificarlo:
#La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)



lista= [1, 3, 6, 9]

while True:
    numero = int(input("Ingresa un numero del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
if numero in lista:
    print(f"El numero {numero} se encuentra en la lista {lista}")
else:
    print(f"El número {numero} no se encuentra en la lista {lista}")
   
print("Programa finlizado")

#6)Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
#la conversión de listas es mi_lista=list(range(inicio,fin,salto))

lista_1=list(range(11))
print("Números del 0 al 10:",lista_1)
print("*"*100)

lista_2=list(range(-10,1))
print("Números del -10 al 0:",lista_2)
print("*"*100)

lista_3=list(range(0,22,2))
print("Números pares del 0 al 20:",lista_3)
print("*"*100)

lista_4=list(range(-19,0,2))
print("Números impares entre -20 y 0:",lista_4)
print("*"*100)

lista_5=list(range(0,55,5))
print("Números multiplos de 5 del 0 al 50:",lista_5)
print("*"*100)

print("Programa finalizado")
print("*"*100)

#7)  Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:




lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']

lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']

lista_3 = []

for i in lista_1:

    if i in lista_2 and i not in lista_3:

        lista_3.append(i)


print (lista_3)