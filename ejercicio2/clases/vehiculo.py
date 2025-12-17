class Vehiculo:
    def __init__(self, patente: str):
        self.patente = patente.strip().upper()

    def get_tipo(self) -> str:
        return "Vehículo"

    def tarifa_por_hora(self) -> int:
        # Lo definen las clases hijas
        raise NotImplementedError

    def __str__(self) -> str:
        return f"{self.patente} [{self.get_tipo()}]"
