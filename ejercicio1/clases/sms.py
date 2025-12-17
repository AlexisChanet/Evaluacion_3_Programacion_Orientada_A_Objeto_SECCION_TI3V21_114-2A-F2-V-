from clases.canal_notificacion import CanalNotificacion


class SMS(CanalNotificacion):
    def get_tipo(self) -> str:
        return "SMS"

    def validar_mensaje(self, mensaje: str) -> None:
        # SMS tiene una regla extra: máximo 160 caracteres
        super().validar_mensaje(mensaje)
        if len(mensaje) > 160:
            raise ValueError("SMS: el mensaje no puede superar 160 caracteres.")

    def enviar(self, mensaje: str) -> bool:
        # Validación simple: que el destino parezca un número
        self.validar_mensaje(mensaje)
        d = self.destino.replace("+", "")
        return d.isdigit() and len(d) >= 9

    def costo(self, mensaje: str) -> int:
        # Costo por tramos: mientras más largo el mensaje, más caro
        self.validar_mensaje(mensaje)
        tramos = (len(mensaje) + 49) // 50
        return 15 * tramos
