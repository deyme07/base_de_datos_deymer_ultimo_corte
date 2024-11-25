import json

class Enfermera:
    def __init__(self, nombre, identificacion, edad, contacto, correo, direccion, especialidad, experiencia, disponibilidad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.contacto = contacto
        self.correo = correo
        self.direccion = direccion
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.disponibilidad = disponibilidad

    def __str__(self):
        return f"{self.nombre} - {self.identificacion} - {self.especialidad} - {self.experiencia} años de experiencia"

def validar_entrada(tipo, mensaje):
    while True:
        entrada = input(mensaje)
        if tipo == 'int':
            try:
                return int(entrada)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif tipo == 'str':
            if entrada.strip() == "":
                print("Este campo no puede estar vacío.")
            else:
                return entrada.strip()
        elif tipo == 'gmail':
            if "@" in entrada and entrada.count("@") == 1 and "." in entrada.split("@")[1]:
                return entrada.strip()
            else:
                print("Por favor, ingrese un correo electrónico válido.")

def registrar_enfermera():
    nombre = validar_entrada('str', "Ingrese su nombre completo: ")
    identificacion = validar_entrada('str', "Ingrese su número de identificación profesional: ")
    edad = validar_entrada('int', "Ingrese su edad: ")
    contacto = validar_entrada('str', "Ingrese su número de contacto: ")
    correo = validar_entrada('gmail', "Ingrese su correo electrónico: ")
    direccion = validar_entrada('str', "Ingrese su dirección: ")
    especialidad = validar_entrada('str', "Ingrese la especialidad: ")
    experiencia = validar_entrada('int', "Ingrese los años de experiencia: ")
    disponibilidad = validar_entrada('str', "Ingrese la disponibilidad horaria: ")

    enfermera = Enfermera(nombre, identificacion, edad, contacto, correo, direccion, especialidad, experiencia, disponibilidad)
    return enfermera

def mostrar_enfermeras(lista):
    if not lista:
        print("No hay registros disponibles.")
    for enfermera in lista:
        print(enfermera)

def guardar_en_archivo(filename, data):
    with open(filename, 'w') as file:
        json.dump([enfermera.__dict__ for enfermera in data], file, indent=4)

def cargar_de_archivo(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Enfermera(**enfermera) for enfermera in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def eliminar_registro(lista, identificacion):
    for i, enfermera in enumerate(lista):
        if enfermera.identificacion == identificacion:
            del lista[i]
            print(f"Registro con identificación {identificacion} eliminado.")
            return True
    print(f"No se encontró un registro con la identificación {identificacion}.")
    return False

def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def registrar_usuario():
    enfermeras = cargar_de_archivo("enfermeras.json")

    while True:
        print("\nOpciones:")
        print("1. Registrar una enfermera")
        print("2. Eliminar un registro")
        print("3. Mostrar registros")
        print("4. Salir")

        opcion = validar_entrada('int', "Seleccione una opción: ")

        if opcion == 1:
            enfermeras.append(registrar_enfermera())
            print("Datos de la enfermera registrados exitosamente.")
        elif opcion == 2:
            identificacion = validar_entrada('str', "Ingrese la identificación del registro a eliminar: ")
            eliminar_registro(enfermeras, identificacion)
        elif opcion == 3:
            ordenar_burbuja(enfermeras)
            print("\nEnfermeras Registradas:")
            mostrar_enfermeras(enfermeras)
        elif opcion == 4:
            print("Guardando registros...")
            guardar_en_archivo("enfermeras.json", enfermeras)
            print("Registros guardados. Saliendo.")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    registrar_usuario()
