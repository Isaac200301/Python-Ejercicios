HermanosGrin = {
    "Blancanieves": {"personaje_principal": "Blancanieves", "año": 1912, "disponible": True},
    "Cenicienta": {"personaje_principal": "Cenicienta", "año": 1815, "disponible": True},
    "Hansel y Gretel": {"personaje_principal": "Hansel y Gretel", "año": 1810, "disponible": False},
    "La Bella Durmiente": {"personaje_principal": "Aurora", "año": 1812, "disponible": True},
    "Rapunzel": {"personaje_principal": "Rapunzel", "año": 1919, "disponible": True},
    "El lobo y los siete cabritos": {"personaje_principal": "Los siete cabritos", "año": 1823, "disponible": True},
    "Rumpelstiltskin": {"personaje_principal": "La hija del molinero", "año": 2000, "disponible": True},
    "El sastrecillo valiente": {"personaje_principal": "El sastrecillo valiente", "año": 1835, "disponible": True},
}

def agregar_cuento():
    titulo = input("Ingrese el título del cuento: ")
    personaje_principal = input("Ingrese el personaje principal del cuento: ")
    año = int(input("Ingrese el año de publicación: "))
    HermanosGrin[titulo] = {"personaje_principal": personaje_principal, "año": año, "disponible": True}
    print(f'El cuento "{titulo}" ha sido añadido a la biblioteca.')


def obtener_claves_minusculas(diccionario):
    claves_minusculas = []
    for clave in diccionario.keys():
        claves_minusculas.append(clave.lower())
    return claves_minusculas

def prestar_cuento():
    titulo = input("Ingrese el título del cuento que desea prestar: ").strip().lower()
    
    claves_minusculas = obtener_claves_minusculas(HermanosGrin)
    
    if titulo in claves_minusculas:
        for clave in HermanosGrin:
            if clave.lower() == titulo:
                if HermanosGrin[clave]["disponible"]:
                    HermanosGrin[clave]["disponible"] = False
                    print(f'El cuento "{clave}" ha sido prestado.')
                else:
                    print(f'El cuento "{clave}" no está disponible.')
                return
    else:
        print(f'El cuento "{titulo}" no se encuentra en la biblioteca.')

def devolver_cuento():
    titulo = input("Ingrese el título del cuento que desea devolver: ").strip().lower()

    claves_minusculas = obtener_claves_minusculas(HermanosGrin)

    if titulo in claves_minusculas:
        for clave in HermanosGrin:
            if clave.lower() == titulo:
                if not HermanosGrin[clave]["disponible"]:
                    HermanosGrin[clave]["disponible"] = True
                    print(f'El cuento "{clave}" ha sido devuelto.')
                else:
                    print(f'El cuento "{clave}" ya estaba disponible.')
                return
    else:
        print(f'El cuento "{titulo}" no se encuentra en la biblioteca.')

def mostrar_cuentos():
    for titulo, detalles in HermanosGrin.items():
        disponible = "Sí" if detalles["disponible"] else "No"
        print(f'Título: {titulo}, Personaje Principal: {detalles["personaje_principal"]}, Año: {detalles["año"]}, Disponible: {disponible}')

def mostrar_cuentos_por_año():
    año = int(input("Ingrese el año de publicación: "))
    print(f'Cuentos publicados en el año {año}:')
    for titulo, detalles in HermanosGrin.items():
        if detalles["año"] == año:
            disponible = "Sí" if detalles["disponible"] else "No"
            print(f'Título: {titulo}, Personaje Principal: {detalles["personaje_principal"]}, Disponible: {disponible}')





while True:
    print("\nMenú de la biblioteca de cuentos de los Hermanos Grimm")
    print("1. Agregar un nuevo cuento")
    print("2. Prestar un cuento")
    print("3. Devolver un cuento")
    print("4. Ver todos los cuentos")
    print("5. Mostrar cuentos por año de publicación")
    print("6. Salir")

    opción = input("Seleccione una opción: ")

    if opción == "1":
        agregar_cuento()
    elif opción == "2":
        prestar_cuento()
    elif opción == "3":
        devolver_cuento()
    elif opción == "4":
        mostrar_cuentos()
    elif opción == "5":
        mostrar_cuentos_por_año()
    elif opción == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")