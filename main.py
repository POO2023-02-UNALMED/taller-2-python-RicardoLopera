class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self,color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color
class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        cantidadAsientos = 0
        for i in range(len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                cantidadAsientos += 1
            else:
                continue
        return cantidadAsientos

    def verificarIntegridad(self):
        verificarRegistro = True
        for i in range(len(self.asientos)):
            if type(self.asientos[i]) == Asiento:
                if self.registro != self.asientos[i].registro:
                    verificarRegistro = False
        
        if self.motor.registro == self.registro and verificarRegistro == True:
            return "Auto original"
        else:
            return "Las piezas no son originales"

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registronew):
        self.registro = registronew

    def asignarTipo(self,tipo):
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo
    

        
