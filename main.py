import menu
import validaciones as val

opcion = -1
while(opcion != 0):
    print("= = Gestor de Tareas = =")
    print("1 - Crear nueva tarea")
    print("2 - Modificar tarea")
    print("3 - Eliminar tarea")
    print("4 - Listar tareas")
    print("0 - Salir")

    opcion = val.validarOpcion(0,4)
    
    match opcion:
        case 1:
            menu.crearTareaMenu()
        case 2:
            menu.modificarTareaMenu()
        case 0:
            print("Saliendo...")