
#Imprimimos las opciones para el usuario
print("1 - Balance")
print("2 - Retiro")
print("3 - Deposito")
print("4 - Terminar")
print(" ")

#Establecemos que la cuenta empiece con 1000 dólares
x= 1000

while True:
    option = int(input("Ingrese una opción: "))
    if option == 1:
        print(x) #Imprima el balance actual
    elif option == 2:
        substract = float(input("Cuánto desea retirar?: ")) #Creamos una variable de tipo float para el monto a retirar
        if x > 0 and substract < x: #Condición -> SI el balance es mayor a 0 y el monto a retirar es menor que el balance
            x = x-substract #El balance será igual al balance menos el monto a retirar
            print("Balance actualizado ",x)
        else: #SI el balance es mayor o menor a 0 y el monto a retirar es mayor que el balance
            print("Balance insuficiente!")
    elif option == 3:
        add = float(input("Cuánto desea depositar?: ")) #Variable de tipo float para monto a consignar
        x = x + add #El balance es igual al balance + el monto a consignar
        print("Balance actualizado ",x)
    elif option == 4:
        exit() #El usuario desea salir del cajero




