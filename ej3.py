def pedirNumero():
    numero1 = int(input("Por favor, introduce un número del uno al diez: "))
    numero2 = int(input("Por favor, introduce el número de línea del uno al diez: "))
    
    nombreFichero = f'./T10Ejercicios/tabladel{numero1}.txt'
    
    try:
        with open(nombreFichero, "r") as archivo:

            lineas = archivo.readlines()
            
            if 0 < numero2 <= len(lineas):
                linea = lineas[numero2 - 1].strip()
                print(f"Línea {numero2}: {linea}")
            else:
                print(f"No hay línea {numero2} en el archivo tabladel{numero1}.")
                
    except FileNotFoundError:
        print("El fichero no existe.")
 

pedirNumero()
