from clases.canal_notificacion import CanalNotificacion


class Push(CanalNotificacion):
    def get_tipo(self) -> str:
        return "Push"

    def enviar(self, mensaje: str) -> bool:
        # Para Push usamos un token. Simulamos que un token válido tiene mínimo 8 chars
        self.validar_mensaje(mensaje)
        return len(self.destino) >= 8

    def costo(self, mensaje: str) -> int:
        # Costo fijo bajo (solo para que el ejercicio tenga diferencias)
        self.validar_mensaje(mensaje)
        return 5
