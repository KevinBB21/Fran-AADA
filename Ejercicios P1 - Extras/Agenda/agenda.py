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
        contenidoNuevo = csv.writer(archivoCSV, delimiter=";")
        contacto = input("Danos la informacion del contacto en este formato : Nombre Apellidos Email Telefono1 Telefono2  Direccion \n")
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


def modificar_contacto(contactos, nombre, nuevo_telefono):
    for contacto in contactos:
        if contacto['nombre'] == nombre:
            contacto['telefono'] = nuevo_telefono
            print(f"Contacto {nombre} modificado.")
            return True
    print(f"Contacto {nombre} no encontrado.")
    return False

def guardar_contactos(archivo, contactos):
    with open(archivo, mode='w', newline='') as f:
        campos = ['nombre', 'telefono', 'email']
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(contactos)