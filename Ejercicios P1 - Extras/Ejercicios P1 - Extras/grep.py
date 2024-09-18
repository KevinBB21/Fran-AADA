with open('fundacion.txt', 'r') as archivo:
    print("Dime la expresion que quieres buscar")
    expresion = input()
    lineas = 0

    for linea in archivo:
        lineas += 1
        if expresion in linea:
            print (lineas)
            print (linea)
            


  