from reloj import Reloj

alarmas = []

nueva_alarma = Reloj()
nueva_alarma.horas = 99

alarmas.append(nueva_alarma)

nueva_nueva_alarma = Reloj()
nueva_nueva_alarma.definir_alarma(23, 690, 1)
alarmas.append(nueva_nueva_alarma)

for alarma in alarmas:
    print(alarma)
