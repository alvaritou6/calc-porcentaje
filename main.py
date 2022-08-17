import time

print('Para calcular un descuento o interes siga las siguientes instrucciones: ')

BaseNum = float(
    input('Introduce el valor a realizar el descuento o interes: '))
Porc = float(
    input('Introduce la cantidad de descuento o interes que desea aplicar: '))
option = 0

ResultPorc = (BaseNum*Porc)/100

while True:
    print("""
    ¿Que deseas hacer?

    1. Realizar un descuento.
    2. Realizar un interes.
    3. Ver el porcentaje en numero.
    4. Cambiar los números.
    5. Apagar la calculadora.

        Creador Alvaro
    """)
    option = int(input('Introduce una opcion: '))

    if option == 1:
        print(" ")
        print("Descuento aplicado en", BaseNum, "-",
              Porc, "%off. El precio final es de:", BaseNum-ResultPorc)
    elif option == 2:
        print(" ")
        print("Interes aplicado en", BaseNum, "+", Porc,
              "%. El precio final es de:", BaseNum+ResultPorc)
    elif option == 3:
        print(" ")
        print("El porcentaje en numero es:", ResultPorc)
    elif option == 4:
        print(" ")
        BaseNum = float(
            input('Introduce el valor a realizar el descuento o interes: '))
        Porc = float(
            input('Introduce la cantidad de descuento o interes que desea aplicar: '))
        ResultPorc = (BaseNum*Porc)/100
    elif option == 5:
        print("La calculadora será apagada en 3 segundos. Nos vemos pronto :D")
        time.sleep(3)
        break
    else:
        print(" ")
        print("Opcion Incorrecta. Porfavor verifica la opcion ingresada")
