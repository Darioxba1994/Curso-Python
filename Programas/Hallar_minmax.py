def minmax():
    while True:
        print("*****************************************************************")
        print("******Sacar Minimos y Maximos*****************")
        print("*****************************************************************")
        opcion = int(input("1) Demostración del cálculo de máximos y mínimos en diccionarios. \n2) Salir. \n")) 
        while opcion !=2 and opcion!=1:
                print("Error !!!!!!!! Escoja una opcion valida")
                opcion = int(input("1) Demostración del cálculo de máximos y mínimos en diccionarios. \n2) Salir. \n")) 
        if opcion == 1:
            opcion2 = int(input("Elija un diccionario para la demostración: \n1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37} \n2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)} \n3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92} \n4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]} \n"))
            if opcion2 ==1:
                dic = {"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
                maxi = int(input("ingrese el numero de máximos"))
                mini = int(input("ingrese el numero de mínimos")) 
                while maxi+mini > len(list(dic.values())):
                    maxi = int(input("ingrese el numero de máximos"))
                    mini = int(input("ingrese el numero de mínimos"))
                minimos = list(dic.values())
                minimos.sort()
                maximos = list(dic.values())
                maximos.sort(reverse = True)
                print(F"Valores calculados en formato LISTA: {[maximos[0:maxi],minimos[0:mini]]}") 
                print(F"Valores calculados en formato TUPLA: {(tuple(maximos[0:maxi]),tuple(minimos[0:mini]))}")
            elif opcion2 ==2:
                dic ={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
                maxi = int(input("ingrese el numero de máximos"))
                mini = int(input("ingrese el numero de mínimos")) 
                while maxi+mini > (len(dic["tplA"])+len(dic["tplB"])+len(dic["tlpC"])):
                    maxi = int(input("ingrese el numero de máximos"))
                    mini = int(input("ingrese el numero de mínimos"))
                minimos = list(list(dic.values())[0])+list(list(dic.values())[1])+list(list(dic.values())[2])
                minimos.sort()
                maximos = list(list(dic.values())[0])+list(list(dic.values())[1])+list(list(dic.values())[2])
                maximos.sort(reverse = True)
                print(F"Valores calculados en formato LISTA: {[maximos[0:maxi],minimos[0:mini]]}") 
                print(F"Valores calculados en formato TUPLA: {(tuple(maximos[0:maxi]),tuple(minimos[0:mini]))}")
            elif opcion2 ==3:
                dic = {"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
                maxi = int(input("ingrese el numero de máximos"))
                mini = int(input("ingrese el numero de mínimos")) 
                while maxi+mini > len(list(dic.values())):
                    maxi = int(input("ingrese el numero de máximos"))
                    mini = int(input("ingrese el numero de mínimos"))
                minimos = list(dic.values())
                minimos.sort()
                maximos = list(dic.values())
                maximos.sort(reverse = True)
                print(F"Valores calculados en formato LISTA: {[maximos[0:maxi],minimos[0:mini]]}") 
                print(F"Valores calculados en formato TUPLA: {(tuple(maximos[0:maxi]),tuple(minimos[0:mini]))}")
            elif opcion2 ==4:
                dic = {"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
                maxi = int(input("ingrese el numero de máximos"))
                mini = int(input("ingrese el numero de mínimos")) 
                while maxi+mini > (len(dic["lst1"])+len(dic["lst2"])+len(dic["lst3"])):
                    maxi = int(input("ingrese el numero de máximos"))
                    mini = int(input("ingrese el numero de mínimos"))                 
                minimos = list(dic.values())[0]+list(dic.values())[1]+list(dic.values())[2]
                minimos.sort()
                maximos = list(dic.values())[0]+list(dic.values())[1]+list(dic.values())[2]
                maximos.sort(reverse = True)
                print(F"Valores calculados en formato LISTA: {[maximos[0:maxi],minimos[0:mini]]}") 
                print(F"Valores calculados en formato TUPLA: {(tuple(maximos[0:maxi]),tuple(minimos[0:mini]))}")

        if opcion ==2:
            print("Termino la demostracion")
            break

