def simulador_cambio_usd_bob():
    tipo_cambio = 6.96  # Tipo de cambio fijo (USD a BOB) - Puedes actualizarlo

    print("Simulador de Tipo de Cambio USD a BOB")
    print("------------------------------------")

    while True:
        try:
            cantidad_usd = float(input("Ingrese la cantidad en dólares (USD) a convertir (o 'salir' para finalizar): "))
            if cantidad_usd < 0:
                print("Ingrese una cantidad válida (no negativa).")
                continue
            
            cantidad_bob = cantidad_usd * tipo_cambio
            print(f"{cantidad_usd:.2f} USD son equivalentes a {cantidad_bob:.2f} BOB")
        except ValueError:
            entrada = input("Entrada no válida. ¿Desea salir? (s/n): ")
            if entrada.lower() == 's':
                break
            else:
                print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break

if __name__ == "__main__":
    simulador_cambio_usd_bob()