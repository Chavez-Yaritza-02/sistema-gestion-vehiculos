"""Actividad individual 3: Sistema de gestión de vehículos.
Ejemplo de abstracción, herencia simple y polimorfismo en Python.
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """Clase abstracta que contiene atributos comunes."""

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def encender(self):
        """Cada tipo de vehículo define cómo enciende."""

    def mostrar_datos(self):
        return f"{self.marca} {self.modelo}"


class Automovil(Vehiculo):
    def encender(self):
        print(f"El automóvil {self.mostrar_datos()} ha arrancado.")

    def abrir_maletero(self):
        print("Maletero abierto.")


class Camion(Vehiculo):
    def encender(self):
        print(f"El camión {self.mostrar_datos()} ha arrancado.")

    def cargar_mercancia(self):
        print("Mercancía cargada en el camión.")


def main():
    automovil = Automovil("Toyota", "Corolla")
    camion = Camion("Volvo", "FH")

    # Polimorfismo: mismo método, diferente implementación.
    vehiculos = [automovil, camion]
    for vehiculo in vehiculos:
        vehiculo.encender()

    # Cada vehículo tiene solo los métodos que le corresponden.
    automovil.abrir_maletero()
    camion.cargar_mercancia()

    assert not hasattr(camion, "abrir_maletero")
    print("Comprobación correcta: Camion no tiene abrir_maletero().")


if __name__ == "__main__":
    main()
