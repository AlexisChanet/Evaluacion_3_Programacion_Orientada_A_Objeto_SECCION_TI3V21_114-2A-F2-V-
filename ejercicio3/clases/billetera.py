from clases.medio_pago import MedioPago


class Billetera(MedioPago):
    def __init__(self, saldo: int):
        super().__init__("Billetera Digital")
        self.saldo = saldo

    def validar(self, monto: int) -> None:
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente en la billetera.")

    def calcular_total(self, monto: int) -> int:
        # $500 de recargo fijo
        return monto + 500
