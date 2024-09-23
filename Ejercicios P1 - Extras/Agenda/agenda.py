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

def modificar_contacto(nombre_buscado, nuevos_datos, datosagenda_csv):
    # Leer los datos del archivo CSV
    with open(datosagenda_csv, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        contactos = list(lector)

    # Modificar el contacto
    for i, contacto in enumerate(contactos):
        if contacto[0] == nombre_buscado:  # Suponiendo que el nombre está en la primera columna
            contactos[i] = nuevos_datos  # Reemplazamos la fila con los nuevos datos
            break

    # Escribir los datos de nuevo en el archivo CSV
    with open(datosagenda_csv, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(contactos)


if eleccioncorr == 1:
    with open("datosagenda.csv", 'a', newline="") as archivoCSV:
        contenidoNuevo = csv.writer(archivoCSV, delimiter=";")
        contacto = input("Danos la informacion del contacto en este formato : Nombre Apellidos Email Telefono1 Telefono2  Direccion \n")
        contenidoNuevo.writerow(contacto.split())
elif eleccioncorr == 2:
    pregunta = input("Dime el nombre de la persona que quieras cambiar y el telefono a cambiar \n")
    modificar_contacto(pregunta.split())
elif eleccioncorr == 3:
    print("por hacer")
elif eleccioncorr == 4:
    print("por hacer")
elif eleccioncorr == 5:
    print("por hacer")
elif eleccioncorr == 6:
    print("Muchas gracias por usar la agenda!")


