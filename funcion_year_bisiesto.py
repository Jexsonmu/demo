#Consigna: Realizar una función llamada año_bisiesto:
# Recibirá un año por parámetro
# Imprimirá “El año año es bisiesto” si el año es bisiesto
# Imprimirá “El año año no es bisiesto” si el año no es bisiesto
# Si se ingresa algo que no sea número debe indicar que se ingrese un número.


# Información a tener en cuenta al realizar el entregable:
#     Se recuerda que los años bisiestos son múltiplos de 4
#     pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí.

# A pesar de que la consigna pedia una funcion que se llame "año_bisiesto" preferi usar "year_bisiesto" para evitar errores de caracter especial por la "ñ"
#Le sume que se calculara a partir de 1582 como comento Mariano

    
def year_bisiesto (year):
    if type(year) != int:
        return ("Debe ingresar un número")
    if year <=1582:
        return ("Los años bisiestos se instauraron a partir de 1582, debe ingresar un año posterior a esta fecha")
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return(f"El año {year} es bisiesto")
    else:
        return(f"El año {year} no es bisiesto")
         
        
print (year_bisiesto(2012))
print (year_bisiesto(2010))
print (year_bisiesto(2000))
print (year_bisiesto(1900))
print (year_bisiesto(2025))
print (year_bisiesto(2024))
print (year_bisiesto("Navidad"))
print (year_bisiesto("CODER HOUSE"))
print (year_bisiesto(1200))
print (year_bisiesto(1582))
print (year_bisiesto(25))