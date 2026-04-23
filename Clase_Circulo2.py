#Crea una clase llamada Circulo que tenga un atributo radio. 
#Implementa métodos para calcular el área y la circunferencia 
#del círculo, y asegúrate de que el radio no pueda ser negativo.

class Circulo:
    PI = 3.14
    def __init__(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo")
        self.radio = radio
        self.diametro = radio * 2

    def calcular_area (self):
        return self.PI * (self.radio ** 2)

    def calcular_circunferencia (self):
        return 2 * self.PI * self.radio


if __name__ == "__main__":
    try:
        circulo1 = Circulo(-5)
    
        print(f"Radio: {circulo1.radio}")
        print(f"Diametro: {circulo1.diametro}")
    
        print(f"Área: {circulo1.calcular_area()}")
        print(f"Circunferencia: {circulo1.calcular_circunferencia()}")
    
    except ValueError as e:
        print(f"Error: {e}")