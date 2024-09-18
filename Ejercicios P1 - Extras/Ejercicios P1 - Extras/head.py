fichero = open('fundacion.txt','r')

N = int(input('Dime el numero'))

while N > 0 :
    leer = fichero.readline()
    print(leer)
    N -= 1
    
fichero.close()