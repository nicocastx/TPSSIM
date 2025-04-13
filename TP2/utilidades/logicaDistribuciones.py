import math
import random


class logicaDistribuciones():
    def __init__(self):
        pass

    def truncar(self, numero):
        factor = 10 ** 4
        numero_escalado = numero * factor
        numero_truncado_escalado = math.trunc(numero_escalado)
        return numero_truncado_escalado / factor

    def contadorIntervalos(self, serie, intervalos):
        contadores_intervalos = [0] * len(intervalos)
        maxSerie = max(serie)

        for numero in serie:
            for i, intervalo in enumerate(intervalos):
                if intervalo[0] <= numero < intervalo[1]:
                    contadores_intervalos[i] += 1
                    break
                if numero == maxSerie:
                    contadores_intervalos[-1] += 1
                    break
        return contadores_intervalos

    def generarIntervalos(self, serie, numIntervalos):

        # aplicarformula()
        a = self.truncar(min(serie))
        b = self.truncar(max(serie))
        print("minimo: " + str(a))
        print("maximo: " + str(b))  # número de intervalos


        # calcular el tamaño de cada intervalo -------------- CON PRECISION
        precision = 0.0001 # Va depender de la cantidad de decimales
        anchoIntervalo =((b - a) / numIntervalos)
        anchoIntervaloPrecisionTruncado = self.truncar((anchoIntervalo) + precision)
        print("Ancho de intervalo: " + str(anchoIntervaloPrecisionTruncado))

        intervalos = []

        for i in range(numIntervalos):
            inicio = a  # No truncar aquí todavía
            fin = a + anchoIntervalo

            if i == numIntervalos - 1:
                intervalos.append((self.truncar(inicio), self.truncar(b)))  # Truncar solo al final
            else:
                intervalos.append((self.truncar(inicio), self.truncar(fin)))

            a = fin  # Actualizar a sin truncar

        print("cantidad de intervalos:", len(intervalos))


        return intervalos

    def generar_normal_box_muller(self, n, mu, sigma):
        normales = []
        for i in range(n // 2):
            u1 = random.random()
            u2 = random.random()
            r = math.sqrt(-2 * math.log(u1))
            theta = 2 * math.pi * u2
            z1 = r * math.cos(theta)
            z2 = r * math.sin(theta)
            normales.append(z1 * sigma + mu)
            normales.append(z2 * sigma + mu)

        # Si es impar, generamos un valor más
        if n % 2 == 1:
            u1 = random.random()
            u2 = random.random()
            r = math.sqrt(-2 * math.log(u1))
            theta = 2 * math.pi * u2
            z1 = r * math.cos(theta)
            normales.append(z1 * sigma + mu)

        return normales
