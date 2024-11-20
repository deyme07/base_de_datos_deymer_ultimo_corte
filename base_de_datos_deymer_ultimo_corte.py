import json
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
                return entrada
        elif tipo == 'gmail':
            if "@" in entrada and "." in entrada:
                return entrada
            else:
                print("Por favor, ingrese un correo electrónico válido.")

def registrar_persona():
    return [
        validar_entrada('str', "Ingrese su nombre completo: "),
        validar_entrada('str', "Ingrese su número de identificación profesional si es enfermera sino ingrese su numero de documento: "),
        validar_entrada('int', "Ingrese su edad: "),
        validar_entrada('str', "Ingrese su número de contacto: "),
        validar_entrada('gmail', "Ingrese su correo electrónico: "),
        validar_entrada('str', "Ingrese su dirección: ")
    ]

def registrar_enfermera():
    return registrar_persona() + [
        validar_entrada('str', "Ingrese la especialidad: "),
        validar_entrada('int', "Ingrese los años de experiencia: "),
        validar_entrada('str', "Ingrese la disponibilidad horaria: ")
    ]

def registrar_paciente():
    return registrar_persona() + [
        validar_entrada('str', "Ingrese el género: "),
        validar_entrada('str', "Ingrese la enfermedad o condición médica principal: "),
        validar_entrada('str', "Ingrese el nombre y número de contacto de una persona en caso de emergencia: "),
        validar_entrada('str', "Ingrese alergias y medicamentos actuales: ")
    ]

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def buscar_por_identificacion(lista, identificacion):
    for persona in lista:
        if persona[1] == identificacion:
            return persona
    return None

# Implementación del algoritmo de Burbuja
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparación por el nombre (posición 0 en cada lista)
            if lista[j][0].lower() > lista[j + 1][0].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def guardar_en_archivo(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def cargar_de_archivo(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def eliminar_registro(lista, identificacion):
    for i, persona in enumerate(lista):
        if persona[1] == identificacion:
            del lista[i]
            print(f"Registro con identificación {identificacion} eliminado.")
            return True
    print(f"No se encontró un registro con la identificación {identificacion}.")
    return False

def registrar_usuario():
    enfermeras = cargar_de_archivo("enfermeras.json")
    pacientes = cargar_de_archivo("pacientes.json")

def registrar_usuario():
    enfermeras = []  # Lista para almacenar registros de enfermeras
    pacientes = []   # Lista para almacenar registros de pacientes

    while True:
        print("\nOpciones:")
        print("1. Registrar una enfermera")
        print("2. Registrar un paciente")
        print("3. Eliminar un registro")
        print("4. Mostrar registros")
        print("5. Salir")
        
        opcion = validar_entrada('int', "Seleccione una opción: ")

        if opcion == 1:
            enfermeras.append(registrar_enfermera())
            print("Datos de la enfermera registrados exitosamente.")
        elif opcion == 2:
            pacientes.append(registrar_paciente())
            print("Datos del paciente registrados exitosamente.")
        elif opcion == 3:
            identificacion = validar_entrada('str', "Ingrese la identificación del registro a eliminar: ")
            if not eliminar_registro(enfermeras, identificacion):
                eliminar_registro(pacientes, identificacion)
        elif opcion == 4:
            print("\nEnfermeras Registradas:")
            mostrar_matriz(enfermeras)
            print("\nPacientes Registrados:")
            mostrar_matriz(pacientes)
        elif opcion == 5:
            print("Guardando registros...")
            guardar_en_archivo("enfermeras.json", enfermeras)
            guardar_en_archivo("pacientes.json", pacientes)
            print("Registros guardados. Saliendo.")
            break
        else:
            print("Opción no válida, intente de nuevo.")


    # Ordenar las listas usando Burbuja
    ordenar_burbuja(enfermeras)
    ordenar_burbuja(pacientes)

    # Mostrar los registros ordenados
    print("\nEnfermeras Registradas:")
    mostrar_matriz(enfermeras)

    print("\nPacientes Registrados:")
    mostrar_matriz(pacientes)

    # Búsqueda por identificación
    identificacion = input("\nIngrese una identificación para buscar: ")
    resultado = buscar_por_identificacion(enfermeras + pacientes, identificacion)
    if resultado:
        print("Persona encontrada:", resultado)
    else:
        print("No se encontró ninguna persona con esa identificación.")

registrar_usuario()