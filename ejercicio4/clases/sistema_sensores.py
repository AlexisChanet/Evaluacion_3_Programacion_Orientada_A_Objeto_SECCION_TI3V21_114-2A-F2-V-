class SistemaSensores:
    def __init__(self, nombre: str):
        # Nombre del sistema (solo para mostrarlo en el reporte)
        self.nombre = nombre

        # Sensores guardados por id (para evitar duplicados)
        self._sensores = {}

    def registrar_sensor(self, sensor) -> None:
        # Agregar sensor y evitar ids repetidos
        if sensor.sensor_id in self._sensores:
            raise ValueError(f"Sensor duplicado: {sensor.sensor_id}")
        self._sensores[sensor.sensor_id] = sensor

    def listar_sensores(self):
        return list(self._sensores.values())

    def leer_todos(self):
        # Leer todos los sensores (si uno falla, no cae todo el programa)
        resultados = []
        for s in self._sensores.values():
            try:
                valor = s.leer()
                resultados.append((s, valor, None))
            except Exception as e:
                resultados.append((s, None, str(e)))
        return resultados

    def generar_reporte(self) -> str:
        # Reporte final con estadísticas
        lineas = []
        lineas.append(f"=== Reporte consolidado: {self.nombre} ===")

        if not self._sensores:
            lineas.append("No hay sensores registrados.")
            return "\n".join(lineas)

        for s in self._sensores.values():
            lecturas = s.obtener_lecturas()

            lineas.append(f"\n[{s.tipo()}] {s.sensor_id} - {s.nombre} (Unidad: {s.unidad_estandar()})")

            if not lecturas:
                lineas.append("  Sin lecturas registradas.")
                continue

            # Para movimiento (0/1) es mejor mostrar conteos
            if s.tipo() == "Movimiento":
                total = len(lecturas)
                movimientos = sum(lecturas)  # suma de 0/1 = cantidad de “1”
                sin_mov = total - movimientos
                porcentaje = round((movimientos / total) * 100, 2)

                lineas.append(f"  Lecturas: {total}")
                lineas.append(f"  Movimiento: {movimientos} | Sin movimiento: {sin_mov}")
                lineas.append(f"  % movimiento: {porcentaje}%")
            else:
                # Para temperatura y humedad: min, max y promedio
                minimo = min(lecturas)
                maximo = max(lecturas)
                promedio = round(sum(lecturas) / len(lecturas), 2)

                lineas.append(f"  Lecturas: {len(lecturas)}")
                lineas.append(f"  Mín: {minimo} | Máx: {maximo} | Prom: {promedio}")

        return "\n".join(lineas)
