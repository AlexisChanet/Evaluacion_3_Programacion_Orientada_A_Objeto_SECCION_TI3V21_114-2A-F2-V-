from clases.canal_notificacion import CanalNotificacion


class GestorNotificaciones:
    def __init__(self):
        # Aquí guardamos los destinos registrados (sin duplicados)
        self._canales: dict[str, CanalNotificacion] = {}

    def registrar(self, canal: CanalNotificacion) -> None:
        # Agrega un destino si no existe
        key = canal.clave_unica()
        if key in self._canales:
            raise ValueError("Destino duplicado: ya estaba registrado.")
        self._canales[key] = canal

    def listar(self) -> list[CanalNotificacion]:
        # Devuelve todos los destinos
        return list(self._canales.values())

    def enviar_a_todos(self, mensaje: str) -> dict:
        # Envía a todos y devuelve un resumen + detalle por canal
        exitos = 0
        fallos = 0
        costo_total = 0
        detalles = []

        for canal in self._canales.values():
            try:
                ok = canal.enviar(mensaje)

                if ok:
                    exitos += 1
                    costo = canal.costo(mensaje)
                    costo_total += costo
                    detalles.append(f"OK - {canal.get_tipo()} ({canal.destino}) | Costo: {costo}")
                else:
                    fallos += 1
                    detalles.append(f"FALLO - {canal.get_tipo()} ({canal.destino}) | Destino inválido")

            except Exception as e:
                fallos += 1
                detalles.append(f"FALLO - {canal.get_tipo()} ({canal.destino}) | {e}")

        return {"exitos": exitos, "fallos": fallos, "costo_total": costo_total, "detalles": detalles}
