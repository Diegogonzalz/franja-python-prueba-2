#Ej2.- pida dos palabras y
#diga si rima o no --> si concidera las ultimas 3 letras 
#--> ultimas 2 rima un poco 
#--> no riman,
#validar que las palabras tengan 3 letras (usar slices)



def main():
    palabra1 = input("Escriba una palabra: ")
    palabra2 = input("Escriba otra palabra: ")
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1[-3: ] == palabra2[-3: ]:
        print("tu palabra rima")
    elif palabra1[-2: ] == palabra2[-2: ]:
        print("tu palabra rima un poco")
    else:
        print("tu palabra no rima")


if __name__ == '__main__':
    main()