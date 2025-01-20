import csv

def leer_calificaciones(nombre_fichero):
    """
    Lee el fichero CSV de calificaciones y devuelve una lista de diccionarios ordenada por apellidos.
    """
    with open(nombre_fichero, newline='', encoding='utf-8') as fichero:
        lector = csv.DictReader(fichero)
        lista = list(lector)
        # Convertimos los valores numéricos y ordenamos por apellido
        for alumno in lista:
            alumno["Examen1"] = float(alumno["Examen1"])
            alumno["Examen2"] = float(alumno["Examen2"])
            alumno["Practicas"] = float(alumno["Practicas"])
            alumno["Asistencia"] = float(alumno["Asistencia"])
        return sorted(lista, key=lambda x: x["Apellido"])

def calcular_nota_final(lista_alumnos):
    """
    Calcula la nota final para cada alumno y la añade al diccionario correspondiente.
    """
    for alumno in lista_alumnos:
        alumno["Nota_Final"] = (
            0.3 * alumno["Examen1"] +
            0.3 * alumno["Examen2"] +
            0.4 * alumno["Practicas"]
        )
    return lista_alumnos

def clasificar_alumnos(lista_alumnos):
    """
    Clasifica a los alumnos en aprobados y suspensos según los criterios especificados.
    """
    aprobados = []
    suspensos = []
    for alumno in lista_alumnos:
        if (
            alumno["Asistencia"] >= 75 and
            alumno["Examen1"] >= 4 and
            alumno["Examen2"] >= 4 and
            alumno["Practicas"] >= 4 and
            alumno["Nota_Final"] >= 5
        ):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos

# Ejecución
nombre_fichero = "./T10Ejercicios/calificaciones.csv"
alumnos = leer_calificaciones(nombre_fichero)
alumnos_con_nota_final = calcular_nota_final(alumnos)
aprobados, suspensos = clasificar_alumnos(alumnos_con_nota_final)

# Mostrar resultados
print("Aprobados:")
for alumno in aprobados:
    print(f"{alumno['Nombre']} {alumno['Apellido']} - Nota final: {alumno['Nota_Final']:.2f}")

print("\nSuspensos:")
for alumno in suspensos:
    print(f"{alumno['Nombre']} {alumno['Apellido']} - Nota final: {alumno['Nota_Final']:.2f}")
