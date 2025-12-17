from clases.auto import Auto
from clases.moto import Moto
from clases.camion import Camion
from clases.estadia import Estadia


class Estacionamiento:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._abiertas: dict[str, Estadia] = {}
        self._cerradas: list[Estadia] = []

    def registrar_entrada(self, patente: str, tipo: str, entrada_min: int) -> None:
        patente = patente.strip().upper()
        if patente in self._abiertas:
            raise ValueError("Esa patente ya tiene una estadía abierta.")

        tipo = tipo.strip().lower()
        if tipo == "auto":
            vehiculo = Auto(patente)
        elif tipo == "moto":
            vehiculo = Moto(patente)
        elif tipo == "camion":
            vehiculo = Camion(patente)
        else:
            raise ValueError("Tipo inválido. Debe ser: auto, moto o camion.")

        self._abiertas[patente] = Estadia(vehiculo, entrada_min)

    def registrar_salida(self, patente: str, salida_min: int) -> int:
        patente = patente.strip().upper()
        if patente not in self._abiertas:
            raise ValueError("No existe una estadía abierta para esa patente.")

        estadia = self._abiertas.pop(patente)
        cobro = estadia.cerrar(salida_min)
        self._cerradas.append(estadia)
        return cobro

    def total_recaudado(self) -> int:
        return sum(e.cobro for e in self._cerradas)

    def cantidad_por_tipo(self) -> dict:
        conteo = {"Auto": 0, "Moto": 0, "Camión": 0}
        for e in self._cerradas:
            conteo[e.vehiculo.get_tipo()] += 1
        return conteo

    def top_3_cobros(self) -> list:
        return sorted(self._cerradas, key=lambda e: e.cobro, reverse=True)[:3]

    def listar_abiertas(self) -> list:
        return list(self._abiertas.values())

    def reporte(self) -> str:
        lineas = []
        lineas.append(f"=== Reporte Estacionamiento: {self.nombre} ===")
        lineas.append(f"Total recaudado: ${self.total_recaudado()}")

        lineas.append("\nCantidad de vehículos por tipo:")
        conteo = self.cantidad_por_tipo()
        for k, v in conteo.items():
            lineas.append(f"- {k}: {v}")

        lineas.append("\nTop 3 cobros más altos:")
        top = self.top_3_cobros()
        if not top:
            lineas.append("- (sin estadías cerradas)")
        else:
            for e in top:
                lineas.append(f"- {e.vehiculo.patente} ({e.vehiculo.get_tipo()}) -> ${e.cobro}")

        return "\n".join(lineas)
