

def crearTabla (numero):
    intNumero = int(numero)
    tabla=[]
     
    for i in range(11):  # Itera desde 0 hasta 4
        resultado = i*intNumero
        linea = str(intNumero)  + 'x' + str(i) + '=' + str(resultado)
        tabla.append(linea)
        
    return tabla
    
def unoAlDiez(numero):
    intNumero = int(numero)
    nombreFichero = './T10Ejercicios/tabladel' + str(numero) + '.txt'
    try:
        # Abrir el archivo en modo lectura/escritura
        with open(nombreFichero,"w") as archivo:
            archivo.write(str(crearTabla(intNumero)))
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    else:
        print("\nEl archivo fue actualizado correctamente.")

unoAlDiez(4)