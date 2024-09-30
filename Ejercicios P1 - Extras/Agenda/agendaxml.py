import xml.etree.ElementTree as ET
import os

# Nombre del fichero XML
XML_FILE = 'agenda.xml'

# Funciones para manejar la agenda
def iniciar_agenda():
    while True:
        print("\n--- Menú de Agenda ---")
        print("1. Guardar datos de un contacto")
        print("2. Modificar datos de un contacto")
        print("3. Dar de baja a un contacto")
        print("4. Buscar un contacto")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            guardar_contacto()
        elif opcion == '2':
            modificar_contacto()
        elif opcion == '3':
            eliminar_contacto()
        elif opcion == '4':
            buscar_contacto()
        elif opcion == '5':
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def guardar_contacto():
    contacto_info = {}
    for field in ['Nombre', 'Apellidos', 'Email', 'Telefono1', 'Telefono2', 'Direccion']:
        contacto_info[field] = input(f"Ingrese {field}: ")
    
    if not os.path.exists(XML_FILE):
        root = ET.Element("agenda")
    else:
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

    contacto = ET.SubElement(root, "contacto")
    for field, value in contacto_info.items():
        ET.SubElement(contacto, field.lower()).text = value

    tree = ET.ElementTree(root)
    tree.write(XML_FILE)
    print("Contacto guardado con éxito.")

def modificar_contacto():
    nombre = input("Nombre del contacto a modificar: ")
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    encontrado = False
    
    for contacto in root.findall('contacto'):
        if contacto.find('nombre').text == nombre:
            for field in ['Apellidos', 'Email', 'Telefono1', 'Telefono2', 'Direccion']:
                nuevo_valor = input(f"Ingrese nuevo {field} (dejar vacío para no modificar): ")
                if nuevo_valor:
                    contacto.find(field.lower()).text = nuevo_valor
            encontrado = True
            break

    if encontrado:
        tree.write(XML_FILE)
        print("Contacto modificado con éxito.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Nombre del contacto a eliminar: ")
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    for contacto in root.findall('contacto'):
        if contacto.find('nombre').text == nombre:
            root.remove(contacto)
            tree.write(XML_FILE)
            print("Contacto eliminado con éxito.")
            return
    
    print("Contacto no encontrado.")

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    
    for contacto in root.findall('contacto'):
        if contacto.find('nombre').text == nombre:
            datos = {field.capitalize(): contacto.find(field.lower()).text for field in ['nombre', 'apellidos', 'email', 'telefono1', 'telefono2', 'direccion']}
            for field, value in datos.items():
                print(f"{field}: {value}")
            return
    
    print("Contacto no encontrado.")

# Iniciar la agenda
if __name__ == "__main__":
    iniciar_agenda()
