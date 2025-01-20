def pedirNumero ():
    numero = int(input("Por favor, introduce un número del uno al diez:"))
    
    nombreFichero = './T10Ejercicios/tabladel' + str(numero) + '.txt'
    try:
        # Abrir el archivo en modo lectura/escritura
        with open(nombreFichero,"r") as archivo:
            print(archivo.read())
    except Exception as e:
        print("El fichero no existe")
    
pedirNumero()