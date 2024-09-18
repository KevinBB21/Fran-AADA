with open('fundacion.txt', 'r') as archivo:
    lineas = 0
    palabras = 0
    caracteres = 0
    
    for linea in archivo:
        lineas += 1  
        caracteres += len(linea)  
        palabras += len(linea.split())  

print(f"Líneas: {lineas}")
print(f"Palabras: {palabras}")
print(f"Caracteres: {caracteres}")