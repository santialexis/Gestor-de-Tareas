from enum import Enum
import os
import datetime
import json

PATH = "tareas.json"

def leerContenidoJson():
    try:
        with open(PATH,"r") as f:
            contenido = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contenido = {
            "ultimoID" : 0,
            "tareas" : {}
        }
    return contenido


def escribirJson(contenido):
    with open(PATH,"w") as f:
        json.dump(contenido,f,indent=4)


class estadoTarea(Enum):
    PENDIENTE = "pendiente"
    EN_CURSO = "en curso"
    TERMINADA = "terminada"


def validarEstado(estado):
    estados = [est.value for est in estadoTarea]
    estados.append("")
    
    if(estado.strip().lower() not in estados):
        return False
    else:
        return estado.capitalize()
        

def validarFecha(fecha):
    try:
        datetime.date.fromisoformat(fecha)
        return fecha
    except ValueError:
        print("Fecha no valida!")


def existeId(id):
    contenido = leerContenidoJson()
    tarea = contenido["tareas"].get(str(id))
    if (tarea is None) or (tarea["eliminada"]):
        return False
    return True


def limpiarPantalla():
    if(os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")