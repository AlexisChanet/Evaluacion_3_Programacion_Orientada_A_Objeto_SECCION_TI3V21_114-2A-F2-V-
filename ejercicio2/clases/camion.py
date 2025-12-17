from clases.vehiculo import Vehiculo


class Camion(Vehiculo):
    def get_tipo(self) -> str:
        return "Camión"

    def tarifa_por_hora(self) -> int:
        return 2500
