import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=2)


def ver_tareas():
    print("-" * 16)
    print("Lista de tareas: ")
    if len(tareas) == 0:
        print("No hay tareas todavía.")
    else:
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    print("-" * 16)


def agg_tareas():
    print("-" * 16)
    nuevatarea = input("Que tarea quieres asignar: ")
    tareas.append(nuevatarea)
    guardar_tareas()
    print("Tarea agregada ✔")
    print("-" * 16)


def del_tareas():
    print("-" * 16)
    try:
        num = int(input("Número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            eliminada = tareas.pop(num - 1)
            guardar_tareas()
            print(f"Eliminada: {eliminada}")
        else:
            print("Ese número no existe.")
    except ValueError:
        print("Escribe solo el número de la tarea.")
    print("-" * 16)


tareas = cargar_tareas()
while True:
    print("\n")
    print("-" * 16)
    print("Menu de opciones")
    print("-" * 16)
    print("Ver tareas (1), agregar (2), quitar (3) o salir (4)")
    try:
        opc = int(input("Elije una opcion: "))
    except ValueError:
        print("Escribe un número del 1 al 4.")
        continue

    if opc == 1:
        ver_tareas()
    elif opc == 2:
        agg_tareas()
    elif opc == 3:
        del_tareas()
    elif opc == 4:
        print("¡Hasta luego!")
        break
