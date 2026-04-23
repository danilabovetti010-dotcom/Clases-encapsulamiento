class Auto:
    def __init__(self, marca, modelo, fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.fabricacion = fabricacion

    def obtener_marca(self):
        return self.marca

    def establecer_marca(self, marca):
        self.marca = marca

    def obtener_modelo(self):
        return self.modelo

    def establecer_modelo(self, modelo):
        self.modelo = modelo

    def obtener_fabricacion(self):
        return self.fabricacion

    def establecer_fabricacion(self, fabricacion):
        self.fabricacion = fabricacion

    def mostrar_informacion(self):
        print(f"Informacion del auto:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.fabricacion}")

if __name__ == "__main__":
    mi_auto = Auto("Ford", 206, 2010)

    mi_auto.mostrar_informacion()

    mi_auto.marca = "Chevrolet"
    mi_auto.fabricacion = 2012

    print("\nDespués de actualizar:")
    mi_auto.mostrar_informacion()