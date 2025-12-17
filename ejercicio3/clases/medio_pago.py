class MedioPago:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def calcular_total(self, monto: int) -> int:
        # Cada medio define su propia lógica
        raise NotImplementedError

    def validar(self, monto: int) -> None:
        # Cada medio puede validar cosas distintas
        pass

    def __str__(self):
        return self.nombre
