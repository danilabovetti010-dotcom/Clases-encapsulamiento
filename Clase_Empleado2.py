#Crea una clase llamada Empleado con atributos nombre, salario y departamento. Implementa un método 
#que aumente el salario en un porcentaje dado y otro que muestre la información del empleado.

class Empleado:
    def __init__(self, nombre, departamento, salario):
        self.nombre = nombre
        self.departamento = departamento
        self.salario = salario

    def calcular_salario(self):
        return self.salario * 12

    def aumentar_salario(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Salario Actual: ${self.salario}")

if __name__ == "__main__":
    empleado1 = Empleado("Pepito", "Contabilidad", 1000)

    print("informacion:")
    empleado1.mostrar_informacion()

    print("\nSalario aumentado al 10%:")
    empleado1.aumentar_salario(10)

    empleado1.mostrar_informacion()

    print(f"Salario Anual Total: ${empleado1.calcular_salario()}")
 