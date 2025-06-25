def comprar_entrada(compradores):
    while True:
        nombre = input("Ingrese el nombre del comprador: ")
        if not nombre:
            print("El nombre del comprador no puede estar vacío.")
            continue
        if nombre in compradores:
            print("El nombre del comprador ya existe. Por favor, use un nombre diferente.")
            continue
        break

    while True:
        tipo_entrada = input("Ingrese el tipo de entrada (G para General, V para VIP): ")
        if tipo_entrada not in ["G", "V"]:
            print("Tipo de entrada inválido. Por favor, ingrese 'G' o 'V'.")
            continue
        break

    while True:
        codigo_confirmacion = input("Ingrese el código de confirmación (mínimo 6 caracteres, al menos 1 mayúscula, 1 número, sin espacios): ")
        if len(codigo_confirmacion) < 6:
            print("El código de confirmación debe tener al menos 6 caracteres.")
            continue
        if not any(char.isupper() for char in codigo_confirmacion):
            print("El código de confirmación debe contener al menos una letra mayúscula.")
            continue
        if not any(char.isdigit() for char in codigo_confirmacion):
            print("El código de confirmación debe contener al menos un número.")
            continue
        if " " in codigo_confirmacion:
            print("El código de confirmación no puede contener espacios en blanco.")
            continue
        break
    compradores[nombre] = {"tipo_entrada": tipo_entrada, "codigo_confirmacion": codigo_confirmacion}
    print("¡Entrada registrada exitosamente!")

def consultar_comprador(compradores):
    nombre = input("Ingrese el nombre del comprador a consultar: ")
    if nombre in compradores:
        datos = compradores[nombre]
        print(f"\nDatos del comprador '{nombre}':")
        print(f"  Tipo de Entrada: {datos["tipo_entrada"]}")
        print(f"  Código de Confirmación: {datos["codigo_confirmacion"]}")
    else:
        print("El comprador no se encuentra.")


def cancelar_compra(compradores):
    nombre = input("Ingrese el nombre del comprador cuya compra desea cancelar: ")
    if nombre in compradores:
        del compradores[nombre]
        print(f"La compra para '{nombre}' ha sido cancelada exitosamente.")
    else:
        print("El comprador no se encuentra, no se puede cancelar la compra.")

def main():
    compradores = {}

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            comprar_entrada(compradores)
        elif opcion == "2":
            consultar_comprador(compradores)
        elif opcion == "3":
            cancelar_compra(compradores)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    main()
