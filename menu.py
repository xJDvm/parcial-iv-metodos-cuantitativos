import os

def mostrar_menu():
    print("Seleccione el archivo que desea ejecutar:")
    print("1. RAMIFICACIONACOTACION.PY")
    print("2. BINARIA.PY")
    print("3. ENTERAMIXTA.PY")
    print("4. ENTERAPURA.PY")
    print("5. PLANOSCORTES.PY")
    print("6. MOCHILA.PY")
    print("0. Salir")

def ejecutar_archivo(opcion):
    archivos = {
        '1': 'RAMIFICACIONACOTACION.PY',
        '2': 'BINARIA.PY',
        '3': 'ENTERAMIXTA.PY',
        '4': 'ENTERAPURA.PY',
        '5': 'PLANOSCORTES.PY',
        '6': 'MOCHILA.PY'
    }
    archivo = archivos.get(opcion)
    if archivo:
        os.system(f'python {archivo}')
    else:
        print("Opción no válida. Intente de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción: ")
        if opcion == '0':
            break
        ejecutar_archivo(opcion)

if __name__ == "__main__":
    main()