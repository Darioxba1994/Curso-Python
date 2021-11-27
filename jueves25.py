Var_str1= "Letrasespeciales Ñ ñ á é"
print(Var_str1)
print(len(Var_str1)) ## Numero de Caracteres
print(Var_str1[0]) # Caracter de posicion 0
print(Var_str1[4:7]) # Caracteres despues del caracter 4 hasta el 6
Var_str2 = "Nombre "
Var_str3 = "Apellido "
Var_str4 = "EDAD"
##OPERACIONES CON STRING
print(Var_str2+Var_str3+Var_str4) #concatenar
print(2*Var_str2)
## Valores numericos
Var_str5=200 
str(Var_str5) # cambiar numeros a string
##Corregir amasonas por Rio Amazonas
Var_str7 = "amasonas"
Var_str6 = "Rio A" + Var_str7[1:3] + "z"+Var_str7[4:]
print(Var_str6)

## Funciones de sring
print(Var_str6.upper()) ## Mayusculas
print(Var_str6.lower()) ## Minusculas
print(Var_str6.title()) ## Modo titulo
print(Var_str7.replace("s","z")) ## Modo titulo