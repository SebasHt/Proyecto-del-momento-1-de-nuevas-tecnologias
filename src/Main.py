import añadir_a_lista
import editar
import eliminar
import mostrar
import Promedio

print("Bien venido a Mila tu organizador de gastos")
print("")
seguir=True
gastos=[]

while seguir:
    print("¿Que quieres hacer ?")
    print("1) añadir gastos ")
    print("2) Ver gastos actuales ")
    print("3) Promedio de los gastos")
    print("4) eliminar o editar gasto")
    print("5) salir")
    opcion = int(input("cual opcion has decidido elegir "))
    

    match opcion:
        case 1:
            print("========================")
            añadir_a_lista.registrar(gastos)
            print("========================")
        case 2:
            print("========================")
            mostrar.mostrarGastos(gastos)
            print("========================")
        case 3:
            print("========================")
            Promedio.promedioGastos(gastos)
            print("========================")
        case 4:
            print("========================")
            opcion= int(input("1) para eliminar o 2) para editar "))
            if opcion == 1 :
                eliminar.eliminarGastos(gastos)
            else :
                editar.editarGasto(gastos)
            print("========================")
        case 5:
            seguir =False
            print("saliendo")