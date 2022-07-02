import os, time

os.system('cls')

banner = """
[1] - Sumar
[2] - Restar
[3] - Multiplicar
[4] - Dividir
[5] - Salir
"""

class Main():
    def sumar(a, b):
        return print(a + b)

    def restar(a, b):
        return print(a - b)

    def multiplicar(a, b):
        return print(a * b)

    def dividir(a, b):
        return print(a / b)

    def inicio():
        print(banner)
        Main.accion()

    def accion():
        opcion = int(input('Que accion quieres hacer ? : '))
        if opcion == 1:
            numero1 = int(input('Primer numero : '))
            numero2 = int(input('Segundo numero : '))
            Main.sumar(numero1, numero2)
            os.system('pause')
            os.system('cls')
            Main.inicio()

        if opcion == 2:
            numero1 = int(input('Primer numero : '))
            numero2 = int(input('Segundo numero : '))
            Main.restar(numero1, numero2)
            os.system('pause')
            os.system('cls')
            Main.inicio()

        if opcion == 3:
            numero1 = int(input('Primer numero : '))
            numero2 = int(input('Segundo numero : '))
            Main.multiplicar(numero1, numero2)
            os.system('pause')
            os.system('cls')
            Main.inicio()
        
        if opcion == 4:
            numero1 = int(input('Primer numero : '))
            numero2 = int(input('Segundo numero : '))
            Main.dividir(numero1, numero2)
            os.system('pause')
            os.system('cls')
            Main.inicio()

        if opcion == 5:
            print('Saliendo')
            time.sleep(2)
            exit()

Main.inicio()