from clases.medio_pago import MedioPago


class Tarjeta(MedioPago):
    def __init__(self, cupo: int):
        super().__init__("Tarjeta")
        self.cupo = cupo

    def validar(self, monto: int) -> None:
        if monto > self.cupo:
            raise ValueError("Cupo insuficiente en la tarjeta.")

    def calcular_total(self, monto: int) -> int:
        # 5% de recargo
        recargo = int(monto * 0.05)
        return monto + recargo
