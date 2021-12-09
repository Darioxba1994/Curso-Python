def clasificacion(Lista): 
    print(" ******************************************************************")
    print(" 1.  Considerando la siguiente codifique un programa que permita separar \n los números parese impares. Identifique también los posibles valores que considere atípicos a ese arreglo.")
    print("")
    print("Separe los siguientes datos")
    print(Lista)
    Par=[]
    Impar = []
    Atipicos = []
    for i in Lista:
        if i%2 == 0:
            Par.append(i)
        else: 
            Impar.append(i)
        if i >= 111:
            Atipicos.append(i)      
    print(F"Los numeros pares son:{Par}")
    print(F"Los numeros impar son:{Impar}")
    print(F"Los numeros atipicos son:{Atipicos}")
