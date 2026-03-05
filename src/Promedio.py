def promedioGastos(lista_gastos):
    if not lista_gastos:
        print("no se a encobtradi fastos")
        return
    total = sum(g["costo"] for g in lista_gastos)
    promedio = total / len(lista_gastos)
    print(f"El promedio de los gastos es: ${promedio:.2f}")