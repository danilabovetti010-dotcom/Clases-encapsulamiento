class Auto:
    def __init__(self, marca, modelo, fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.fabricacion = fabricacion
        
    def mostrar_informacion(self):
        print(f"Informacion del auto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.fabricacion}")

if __name__ == "__main__":
    auto1 = Auto("Ford", 206, 2010)

    auto1.mostrar_informacion()

    auto1.marca = "Chevrolet"
    auto1.fabricacion = 2012

    print("\nDespués de actualizar:")
    auto1.mostrar_informacion()
