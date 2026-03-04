def mostrar_gastos(lista_gastos):
    if not lista_gastos:
        print("No hay gastos registrados.")
        return
    
    print("==Gastos Registrados==")
    for g in lista_gastos:
        print(f"Nombre: {g['nombre']} | Desc: {g['descripcion']} | Costo: ${g['costo']} ")