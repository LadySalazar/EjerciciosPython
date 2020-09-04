def NumeroEntero(Numero):
    aux=Numero%2
    if aux==0:
        respuesta=True
    else :
        respuesta = False
    return respuesta
def main():
    print("Bienvenido al programa de Numero par")
    Numero =-1
    while Numero<0:
        Numero=int(input("por favor ingrese el numero:  "))

    NumeroEntero(Numero)
    if NumeroEntero(Numero)==True:
        print("El número es par")
    else:
        print("El número es impar")

if __name__ == '__main__':
    main()
