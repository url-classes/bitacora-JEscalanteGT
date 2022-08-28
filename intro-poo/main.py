from gato import Gato
from repeat_timer import RepeatTimer


def main():
    print('Bienvenido al simulador de mascotas')
    nombre = input('Ingrese el nombre de su mascota: ')
    mascota = Gato(nombre)

    timer = RepeatTimer(1, mascota.respirar)
    timer.start()

    while True:
        print('Mi mascota:')
        print("Nombre: ", mascota.nombre)
        print("Energía: ", mascota.energia)
        print('Opciones:')
        print('1- Saludar mascota')
        print('10- Salir')
        opcion = int(input('Ingrese una opción: '))
        if opcion == 1:
            mascota.saludar()
        if opcion == 10:
            break


main()
