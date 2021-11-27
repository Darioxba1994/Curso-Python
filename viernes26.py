## Imprimir palabras en texto
NOMBRE ="Juanddd"
print(NOMBRE.upper())
print("Mi nombre "+NOMBRE.upper()+"") #forma1 "+   +"
print("mi nombre es_ {NOMBRE}".format(NOMBRE="juan")) #format(Variable = "valor")
print(F"mi nombre es_ {NOMBRE.upper()}") # F"  "

## realizar un programa que ingrese un valor entero y determine si es niño, adolecente o adulto
## usando if else
edad= int(input("Ingrese su edad como un número entero: " ))
if edad >=1 and edad<=10:
    print("Se considera un niño")
else:
    if edad>=11 and edad <=18:
        print("Se considera adolecente")
    else:
        print("es un adulto")
## usando elif function
if edad >=1 and edad<=10:
    print("Se considera un niño")
elif edad >=11 and edad <=18:
    
        print("Se considera adolecente")
else:
    print("es un adulto")
    



















