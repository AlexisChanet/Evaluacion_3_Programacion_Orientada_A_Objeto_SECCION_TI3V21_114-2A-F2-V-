from clases.tienda import Tienda
from clases.tarjeta import Tarjeta
from clases.transferencia import Transferencia
from clases.billetera import Billetera


def mostrar_menu():
    print("\n=== Ejercicio 3: Pagos en tienda ===")
    print("1) Registrar venta")
    print("2) Ver reporte")
    print("0) Salir")


def leer_monto(mensaje: str) -> int:
    # Permite ingresar montos como: 50000, 50.000, 50 000
    texto = input(mensaje).strip()
    texto = texto.replace(".", "").replace(" ", "")

    if texto == "" or not texto.isdigit():
        raise ValueError("Debes ingresar un monto válido (ej: 50000 o 50.000).")

    monto = int(texto)

    if monto <= 0:
        raise ValueError("El monto debe ser mayor a cero.")

    # Límite simple para evitar montos absurdos (anti 'romper programa')
    if monto > 50_000_000:
        raise ValueError("El monto es demasiado alto para este sistema (máx: 50.000.000).")

    return monto


def main():
    tienda = Tienda("Tienda Demo")

    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()

        try:
            if opcion == "1":
                monto = leer_monto("Monto de la venta: ")

                print("\nMedio de pago:")
                print("1) Tarjeta")
                print("2) Transferencia")
                print("3) Billetera digital")
                medio_op = input("Seleccione: ").strip()

                if medio_op == "1":
                    cupo = leer_monto("Cupo disponible de la tarjeta: ")
                    medio = Tarjeta(cupo)

                elif medio_op == "2":
                    medio = Transferencia()

                elif medio_op == "3":
                    saldo = leer_monto("Saldo disponible en billetera: ")
                    medio = Billetera(saldo)

                else:
                    print("Medio no válido. Intenta nuevamente.")
                    continue

                tienda.registrar_venta(monto, medio)

                # Mostrar el comprobante de la última venta (se entiende mejor)
                ultima = tienda.ventas[-1]
                print("\nVenta registrada correctamente.")
                print("Comprobante:")
                print(ultima.comprobante())

            elif opcion == "2":
                print("\n=== Reporte final ===")
                print(f"Total recaudado: ${tienda.total_recaudado()}")
                print(f"Total recargos: ${tienda.total_recargos()}")

                print("\nComprobantes:")
                comprobantes = tienda.comprobantes()
                if not comprobantes:
                    print("- (No hay ventas registradas)")
                else:
                    for c in comprobantes:
                        print("-", c)

            elif opcion == "0":
                print("Saliendo...")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
