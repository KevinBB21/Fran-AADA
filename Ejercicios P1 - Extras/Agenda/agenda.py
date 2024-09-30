import csv

CSV_FILE = 'agenda.csv'
FIELDS = ['Nombre', 'Apellidos', 'Email', 'Telefono1', 'Telefono2', 'Direccion']

def mostrarMenu():
    opcion = 0
    while opcion > 3 or opcion < 1:
        print("1. Guardar un nuevo contacto")
        print("2. Modificar un contacto")
        print("3. Eliminar un contacto")
        print("4. Buscar un contacto")
        print("5. Mostrar contactos")
        print("6. Salir del menú")
        opcion = int(input())
        if opcion == 1:
            crearContacto()
            opcion = 0
        elif opcion == 2:
            modificarContacto()
            opcion = 0
        elif opcion == 3:
            eliminarContacto()
            opcion = 0
        elif opcion == 4:
            buscarContacto()
            opcion = 0
        elif opcion == 5:
            muestraContacto()
            opcion = 0
        elif opcion == 6:
            break



def crearContacto():
    csvfile = open(CSV_FILE, 'a', newline='')
    writer = csv.writer(csvfile, delimiter=';')

    print("Inserte los datos de contacto")
    nombre = str(input("Nombre: "))
    apellido = str(input("Apellido: "))
    email = str(input("Email: "))
    telefono1 = str(input("Primer Telefono: "))
    telefono2 = str(input("Segundo Telefono:"))
    direccion = str("Calle " + input("Direccion: "))
    writer = writer.writerow([nombre, apellido, email, telefono1,
                              telefono2, direccion])
    csvfile.close()

def modificarContacto():
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    apellido = input("Ingrese los apellidos del contacto a modificar: ")
    encontrado = False
    newrows = []

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            if row['Nombre'] == nombre and row['Apellidos'] == apellido:

                email = input("Ingrese el nuevo email: ")
                telefono1 = input("Ingrese el nuevo teléfono 1: ")
                telefono2 = input("Ingrese el nuevo teléfono 2: ")
                direccion = input("Ingrese la nueva dirección: ")

                row['Email'] = email
                row['Telefono1'] = telefono1
                row['Telefono2'] = telefono2
                row['Direccion'] = direccion

                encontrado = True

            newrows.append(row)
        print(newrows)
    if not encontrado:
        print("Este contacto no esta en la agenda")
    else:
        with open(CSV_FILE, 'w', newline='') as csvnewfile:
            writer = csv.DictWriter(csvnewfile, fieldnames=FIELDS, delimiter=";")
            writer.writeheader()
            writer.writerows(newrows)
            print("Contacto modificado correctamente")

def eliminarContacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    apellidos = input("Ingrese los apellidos del contacto a eliminar: ")
    encontrado = False
    newrows = []

    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")

        for row in reader:
            if row['Nombre'] == nombre and row['Apellidos'] == apellidos:
                encontrado = True
            else:
                newrows.append(row)

    if not encontrado:
        print("Este contacto no esta en la agenda")
    else:
        with open(CSV_FILE, 'w', newline='') as csvnewfile:
            writer = csv.DictWriter(csvnewfile, fieldnames=FIELDS, delimiter=";")
            writer.writeheader()
            writer.writerows(newrows)
        print("Contacto eliminado correctamente")

def buscarContacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    apellidos = input("Ingrese los apellidos del contacto a buscar: ")
    encontrado = False
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:

            if row['Nombre'] == nombre and row['Apellidos'] == apellidos:
                print(list(row.values()))
                encontrado = True
                break
        if not encontrado:
            print("Este contacto no esta en la agenda")


def muestraContacto():

    with open(CSV_FILE, 'r', newline='') as csvfile:
        contactos = []

        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            contactos.append(list(row.values()))
        print(sorted(contactos))

mostrarMenu()