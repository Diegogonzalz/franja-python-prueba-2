#Ej3.- funcion que calcule el area de un circulo y
#otra que calcule el volumen de un cilindro 
#usando la primera funcion 

def area_circulo(radio):
    pi = 3.1415
    area = pi * radio ** 2
    return area

def volumen_cilindro(radio, altura):
    volumen = area_circulo(radio) * altura
    return volumen

def main():
  radio = float(input("Ingrese un radio en cm: "))
  altura = float(input("Escriba una altura en cm: "))
  print("El area de su circulo es "+str(area_circulo(radio)))
  print("El volumen del cilindro es "+str(volumen_cilindro(radio,altura)))

if __name__ == '__main__':
    main()