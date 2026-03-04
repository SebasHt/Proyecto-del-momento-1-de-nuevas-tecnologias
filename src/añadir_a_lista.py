def registrar(listaGastos):
    print(" Nuevo Registro ")
    nombre = input("Nombre del gasto: ")
    desc = input("Descripcion breve: ")
    try:
        costo = float(input("Costo: "))
        gasto = {
            "nombre": nombre,
            "descripcion": desc,
            "costo": costo,
        }
        listaGastos.append(gasto)
        print("Gasto registrado exitosamente.")
    except ValueError:
        print("Error: El costo debe ser un numero.")
