import random
from clases.sensor import Sensor


class SensorMovimiento(Sensor):
    def tipo(self) -> str:
        return "Movimiento"

    def unidad_estandar(self) -> str:
        return "0/1"

    def leer(self) -> int:
        # Simulación: 0 = no hay movimiento, 1 = hay movimiento
        valor = random.choice([0, 1])

        # Validación mínima
        if valor not in (0, 1):
            raise ValueError("Movimiento inválido (solo 0 o 1).")

        # Guardamos la lectura (0/1)
        self.registrar_lectura(valor)
        return valor
