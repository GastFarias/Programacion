#Gaston Farias

#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
#Construye los siguientes métodos para la clase:
# *Un constructor, donde los datos pueden estar vacíos.
# *Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. 
# *mostrar(): Muestra los datos de la persona. 
# *esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.setNombre(nombre)
        self.setEdad(edad)
        self.setDni(dni)


    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre
        

    def getEdad(self):
        return str(self.edad)

    def setEdad(self, edad):
        if edad != "":
            if edad.isnumeric():
                self.edad = edad
            else:
                nuevoEdad = input("Ingreso de edad Incorrecto, Ingrese nuevamente: ")
                self.setEdad(nuevoEdad)            
        else:
            self.edad = edad


    def getDni(self):
        return self.dni

    def setDni(self, dni):
        self.dni = dni
        if dni != "":
            if dni.isnumeric() and len(dni) >= 7 and len(dni) <= 8:
                self.dni = dni
            else:
                nuevoDni = input("Ingreso de DNI incorrecto, vuelva a ingresarlo.\n Intente sin puntos y sin caracteres especiales o letras: ")
                self.setDni(nuevoDni)
        else:
            self.dni = dni

    def Imprimir(self):
        print(f" Nombre: {self.nombre} \n Edad: {self.edad}\n Dni: {self.dni} \n")

    def esMayorDeEdad(self):
        if int(self.edad) >= 18: 
            variable = True
            return variable
        else:
            variable = False
            return variable
    

def Ingreso():
    nombre = input("Ingrese nombre: ")
    edad = input("Ingrese edad: ")
    dni = input("Ingrese DNI: ")
    persona = Persona(nombre, edad, dni)
    persona.Imprimir()
    var = persona.esMayorDeEdad()
    print("Es mayor de edad? " + str(var))

#Ingreso()
