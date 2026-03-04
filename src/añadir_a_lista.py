def registrar(listaGasto):
    print(" Nuevo Registro ")
    nombre = input("Nombre del gasto: ")
    desc = input("Descripcion breve: ")
    try:
        costo = float(input("Costo: "))
        
        # Almacenamos el gasto como un diccionario
        listaGasto = {
            "nombre": nombre,
            "descripcion": desc,
            "costo": costo,
            "fecha": fecha
        }
        lista_gastos.append(listaGasto)
        print("Gasto registrado exitosamente.")
    except ValueError:
        print("Error: El costo debe ser un numero.")