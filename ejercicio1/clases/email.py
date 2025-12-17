from clases.canal_notificacion import CanalNotificacion


class Email(CanalNotificacion):
    def get_tipo(self) -> str:
        return "Email"

    def enviar(self, mensaje: str) -> bool:
        # Validación simple: que parezca un correo real
        self.validar_mensaje(mensaje)
        d = self.destino.lower()
        return ("@" in d) and ("." in d)

    def costo(self, mensaje: str) -> int:
        # Simulación de costo fijo por envío
        self.validar_mensaje(mensaje)
        return 10
