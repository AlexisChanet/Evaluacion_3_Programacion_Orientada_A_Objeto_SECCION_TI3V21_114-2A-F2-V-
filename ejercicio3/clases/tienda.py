from clases.venta import Venta


class Tienda:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: list[Venta] = []
        self.contador = 1

    def registrar_venta(self, monto: int, medio) -> None:
        if monto <= 0:
            raise ValueError("El monto debe ser mayor a cero.")

        medio.validar(monto)
        total = medio.calcular_total(monto)

        venta = Venta(self.contador, monto, medio, total)
        self.ventas.append(venta)
        self.contador += 1

    def total_recaudado(self) -> int:
        return sum(v.total for v in self.ventas)

    def total_recargos(self) -> int:
        return sum(v.total - v.monto for v in self.ventas)

    def comprobantes(self) -> list[str]:
        return [v.comprobante() for v in self.ventas]
