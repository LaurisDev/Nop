import random


class Ecuacion:

    def __init__(self):
        # Clase Ecuacion creada con numeros y operadores random

        self.numeros: list = [random.randint(1, 9) for _ in range(3)]  # Generar 4 números enteros de 0 a 9
        self.ecuacion: list = []

        # numeros generados {self.numeros}

        self.operadores: list = ["*", "/", "+", "-"]

        # operadores generados {self.operadores}

    """ metodo confirmar logica se encarga de analizar la ecuacion generada y obtener el resultado de la misma"""

    def confirmar_logica(self, _lista: list) -> int:
        # METODO CONFIRMAR_LOGICA LLAMADO
        print(_lista)

        """ bucle inicial para operadores de mayor importancia * y /"""
        for i in range(2):
            for i in range(len(_lista)):
                if i < len(_lista):
                    # inicio del bucle for */

                    if _lista[i] == "*":

                        _lista[i] = _lista[i - 1] * _lista[i + 1]
                        _lista.remove(_lista[i - 1])
                        _lista.remove(_lista[i])

                    elif _lista[i] == "/":

                        _lista[i] = int(_lista[i - 1] / _lista[i + 1])
                        _lista.remove(_lista[i - 1])
                        _lista.remove(_lista[i])


                    else:
                        pass
                        # " no paso la condicion, saltando al siguiente"

        """ bucle secundario para operadores de menor importancia + y -"""
        for i in range(2):
            for i in range(len(_lista)):
                if i < len(_lista):
                    # inicio del bucle for +-

                    # objeto a revisar: {_lista[i]}

                    if _lista[i] == "+":

                        _lista[i] = _lista[i - 1] + _lista[i + 1]
                        _lista.remove(_lista[i - 1])
                        _lista.remove(_lista[i])

                    elif _lista[i] == "-":

                        _lista[i] = _lista[i - 1] - _lista[i + 1]
                        _lista.remove(_lista[i - 1])
                        _lista.remove(_lista[i])

                    else:
                        pass
                        # " no paso la condicion, saltando al siguiente"

        return _lista[0]

    def generar_ecuacion(self):
        # "METODO GENERAR_ECUACION LLAMADO"

        ecuaciones: list = [self.numeros[0], random.choice(self.operadores)]

        for i in range(1, 2):
            numero: int = self.numeros[i]
            operador: str = random.choice(self.operadores)

            if operador == "/" and numero == 0:  # Evitar la división por cero
                numero = 1

            ecuaciones.append(numero)
            ecuaciones.append(operador)

        ecuaciones.append(self.numeros[2])
        ecuaciones.append("=")
        self.ecuacion = self.ecuacion + ecuaciones

        #print(f"ecuacion generada: {self.ecuacion}")

        confirmar_logica: int = self.confirmar_logica(ecuaciones)

        #print(f" confirmacion, tipo de retorno {type(confirmar_logica)}")
        #print(f" confirmacion, valor del retorno{confirmar_logica}")
        #print(f" ecuacion resultante: {self.ecuacion}")

        if type(confirmar_logica) == float:
            #print("generando otra secuencia")
            self.ecuacion = []
            self.generar_ecuacion()
        elif confirmar_logica < -10:
            #print("generando otra secuencia")
            self.ecuacion = []
            self.generar_ecuacion()
        elif -10 < confirmar_logica < 0:
            self.ecuacion.append(str(confirmar_logica)[0])
            self.ecuacion.append(str(confirmar_logica)[1])

        elif 10 > confirmar_logica >= 0:
            self.ecuacion.append(0)
            self.ecuacion.append(confirmar_logica)

        elif confirmar_logica >= 10:
            self.ecuacion.append(str(confirmar_logica)[0])
            self.ecuacion.append(str(confirmar_logica)[1])

        #print(f" resultado: {confirmar_logica}")
        #print(f"RETORNO DEL METODO GENERAR SECUENCIA = {self.ecuacion}")

        return self.ecuacion

