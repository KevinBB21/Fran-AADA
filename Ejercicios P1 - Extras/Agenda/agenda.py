import csv

print("Eliga una opcion de esta agenda \n")
print("1 - Guardar datos de un contacto \n")
print("2 - Modificar datos de un contacto \n")
print("3 - Dar de baja un contacto \n")
print("4 - Buscar un contacto \n")
print("5 - Mostrar la lista de contactos ordenada \n")
print("6 - Salir de la agenda \n")

eleccion = input("¿Cual sera su elección? \n")
eleccioncorr = int (eleccion)

if eleccioncorr == 1:
    with open("datosagenda.csv", 'a', newline="") as archivoCSV:
        contenidoNuevo = csv.writer(archivoCSV, delimiter=",")
        contacto = input("Danos la informacion del contacto, Gracias")
        contenidoNuevo.writerow([contacto])
elif eleccioncorr == 2:
    print("por hacer")
elif eleccioncorr == 3:
    print("por hacer")
elif eleccioncorr == 4:
    print("por hacer")
elif eleccioncorr == 5:
    print("por hacer")
elif eleccioncorr == 6:
    print("Muchas gracias por usar la agenda!")

