import añadir_a_lista
import editar

print("Bien venido a Mila tu organizador de gastos")
print("")
seguir=True
gastos=[]

while seguir:
    print("¿Que quieres hacer ?")
    print("1) añadir gastos ")
    print("2) Ver gastos actuales ")
    print("3) Promedio de los gastos")
    print("4) salir")
    opcion = int(input("cual opcion has decidido elegir "))
    

    match opcion:
        case 1:
            print("")
            añadir_a_lista.registrar(gastos)
        case 2:
            print("")
            editar.mostrar_gastos(gastos)
        case 3:
            print("")
        case 4:
            seguir =False
            print("saliendo")