def PASWORD():
    print(" ******************************************************************")
    print(" 2. Desarrollar un programa que permita validar la contraseña introducida por un usuario \n con las siguientes comprobaciones: ")
    minusc=["a","b","c","d","e","f","g","h","i","j"]
    mayus=["K","L","M","N","O","P","Q","R","S","T"]
    numeros=["1","2","3","4","5","6","7","8","9","0"]
    signos=["$","%","*","@"]

    c1=[False, False, False, False]
    while c1 != [True,True,True,True]:
        Pasword = input("Ingrese una contraseña con las siguientes caracteristicas: \n1. Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j  \n2. Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.\n3. Debe contener al menos un número entre 0 y 9.\n4. Debe contener un símbolo especial entre: $,%,*,@\n5. Tamaño mínimo de 5 caracteres y máximo de 15.\n")
        P = list(Pasword)
        cond =["minusculas", "mayusculas", "numeros", "signos"]
        if len(P)>=5 and len(P) <=15:
            j=0
            c3 =[]
            for p in P:  
                v1 = p in minusc 
                v2 = p in mayus 
                v3 = p in numeros
                v4 = p in signos
                c2 =[v1,v2,v3,v4]

                i = 0
                for v in c2:
                    if v == True:
                        c1[i] = True
                    i=i+1

                if p in minusc or p in mayus or p in numeros or p in signos :
                    j =j+1
                else:
                    c3.append(p)
            i=0
            lst =[]
            for c in c1:
                if c== False:
                    lst.append(cond[i])
                i=i+1 

            if c1 ==[True,True,True,True] and len(P) == j:
                print("Su contraseña ha sido validada =D")
                break
            else:
                    print("La contraseña no cumple las condiciones, no hay {0} y {1} no se identifican en el alfabeto".format(lst,c3))
        else:
            print("Necesita al menos 5 caracteres y maximo 15")
