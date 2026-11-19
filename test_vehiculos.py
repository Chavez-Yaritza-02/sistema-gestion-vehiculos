"""Pruebas básicas. Ejecutar: python -m unittest -v"""

import unittest
from abc import ABC
from main import Automovil, Camion, Vehiculo


class PruebasVehiculos(unittest.TestCase):
    def test_vehiculo_es_abstracto(self):
        self.assertTrue(issubclass(Vehiculo, ABC))
        with self.assertRaises(TypeError):
            Vehiculo("Marca", "Modelo")

    def test_herencia_simple(self):
        self.assertEqual(Automovil.__bases__, (Vehiculo,))
        self.assertEqual(Camion.__bases__, (Vehiculo,))

    def test_metodos_propios(self):
        auto = Automovil("Toyota", "Corolla")
        camion = Camion("Volvo", "FH")
        self.assertTrue(hasattr(auto, "abrir_maletero"))
        self.assertFalse(hasattr(camion, "abrir_maletero"))
        self.assertTrue(hasattr(camion, "cargar_mercancia"))
        self.assertFalse(hasattr(auto, "cargar_mercancia"))

    def test_polimorfismo(self):
        self.assertNotEqual(Automovil.encender, Camion.encender)
        for vehiculo in [Automovil("Toyota", "Corolla"), Camion("Volvo", "FH")]:
            self.assertTrue(callable(vehiculo.encender))
            self.assertEqual(vehiculo.mostrar_datos(), f"{vehiculo.marca} {vehiculo.modelo}")


if __name__ == "__main__":
    unittest.main()
