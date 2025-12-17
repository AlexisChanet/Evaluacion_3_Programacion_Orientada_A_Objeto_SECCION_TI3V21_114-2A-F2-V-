from clases.vehiculo import Vehiculo


class Moto(Vehiculo):
    def get_tipo(self) -> str:
        return "Moto"

    def tarifa_por_hora(self) -> int:
        return 800
