cargos = ["CEO", "Desarrollador", "Analista de datos"]
import os


trabajadores = []

def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").upper()
    while cargo not in cargos:
        print("Cargo no válido. Los cargos válidos son:", cargos)
        cargo = input("Ingrese el cargo del trabajador (CEO/Desarrollador/Analista de datos): ").upper()
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    liquido_pagar = sueldo_bruto - desc_salud - desc_afp
    trabajador = {"Nombre": nombre, "Apellido": apellido, "Cargo": cargo, "Sueldo Bruto": sueldo_bruto, "Desc. Salud": desc_salud, "Desc. AFP": desc_afp, "Líquido a pagar": liquido_pagar}
    trabajadores.append(trabajador)
    print("Trabajador registrado con éxito.\n")


def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.\n")
    else:
        for trabajador in trabajadores:
            print("Nombre:", trabajador["Nombre"], trabajador["Apellido"])
            print("Cargo:", trabajador["Cargo"])
            print("Sueldo Bruto:", trabajador["Sueldo Bruto"])
            print("Desc. Salud:", trabajador["Desc. Salud"])
            print("Desc. AFP:", trabajador["Desc. AFP"])
            print("Líquido a pagar:", trabajador["Líquido a pagar"])
            print()


def imprimir_planilla(cargo=None):
    if not trabajadores:
        print("No hay trabajadores registrados.\n")
        return
    if cargo:
        trabajadores_filtrados = [trabajador for trabajador in trabajadores if trabajador["Cargo"] == cargo]
        if not trabajadores_filtrados:
            print("No hay trabajadores con el cargo especificado.\n")
            return
        file_name = f"planilla_{cargo}.txt"
        with open(file_name, "w") as file:
            for trabajador in trabajadores_filtrados:
                file.write(f"Nombre: {trabajador['Nombre']} {trabajador['Apellido']}\n")
                file.write(f"Cargo: {trabajador['Cargo']}\n")
                file.write(f"Sueldo Bruto: {trabajador['Sueldo Bruto']}\n")
                file.write(f"Desc. Salud: {trabajador['Desc. Salud']}\n")
                file.write(f"Desc. AFP: {trabajador['Desc. AFP']}\n")
                file.write(f"Líquido a pagar: {trabajador['Líquido a pagar']}\n\n")
        print(f"Planilla de sueldos para el cargo {cargo} generada con éxito en {file_name}\n")
    else:
        file_name = "planilla_todos.txt"
        with open(file_name, "w") as file:
            for trabajador in trabajadores:
                file.write(f"Nombre: {trabajador['Nombre']} {trabajador['Apellido']}\n")
                file.write(f"Cargo: {trabajador['Cargo']}\n")
                file.write(f"Sueldo Bruto: {trabajador['Sueldo Bruto']}\n")
                file.write(f"Desc. Salud: {trabajador['Desc. Salud']}\n")
                file.write(f"Desc. AFP: {trabajador['Desc. AFP']}\n")
                file.write(f"Líquido a pagar: {trabajador['Líquido a pagar']}\n\n")
        print(f"Planilla de sueldos generada con éxito en {file_name}\n")


def main():
    while True:
        print("Seleccione una opción:")
        print("1. Registrar trabajador")
        print("2. Listar todos los trabajadores")
        print("3. Imprimir planilla de sueldos")
        print("4. Salir del programa")
        opcion = input("Opción: ")

        if opcion == "1":
            registrar_trabajador()
        elif opcion == "2":
            listar_trabajadores()
        elif opcion == "3":
            cargo = input("Ingrese el cargo para el que desea imprimir la planilla (deje en blanco para imprimir todos): ").upper()
            imprimir_planilla(cargo)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()