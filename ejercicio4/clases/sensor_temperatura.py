import random
from clases.sensor import Sensor


class SensorTemperatura(Sensor):
    def __init__(self, sensor_id: str, nombre: str, unidad: str = "C"):
        super().__init__(sensor_id, nombre)
        # Este sensor puede “leer” en C o F, pero el sistema lo mostrará en Celsius
        self.unidad = unidad.upper()  # "C" o "F"

    def tipo(self) -> str:
        return "Temperatura"

    def unidad_estandar(self) -> str:
        return "°C"

    def _a_celsius(self, valor: float) -> float:
        # Si viene en Fahrenheit, lo convertimos a Celsius
        if self.unidad == "C":
            return valor
        return (valor - 32) * 5 / 9

    def leer(self) -> float:
        # Simulación: generamos un valor posible según la unidad
        if self.unidad == "C":
            valor = random.uniform(-10, 40)
        else:
            valor = random.uniform(14, 104)

        # Normalizamos a Celsius
        valor_c = self._a_celsius(valor)

        # Validación simple para evitar valores absurdos
        if valor_c < -50 or valor_c > 80:
            raise ValueError("Temperatura fuera de rango para el sistema.")

        valor_c = round(valor_c, 2)

        # Guardamos la lectura ya en unidad estándar (Celsius)
        self.registrar_lectura(valor_c)
        return valor_c
