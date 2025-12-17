from clases.estacionamiento import Estacionamiento


def hhmm_a_minutos(hhmm: str) -> int:
    hhmm = hhmm.strip()
    if ":" not in hhmm:
        raise ValueError("Formato inválido. Usa HH:MM (ej: 08:30).")

    h, m = hhmm.split(":")
    h = int(h)
    m = int(m)

    if h < 0 or h > 23 or m < 0 or m > 59:
        raise ValueError("Hora fuera de rango.")

    return h * 60 + m


def mostrar_menu():
    print("\n=== Ejercicio 2: Tarificador Estacionamiento ===")
    print("1) Registrar entrada")
    print("2) Registrar salida")
    print("3) Ver estadías abiertas")
    print("4) Ver reporte final")
    print("5) Cargar prueba (12 estadías)")
    print("0) Salir")


def cargar_prueba(est: Estacionamiento):
    # 12 estadías (mezcla de tipos y horarios)
    datos = [
        ("AA1111", "auto", "07:10", "08:05"),
        ("BB2222", "moto", "09:30", "10:10"),
        ("CC3333", "camion", "18:15", "20:00"),
        ("DD4444", "auto", "12:00", "12:40"),
        ("EE5555", "moto", "19:10", "19:55"),
        ("FF6666", "camion", "06:30", "07:20"),
        ("GG7777", "auto", "17:50", "18:10"),
        ("HH8888", "moto", "08:00", "09:00"),
        ("II9999", "auto", "20:10", "21:05"),
        ("JJ0000", "camion", "10:00", "11:35"),
        ("KK1212", "moto", "14:05", "15:00"),
        ("LL3434", "auto", "18:40", "19:20"),
    ]

    for patente, tipo, ent, sal in datos:
        est.registrar_entrada(patente, tipo, hhmm_a_minutos(ent))
        est.registrar_salida(patente, hhmm_a_minutos(sal))

    print("Prueba cargada: 12 estadías registradas y cerradas.")


def main():
    est = Estacionamiento("Parking Demo")

    while True:
        mostrar_menu()
        op = input("Opción: ").strip()

        try:
            if op == "1":
                patente = input("Patente: ").strip().upper()
                tipo = input("Tipo (auto/moto/camion): ").strip().lower()
                entrada = input("Hora entrada (HH:MM): ").strip()

                est.registrar_entrada(patente, tipo, hhmm_a_minutos(entrada))
                print("Entrada registrada.")

            elif op == "2":
                patente = input("Patente: ").strip().upper()
                salida = input("Hora salida (HH:MM): ").strip()

                cobro = est.registrar_salida(patente, hhmm_a_minutos(salida))
                print(f"Salida registrada. Cobro: ${cobro}")

            elif op == "3":
                abiertas = est.listar_abiertas()
                if not abiertas:
                    print("No hay estadías abiertas.")
                else:
                    print("Estadías abiertas:")
                    for e in abiertas:
                        print(f"- {e.vehiculo.patente} ({e.vehiculo.get_tipo()})")

            elif op == "4":
                print(est.reporte())

            elif op == "5":
                cargar_prueba(est)

            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("Opción no válida.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
    