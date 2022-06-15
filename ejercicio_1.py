#ej1.- funcion que contenga un listado de palabras, 
#devuelva la mas larga 
#imprimir por pantalla la palabra resultante 
def encontrar_palabra_mayor(palabras):
    palabra_longitud = []
    for p in palabras:
        palabra_longitud.append((len(p), p))
    palabra_longitud.sort()
    return palabra_longitud[-1][1]

def main():
    palabras = ["cuestionable", "antigua", "arboles", "bañera", "ruborizado"]
    print(encontrar_palabra_mayor(palabras))

if __name__ == '__main__':
    main()