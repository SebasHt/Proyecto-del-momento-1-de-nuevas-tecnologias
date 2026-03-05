def eliminarGastos(listaGastos):
    if not listaGastos:
        print("no se an encontrado gastos para eliminar")
        return
    try:
        indice =int(input("ingre el numero del gasti que decea eliminar empezando desde el cero"))
        if 0 <= indice < len(listaGastos):
         eliminar = listaGastos.pop(indice)
         print(f"gasto '{eliminar['nombre']}' se elimino correctamente")
        else :
           print ("colocar bien el numero")
    except ValueError:
       print("error el numero era")
