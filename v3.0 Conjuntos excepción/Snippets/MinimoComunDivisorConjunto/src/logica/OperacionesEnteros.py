from src.logica.operacionesEnteros import FaltanParametros
class OperacionesEnteros:
    def __init__(self, numeros):
        self.__numeros = numeros

    def calcularMCM(self):
        if len(self.__numeros) < 2:
            raise FaltanParametros
        elif len(self.__numeros) > 1:
            return self.MCMMasDosNumeros()
        else:
            return 0

    def MCM(self, numero1, numero2):
        return abs(numero1 * numero2) // self.MCD(numero1, numero2)

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCMMasDosNumeros(self):
        for n in self.__numeros:
            if not isinstance(n, int):
                raise ValueError

        cantidadNumeros = len(self.__numeros)
        mcm = self.MCM(self.__numeros[0], self.__numeros[1])
        i = 0
        while i < (cantidadNumeros - 2):
            mcm = self.MCM(mcm, self.__numeros[i+2])
            i = i + 1
        return mcm
