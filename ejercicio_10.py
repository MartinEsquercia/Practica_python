palabra = input("Ingrese una palabra ")
palabra = palabra.lower()
palabra_lista = []
cant = 0
if(palabra.isalpha())==True:
    for i in palabra:
        palabra_lista.append(i)
    for j in palabra_lista:
        if(j=="a")or(j=="e")or(j=="i")or(j=="o")or(j=="u")or(j=="l")or(j=="n")or(j=="r")or(j=="s")or(j=="t"):
            cant = cant + 1
        elif(j=="d")or(j=="g"):
            cant = cant + 2
        elif(j=="b")or(j=="c")or(j=="m")or(j=="p"):
            cant = cant + 3
        elif(j=="f")or(j=="h")or(j=="v")or(j=="w")or(j=="y"):
            cant = cant + 4
        elif(j=="k"):
            cant = cant + 5
        elif(j=="j")or(j=="x"):
            cant = cant + 6
        else:
            cant = cant + 7
else:
    print("No se a ingresado una palabra")
if(palabra.isalpha())==True:
    print("La palabra fue "+palabra+" a sumado ")
    print(cant)
    print("puntos")