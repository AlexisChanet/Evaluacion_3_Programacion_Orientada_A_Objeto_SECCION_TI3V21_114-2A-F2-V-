from clases.vehiculo import Vehiculo


class Auto(Vehiculo):
    def get_tipo(self) -> str:
        return "Auto"

    def tarifa_por_hora(self) -> int:
        return 1200
