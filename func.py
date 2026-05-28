import json
import datetime

PATH = "Gestor-de-Tareas/tareas.json"

def crearTarea(contenido,nombre,desc,estado):
    tarea_id = contenido["ultimoID"] + 1
    fechaCreacion = str(datetime.datetime.now().date())
    nuevaTarea = {
        "nombre" : nombre,
        "descripcion" : desc,
        "estado" : estado if estado.strip() else "Pendiente",
        "fecha_creacion" : fechaCreacion,
        "fecha_mod" : fechaCreacion,
        "eliminada" : False
    }

    contenido["tareas"][tarea_id] = nuevaTarea
    contenido["ultimoID"] = tarea_id

    with open(PATH,"w") as f:
        json.dump(contenido,f,indent=4)
    
    return tarea_id


def modificarTarea(contenido, id_tarea, nuevo_nombre, nueva_desc, nuevo_estado):
    se_modifico = False

    if(nuevo_nombre.strip()):
        contenido["tareas"][id_tarea]["nombre"] = nuevo_nombre
        se_modifico = True
    
    if(nueva_desc.strip()):
        contenido["tareas"][id_tarea]["descripcion"] = nueva_desc
        se_modifico = True
    
    if(nuevo_estado.strip()):
        contenido["tareas"][id_tarea]["estado"] = nuevo_estado
        se_modifico = True

    if(se_modifico):
        contenido["tareas"][id_tarea]["fecha_mod"] = str(datetime.datetime.now().date())
    
    with open(PATH,"w") as f:
        json.dump(contenido,f,indent=4)

    return se_modifico