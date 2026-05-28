from enum import Enum
import os
import datetime
import json

PATH = "Gestor-de-Tareas/tareas.json"

class estadoTarea(Enum):
    PENDIENTE = "Pendiente"
    EN_CURSO = "En Curso"
    TERMINADA = "Terminada"


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


def validarOpcion(min,max):
    while(True):
        try:
            opcion = int(input("-> "))
        except ValueError:
            print("Ingrese una opcion valida!")
        else:
            if(opcion < min or opcion > max):
                print("Ingrese una opcion valida!")
            else:
                return opcion


def validarEstado():
    estados = [est.value.strip().lower() for est in estadoTarea]
    estados.append("")
    while(True):
        estado = input("-> ")
        if(estado.strip().lower() not in estados):
            print("Ingrese un estado valido!")
        else:
            return estado.capitalize()
        
def validarFecha():
    while(True):
        fecha = input("-> ")
        if(not fecha.strip()):
            return fecha
        try:
            datetime.date.fromisoformat(fecha)
            return fecha
        except ValueError:
            print("Fecha no valida!")

def buscarTareaConId(contenido):
    while(True):
        id_tarea = input("-> ")
        if(not id_tarea.strip()):
            return None

        tarea = contenido["tareas"].get(id_tarea)
        if (tarea is None) or (tarea["eliminada"]):
            print("ID no existente!")
        else:
            return id_tarea


def limpiarPantalla():
    if(os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")


def continuar():
    print("Presione Enter para continuar...")
    input()