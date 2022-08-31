#Gaston Farias
from Poo2 import Cuenta, DefinirSaldoInicial, DefinirTitular, Menu
from Poo1 import Persona

class CuentaJoven(Cuenta):
    def __init__(self, titular, saldo, bonificacion):
        super().__init__(titular, saldo)
        self.setBonificacion(bonificacion)
        #self.setTitular(titular)

    def setBonificacion(self, bonificacion):
        self.bonificacion = bonificacion
    
    @property
    def getBonificacion(self):
        return self.bonificacion

    @property
    def esTitularValido(self):
        tit = self.getEdadTitular
        if int(tit) >= 18 and int(tit) < 25:
            return True
        else: 
            return False

    def Retiro(self):
        if self.esTitularValido == True:
            antes = self.getSaldo
            super().Retiro()
            boni = ((int(antes) - int(self.getSaldo)) * int(self.bonificacion)) / 100
            print("Bonificacion cuenta joven: " + str(boni))
            self.setSaldo(str( int(self.getSaldo) + boni))
            

        else:
            print("No es un Titular valido para utilizar la 'cuenta joven'.")


def DefinirBonificacion():
    inicial = input("Defina la bonificacion en porcentaje.")
    if inicial != "":
        if inicial.isnumeric():
            return inicial
        else:
            print("Ingreso invalido, intente nuevamente sin caracteres especiales o letras.")
            DefinirBonificacion()
    else:
        print("Indique correctamente el valor.")



titular = DefinirTitular()
saldo = DefinirSaldoInicial()
bonificacion = DefinirBonificacion()

joven = CuentaJoven(titular, saldo, bonificacion)

Menu(joven)
