from clases.email import Email
from clases.sms import SMS
from clases.push import Push
from clases.gestor_notificaciones import GestorNotificaciones


def mostrar_menu():
    print("\n=== Ejercicio 1: Notificaciones ===")
    print("1) Registrar destino")
    print("2) Listar destinos")
    print("3) Enviar mensaje a todos")
    print("4) Cargar ejemplo (destinos + 2 mensajes)")
    print("0) Salir")


def pedir_tipo_canal():
    # Valida que el tipo sea uno permitido
    while True:
        tipo = input("Tipo (email / sms / push): ").strip().lower()
        if tipo in ["email", "sms", "push"]:
            return tipo
        print("Tipo inválido. Debe ser: email, sms o push.")


def cargar_ejemplo(gestor: GestorNotificaciones):
    ejemplos = [
        Email("soporte@empresa.cl"),
        SMS("+56912345678"),
        Push("token_app_12345"),
    ]

    for canal in ejemplos:
        try:
            gestor.registrar(canal)
        except ValueError:
            pass

    print("Ejemplo cargado. Enviando 2 mensajes de prueba...")

    mensajes = [
        "Alerta 1: mantenimiento a las 22:00",
        "Alerta 2: actualización del sistema",
    ]

    for mensaje in mensajes:
        r = gestor.enviar_a_todos(mensaje)

        print(f"\nMensaje: {mensaje}")
        print("Detalle del envío:")
        for d in r["detalles"]:
            print(f"  {d}")

        print(
            f"Resumen -> Éxitos: {r['exitos']} | "
            f"Fallos: {r['fallos']} | "
            f"Costo: {r['costo_total']}"
        )


def main():
    gestor = GestorNotificaciones()

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                # Registrar destino
                tipo = pedir_tipo_canal()
                destino = input("Destino: ").strip()

                if tipo == "email":
                    gestor.registrar(Email(destino))
                elif tipo == "sms":
                    gestor.registrar(SMS(destino))
                else:
                    gestor.registrar(Push(destino))

                print("Destino registrado correctamente.")

            elif opcion == "2":
                # Listar destinos
                canales = gestor.listar()
                if not canales:
                    print("No hay destinos registrados.")
                else:
                    print("Destinos registrados:")
                    for c in canales:
                        print(f"- {c}")

            elif opcion == "3":
                # Enviar mensaje
                mensaje = input("Mensaje: ").strip()

                if not mensaje:
                    print("El mensaje no puede estar vacío.")
                    continue

                if not gestor.listar():
                    print("No hay destinos registrados. Primero registra al menos uno.")
                    continue

                r = gestor.enviar_a_todos(mensaje)

                print("\nDetalle del envío:")
                for d in r["detalles"]:
                    print(f"  {d}")

                print(
                    f"\nResumen -> Éxitos: {r['exitos']} | "
                    f"Fallos: {r['fallos']} | "
                    f"Costo: {r['costo_total']}"
                )

            elif opcion == "4":
                cargar_ejemplo(gestor)

            elif opcion == "0":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
