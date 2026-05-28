from enum import Enum
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


def continuar():
    print("Presione Enter para continuar...")
    input()