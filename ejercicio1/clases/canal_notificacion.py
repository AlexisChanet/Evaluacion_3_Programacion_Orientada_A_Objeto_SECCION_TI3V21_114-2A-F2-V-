class CanalNotificacion:
    def __init__(self, destino: str):
        # Clase base: representa un canal genérico (Email, SMS, Push)
        destino = (destino or "").strip()
        if not destino:
            raise ValueError("El destino no puede estar vacío.")
        self.destino = destino

    def get_tipo(self) -> str:
        # Las clases hijas sobreescriben esto
        return "Canal"

    def clave_unica(self) -> str:
        # Se usa para no repetir el mismo destino en el mismo canal
        return f"{self.get_tipo()}:{self.destino}".lower()

    def validar_mensaje(self, mensaje: str) -> None:
        # Validación general para cualquier canal
        if not (mensaje or "").strip():
            raise ValueError("El mensaje no puede estar vacío.")

    def costo(self, mensaje: str) -> int:
        # Costo base (las hijas lo cambian)
        self.validar_mensaje(mensaje)
        return 0

    def enviar(self, mensaje: str) -> bool:
        # En una app real acá se llamaría a un servicio externo.
        # Aquí solo simulamos un envío correcto.
        self.validar_mensaje(mensaje)
        return True

    def __str__(self) -> str:
        # Cómo se muestra cuando lo imprimimos
        return f"{self.get_tipo()} -> {self.destino}"
