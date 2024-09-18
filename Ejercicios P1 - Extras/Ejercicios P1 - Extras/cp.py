fichero1 = open('fundacion.txt', 'r')
contenido = fichero1.read()
fichero1.close()
fichero2 = open('copiaa.txt', 'w')
fichero2.write(contenido)
fichero2.close()


