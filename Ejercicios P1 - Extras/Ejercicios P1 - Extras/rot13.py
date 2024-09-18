fichero1 = open('fundacion.txt', 'r')

encrypyted_file = open('encrypted_fundacion.txt', 'w')
#fichero2.write(contenido)
leer = fichero1.read()
resultado = ""
for char in leer:
    if char != "\n":
        calculo =  (ord(char)) + 13
        resultado += (chr(calculo))
encrypyted_file.write(resultado)
