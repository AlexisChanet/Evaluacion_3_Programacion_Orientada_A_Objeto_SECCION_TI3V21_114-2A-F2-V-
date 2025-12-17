import random
from clases.sensor import Sensor


class SensorHumedad(Sensor):
    def tipo(self) -> str:
        return "Humedad"

    def unidad_estandar(self) -> str:
        return "%"

    def leer(self) -> float:
        # Simulación: humedad entre 0 y 100
        valor = round(random.uniform(0, 100), 2)

        # Validación pedida por el enunciado
        if valor < 0 or valor > 100:
            raise ValueError("Humedad fuera de rango (0 a 100).")

        # Guardamos el valor normalizado (en %)
        self.registrar_lectura(valor)
        return valor
