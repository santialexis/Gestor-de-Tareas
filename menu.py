import json
import func
import validaciones as val

PATH = "Gestor-de-Tareas/tareas.json"

def crearTareaMenu():
    print("\nNombre de la tarea (solo Enter para cancelar):")
    nombre = input("-> ")
    if(not nombre.strip()):
        return

    print("\nDescripcion (opcional):")
    desc = input("-> ")

    print('\nEstado ("Pendiente" por defecto):')
    estado = val.validarEstado()

    contenido = val.leerContenidoJson()
    id_creado = func.crearTarea(contenido,nombre,desc,estado)

    print(f"\nTarea creada con exito! ID: {id_creado}")
    val.continuar()


def modificarTareaMenu():
    contenido = val.leerContenidoJson()

    print("\nID (solo Enter para cancelar):")
    while(True):
        id_tarea = input("-> ")
        if(not id_tarea.strip()):
            return

        tarea = contenido["tareas"].get(id_tarea)
        if (tarea is None) or (tarea["eliminada"]):
            print("ID no existente!")
        else:
            break

    print("\nCampos a modificar (solo Enter para no modificar)")
    nuevo_nombre = input("Nuevo nombre: ")
    nueva_desc = input("Nueva descripcion: ")
    print("Nuevo estado: ",end="")
    nuevo_estado = val.validarEstado()

    se_modifico = func.modificarTarea(contenido,id_tarea,nuevo_nombre,nueva_desc,nuevo_estado)
    if(se_modifico):
        print(f"Tarea ID: {id_tarea} modificada!")
    else:
        print("La tarea no fue modificada...")
    val.continuar()