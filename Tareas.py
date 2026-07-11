def ver_tareas():
    print("-"*16)
    print("Lista de tareas: ")
    if len(tareas) == 0:
        print("No hay tareas todavía.")
    for tarea in tareas:
        print(tarea)
    print("-"*16)     
def agg_tareas():
    print("-"*16)
    nuevatarea=input("Que tarea quieres asignar: ")
    tareas.append(nuevatarea)
    print("-"*16)       
def del_tareas():
    print("-"*16)
    fulltarea=input("Que tarea quieres eliminar: ")
    if fulltarea in tareas:
        tareas.remove(fulltarea)
    else:
        print("-"*16)
        print("No existe tu tarea, sé específico con los caracteres.")
    print("-"*16)        


tareas=[]
while True:
    print("\n")
    print("-"*16)
    print("Menu de opciones")
    print("-"*16)
    print("Quieres ver tareas (1), agregar(2), quitar tareas(3) o salir (4)")
    opc=int(input("Elije una opcion: "))
    if opc==1:
        ver_tareas()
    elif opc==2:
        agg_tareas()
    elif opc==3:
        del_tareas()
    elif opc==4:
        break
    
