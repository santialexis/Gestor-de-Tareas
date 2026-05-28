import func
import validaciones as val

PATH = "Gestor-de-Tareas/tareas.json"

def crearTareaMenu():
    print("\nNombre de la tarea (solo Enter para cancelar):")
    nombre = input("-> ")
    if(not nombre.strip()):
        print("Cancelando...\n")
        return

    print("\nDescripcion (opcional):")
    desc = input("-> ")

    print('\nEstado (Pendiente por defecto, En curso, Terminada):')
    estado = val.validarEstado()

    contenido = val.leerContenidoJson()
    id_creado = func.crearTarea(contenido,nombre,desc,estado)

    print(f"\nTarea creada con exito! ID: {id_creado}")
    val.continuar()
    return 0


def modificarTareaMenu():
    contenido = val.leerContenidoJson()

    print("\nID (solo Enter para cancelar):")
    id_tarea = val.buscarTareaConId(contenido)
    if(id_tarea is None):
        print("Cancelando...\n")
        return

    print("\nCampos a modificar (solo Enter para no modificar)")
    nuevo_nombre = input("Nuevo nombre -> ")
    nueva_desc = input("Nueva descripcion -> ")
    print("Nuevo estado ",end="")
    nuevo_estado = val.validarEstado()

    se_modifico = func.modificarTarea(contenido,id_tarea,nuevo_nombre,nueva_desc,nuevo_estado)
    if(se_modifico):
        print(f"Tarea ID: {id_tarea} modificada!")
    else:
        print("La tarea no fue modificada...")
    val.continuar()
    return 0


def eliminarTareaMenu():
    contenido = val.leerContenidoJson()

    print("\nID (solo Enter para cancelar):")
    id_tarea = val.buscarTareaConId(contenido)
    if(id_tarea is None):
        print("Cancelando...\n")
        return
    
    func.eliminarTarea(contenido,id_tarea)
    print("Tarea eliminada!")
    val.continuar()
    return 0


def listarTareasMenu():
    contenido = val.leerContenidoJson()

    print("Indicar estado (opcional) -> ")
    estado = val.validarEstado()

    print("Indicar fecha de creacion (aaaa-mm-dd, opcional) -> ")
    fecha = val.validarFecha()

    func.listarTareas(contenido,estado,fecha)
    val.continuar()
    return 0