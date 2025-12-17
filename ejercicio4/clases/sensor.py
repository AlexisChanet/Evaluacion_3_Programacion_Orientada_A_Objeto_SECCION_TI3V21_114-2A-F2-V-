class Sensor:
    def __init__(self, sensor_id: str, nombre: str):
        # Datos básicos de cualquier sensor
        self.sensor_id = sensor_id
        self.nombre = nombre

        # Aquí guardamos las lecturas, pero ya en la unidad “estándar” del sistema
        self._lecturas_normalizadas = []

    def leer(self):
        # Cada sensor “lee” a su manera, por eso esto lo hacen las clases hijas
        raise NotImplementedError("Este método debe ser implementado por cada tipo de sensor.")

    def registrar_lectura(self, valor_normalizado):
        # Guardar una lectura ya normalizada
        self._lecturas_normalizadas.append(valor_normalizado)

    def obtener_lecturas(self):
        # Devolver las lecturas guardadas
        return list(self._lecturas_normalizadas)

    def tipo(self) -> str:
        # Nombre del tipo de sensor (lo cambian las clases hijas)
        return "Sensor"

    def unidad_estandar(self) -> str:
        # Unidad que usa el sistema para este sensor (lo cambian las clases hijas)
        return ""
