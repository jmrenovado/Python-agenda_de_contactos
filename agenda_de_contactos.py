


def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contastos")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Por favor ingrese el nombre completo del contacto:")
    telefono = input("Por favor ingrese el número de teléfono del contacto:")
    email = input("Por favor ingrese el email del contato:")
    agenda[nombre] = { "telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto ha eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre de contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no se ha encontrado en la agenda")

def listar_contacto(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20)
    else:
        print("La agenda aún está vacía")

def agenda_contacto():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contacto(agenda)
        elif opcion == "5":
            print("Saliendo de la aplicación ¡Hasta luego!")
            break

agenda_contacto()