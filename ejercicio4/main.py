from clases.sistema_sensores import SistemaSensores
from clases.sensor_temperatura import SensorTemperatura
from clases.sensor_humedad import SensorHumedad
from clases.sensor_movimiento import SensorMovimiento


def menu():
    print("\n=== Ejercicio 4: Sensores y lecturas ===")
    print("1) Registrar sensor")
    print("2) Listar sensores")
    print("3) Generar lecturas (N rondas)")
    print("4) Ver reporte")
    print("5) Cargar demo (sensores + 5 rondas)")
    print("0) Salir")


def pedir_entero(mensaje: str) -> int:
    while True:
        dato = input(mensaje).strip()
        dato = dato.replace(" ", "")

        if dato.startswith("-") and dato[1:].isdigit():
            print("No se permiten números negativos.")
            continue

        if not dato.isdigit():
            print("Ingresa un número válido.")
            continue

        return int(dato)


def normalizar_tipo(opcion: str) -> str:
    opcion = opcion.strip().lower()

    if opcion in ("1", "temperatura", "temp"):
        return "temperatura"
    if opcion in ("2", "humedad", "hum"):
        return "humedad"
    if opcion in ("3", "movimiento", "mov"):
        return "movimiento"

    return ""


def mostrar_lectura(sensor, valor):
    if sensor.tipo() == "Movimiento":
        return "Movimiento detectado" if valor == 1 else "Sin movimiento"
    return f"{valor} {sensor.unidad_estandar()}"


def registrar_sensor_interactivo(sistema: SistemaSensores):
    print("\nTipo de sensor:")
    print("1) Temperatura")
    print("2) Humedad")
    print("3) Movimiento")

    op = input("Seleccione (número o texto): ").strip()
    tipo = normalizar_tipo(op)

    sensor_id = input("ID del sensor (ej: T-01): ").strip()
    nombre = input("Nombre (ej: Temp Bodega): ").strip()

    if not sensor_id or not nombre:
        print("ID y nombre no pueden quedar vacíos.")
        return

    try:
        if tipo == "temperatura":
            unidad = input("Unidad de lectura (C/F): ").strip().upper()
            if unidad not in ("C", "F"):
                print("Unidad inválida. Debe ser C o F.")
                return
            sistema.registrar_sensor(SensorTemperatura(sensor_id, nombre, unidad))

        elif tipo == "humedad":
            sistema.registrar_sensor(SensorHumedad(sensor_id, nombre))

        elif tipo == "movimiento":
            sistema.registrar_sensor(SensorMovimiento(sensor_id, nombre))

        else:
            print("Tipo de sensor no válido.")
            return

        print("Sensor registrado correctamente.")

    except Exception as e:
        print(f"Error: {e}")


def leer_rondas(sistema: SistemaSensores, rondas: int):
    if rondas <= 0:
        print("Las rondas deben ser mayor que 0.")
        return

    sensores = sistema.listar_sensores()
    if not sensores:
        print("No hay sensores registrados.")
        return

    print(f"\nGenerando lecturas ({rondas} rondas)...")
    for r in range(1, rondas + 1):
        print(f"\nRonda {r}:")
        resultados = sistema.leer_todos()

        for sensor, valor, error in resultados:
            if error:
                print(f"  {sensor.sensor_id} ({sensor.tipo()}) -> ERROR: {error}")
            else:
                print(f"  {sensor.sensor_id} ({sensor.tipo()}) -> {mostrar_lectura(sensor, valor)}")


def cargar_demo(sistema: SistemaSensores):
    demo = [
        SensorTemperatura("T-01", "Temp Bodega", "C"),
        SensorTemperatura("T-02", "Temp Oficina", "F"),
        SensorHumedad("H-01", "Humedad Bodega"),
        SensorMovimiento("M-01", "Movimiento Entrada"),
    ]

    # Registramos solo si no existen (sin borrar lo que el usuario ya registró)
    for s in demo:
        try:
            sistema.registrar_sensor(s)
        except Exception:
            pass

    print("Demo cargada (sin borrar sensores existentes). Leyendo 5 rondas...")
    leer_rondas(sistema, 5)
    print("\n" + sistema.generar_reporte())


def main():
    sistema = SistemaSensores("Sistema IoT")

    while True:
        menu()
        op = input("Opción: ").strip()

        if op == "1":
            registrar_sensor_interactivo(sistema)

        elif op == "2":
            sensores = sistema.listar_sensores()
            if not sensores:
                print("No hay sensores registrados.")
            else:
                print("\nSensores registrados:")
                for s in sensores:
                    print(f"- {s.sensor_id} | {s.tipo()} | {s.nombre}")

        elif op == "3":
            rondas = pedir_entero("Cantidad de rondas: ")
            leer_rondas(sistema, rondas)

        elif op == "4":
            print("\n" + sistema.generar_reporte())

        elif op == "5":
            cargar_demo(sistema)

        elif op == "0":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
