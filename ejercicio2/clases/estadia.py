import math
from clases.vehiculo import Vehiculo


class Estadia:
    def __init__(self, vehiculo: Vehiculo, entrada_min: int):
        self.vehiculo = vehiculo
        self.entrada_min = entrada_min
        self.salida_min = None
        self.cobro = 0

    def cerrar(self, salida_min: int) -> int:
        # Validación simple
        if salida_min <= self.entrada_min:
            raise ValueError("La hora de salida debe ser mayor que la hora de entrada.")

        self.salida_min = salida_min

        minutos = self.salida_min - self.entrada_min
        horas = minutos / 60

        # Fracción de hora: se cobra redondeando hacia arriba
        horas_cobradas = math.ceil(horas)

        base = horas_cobradas * self.vehiculo.tarifa_por_hora()

        # Recargo horario punta (simulado por rangos)
        # Punta: 07:00-09:59 y 18:00-20:59
        recargo = 0
        if self._hay_punta(self.entrada_min, self.salida_min):
            recargo = int(base * 0.25)  # 25%

        self.cobro = base + recargo
        return self.cobro

    def _hay_punta(self, entrada: int, salida: int) -> bool:
        rangos = [
            (7 * 60, 10 * 60),    # 07:00 a 10:00
            (18 * 60, 21 * 60),   # 18:00 a 21:00
        ]
        for minuto in range(entrada, salida):
            for ini, fin in rangos:
                if ini <= minuto < fin:
                    return True
        return False
