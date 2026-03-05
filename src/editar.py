def editarGasto(lista_gastos):
    if not lista_gastos:
        print("No hay gastos para editar.")
        return
    mostrar_gastos(lista_gastos)
    try:
        indice = int(input("Ingresa el número del gasto a editar (empezando desde 0): "))
        if 0 <= indice < len(lista_gastos):
            gasto = lista_gastos[indice]
            print("Editando gasto:", gasto)
            nuevo_nombre = input(f"Nuevo nombre ({gasto['nombre']}): ") or gasto['nombre']
            nueva_desc = input(f"Nueva descripción ({gasto['descripcion']}): ") or gasto['descripcion']
            try:
                nuevo_costo = input(f"Nuevo costo ({gasto['costo']}): ")
                nuevo_costo = float(nuevo_costo) if nuevo_costo else gasto['costo']
                gasto.update({
                    "nombre": nuevo_nombre,
                    "descripcion": nueva_desc,
                    "costo": nuevo_costo
                })
                print("Gasto actualizado exitosamente.")
            except ValueError:
                print("Error: el costo debe ser un número.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Error: debes ingresar un número válido.")
