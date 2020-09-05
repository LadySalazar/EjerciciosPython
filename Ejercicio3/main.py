def ImprimirCaracter(palabra):
    primera = palabra[0]
    longitud = len(palabra)
    ultimo = palabra[longitud - 1]
    respuesta=f"Primera letra {primera} y {ultimo} letra"
    return respuesta
def main():
    print("Bienvenido al programa Palabras")
    Palabra=input("por favor ingrese la Palabra:  ")
    print(ImprimirCaracter(Palabra))
if __name__ == '__main__':
    main()