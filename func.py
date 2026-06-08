import json
import datetime
import validaciones as val

PATH = "tareas.json"

def crearTarea(nombre,estado,desc):
    contenido = val.leerContenidoJson()
    tarea_id = contenido["ultimoID"] + 1

    fechaCreacion = str(datetime.datetime.now().date())
    nuevaTarea = {
        "nombre" : nombre,
        "descripcion" : desc,
        "estado" : estado if estado else "Pendiente",
        "fecha_creacion" : fechaCreacion,
        "fecha_mod" : fechaCreacion,
        "eliminada" : False
    }

    contenido["tareas"][tarea_id] = nuevaTarea
    contenido["ultimoID"] = tarea_id

    val.escribirJson(contenido)
    return tarea_id


def modificarTarea(id, nuevo_nombre, nuevo_estado, nueva_desc):
    contenido = val.leerContenidoJson()
    se_modifico = False
    id = str(id)

    if(nuevo_nombre is not None):
        contenido["tareas"][id]["nombre"] = nuevo_nombre
        se_modifico = True
    
    if(nueva_desc is not None):
        contenido["tareas"][id]["descripcion"] = nueva_desc
        se_modifico = True
    
    if(nuevo_estado is not None):
        contenido["tareas"][id]["estado"] = nuevo_estado
        se_modifico = True

    if(se_modifico):
        contenido["tareas"][id]["fecha_mod"] = str(datetime.datetime.now().date())
    
    with open(PATH,"w") as f:
        json.dump(contenido,f,indent=4)

    return se_modifico


def eliminarTarea(id):
    contenido = val.leerContenidoJson()
    
    contenido["tareas"][str(id)]["eliminada"] = True
    with open(PATH,"w") as f:
        json.dump(contenido,f,indent=4)
    return True


def listarTareas(estado, fecha):
    contenido = val.leerContenidoJson()
    tareas = contenido["tareas"]
    estado = estado.strip().lower()

    res = {
        id_tarea: tarea for id_tarea,tarea in tareas.items()
        if(estado is None or tarea.get("estado").lower() == estado)
        and (fecha is None or tarea.get("fecha_creacion").lower() == fecha)
        and (not(tarea.get("eliminada")))
    }

    imprimirTareas(res)
    return 1


def imprimirTareas(tareas):
    print("\n===================================================================")
    for id_t,t in tareas.items():
        nombre = t.get("nombre")
        estado = t.get("estado")
        fecha_ini = t.get("fecha_creacion")
        fecha_mod = t.get("fecha_mod")
        desc = t.get("descripcion")
        print(f"ID: {id_t} // Nombre: {nombre} // Estado: {estado}")
        print(f"Fecha de creacion: {fecha_ini} // Ultima modificacion: {fecha_mod}")
        print(f"Descripcion: {desc}")
        print("===================================================================")