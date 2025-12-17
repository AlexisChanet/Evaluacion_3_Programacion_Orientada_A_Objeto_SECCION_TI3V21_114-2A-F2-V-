from clases.medio_pago import MedioPago


class Transferencia(MedioPago):
    def __init__(self):
        super().__init__("Transferencia")

    def calcular_total(self, monto: int) -> int:
        # Sin recargo
        return monto
