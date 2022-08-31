import Poo1


class Cuenta:
    def __init__(self, titular, saldo):
        self.setTitular(titular)
        self.setSaldo(saldo)

    @property
    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular

    @property
    def getSaldo(self):
        return self.saldo

    def setSaldo(self, saldo):
        self.saldo = saldo
        print("El saldo actual es: " + self.saldo)

    @property
    def getEdadTitular(self):
        return self.titular.edad

    def Ingreso(self):
        #self.saldo =+ ingreso
        ingreso = input("Ingrese el monto a depositar: ")
        if ingreso.isnumeric():
            actual = int(self.getSaldo)
            self.setSaldo(str(actual + int(ingreso)))
            
        else:
            print("Ingreso invalido, recuerde utilizar numeros enteros. No se permiten puntos, comas o letras.")
            self.Ingreso()
    
    def Retiro(self):
        actual = self.getSaldo
        self.ImprimirSaldo()
        retiro = input("Ingrese el monto a retirar: ")

        if retiro != "" and retiro.isnumeric():
            if retiro > self.getSaldo:
                if int(actual) >= 0:
                    self.setSaldo(str(int(actual) - int(retiro)))

                else:
                    print("Saldo insuficiente. Esta cuenta ya registra deuda.")
                    self.ImprimirSaldo()
                    self.ProponerIngreso()
            else:
                self.setSaldo(str(int(actual) - int(retiro)))
        else:
            n = input("Ingreso invalido, recuerde utilizar numeros enteros."+
            " No se permiten puntos, comas o letras.\n Pulse 'ENTER' para continuar. \n")
            self.Retiro()
    
    def ProponerIngreso(self):
        print("¿Desea realizar un nuevo deposito?")
        resp = input("Indique 1 para SI \nIndique 2 para NO: ")
        if resp == "1":
            self.Ingreso()
        elif resp == "2":
            pass
        else:
            self.ProponerIngreso()

    def ImprimirSaldo(self):
        saldo = self.getSaldo
        print("El saldo disponible es: " + saldo)

    def ConsultarCliente(self):
        nombre = self.getTitular.getNombre()
        dni = self.getTitular.getDni()
        edad = self.getTitular.getEdad()
        print("El cliente es: " + nombre + "\n    Edad: " + edad + "\n    DNI: " + dni)
#--------------------------------------------------------------------------------------------
#Cierre Clase Cuenta
#--------------------------------------------------------------------------------------------


def DefinirTitular():
    nombre = input("Defina el nombre del titular: ")
    dni = input ("Indeque el DNI de " + nombre + ": ")
    edad = input("Indique la edad de " + nombre + ": ")

    titular = Poo1.Persona(nombre, edad, dni)
    return titular

def DefinirSaldoInicial():
    inicial = input("Defina el saldo inicial. Este ingreso es opcional, puede igresarlo mas tarde. ")
    if inicial != "":
        if inicial.isnumeric():
            return inicial
        else:
            DefinirSaldoInicial()
    else:
        return inicial

def Menu(cuenta):
    op = input("\n\nElija una accion: \n"+
    "     1- Ingresar Dinero.\n"+
    "     2- Retirar Dinero. \n"+
    "     3- Consultar Saldo Disponible. \n"+
    "     4- Consultar datos del cliente. \n"+
    "     9- Salir:  \n\n")
    if op == "1":
        cuenta.Ingreso()
        Menu(cuenta)
    elif op == "2":
        cuenta.Retiro()
        Menu(cuenta)
    elif op == "3":
        cuenta.ImprimirSaldo()
        Menu(cuenta)
    elif op == "4":
        cuenta.ConsultarCliente()
        Menu(cuenta)
    elif op == "9":
        print("---Saliendo--- \n-Gracias por utilizar nuestro sistema-")
    else:
        print("Opcion Invalida. Vuelva a intentarlo.")
        Menu(cuenta)

#titular = DefinirTitular()
#inicial = DefinirSaldoInicial()

#cuenta = Cuenta(titular, inicial)
#Menu(cuenta)

