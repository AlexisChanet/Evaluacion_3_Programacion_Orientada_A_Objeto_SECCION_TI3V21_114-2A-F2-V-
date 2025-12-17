class Venta:
    def __init__(self, id_venta: int, monto: int, medio, total: int):
        self.id_venta = id_venta
        self.monto = monto
        self.medio = medio
        self.total = total

    def comprobante(self) -> str:
        return (
            f"Venta #{self.id_venta} | "
            f"Monto: ${self.monto} | "
            f"Medio: {self.medio} | "
            f"Total pagado: ${self.total}"
        )
