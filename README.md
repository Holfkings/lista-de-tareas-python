# 📝 Lista de Tareas en Python

Aplicación de consola para gestionar una lista de tareas: permite ver, agregar y eliminar tareas mediante un menú interactivo. Las tareas se **guardan en un archivo** (`tareas.json`), así no se pierden al cerrar el programa.

## 🚀 ¿Qué hace?

- **Ver tareas**: muestra todas las tareas guardadas (numeradas) o avisa si la lista está vacía.
- **Agregar tareas**: añade una nueva tarea y la guarda en disco.
- **Eliminar tareas**: quita una tarea por su número, validando que exista.
- **Persistencia**: las tareas se guardan en `tareas.json` y se cargan al iniciar.
- **Salir**: cierra el programa.

## 🛠️ Tecnologías

- Python 3
- Módulos estándar: `json`, `os`

## ▶️ Cómo ejecutarlo

1. Clona este repositorio o descarga `Tareas.py`
2. Abre una terminal en la carpeta del proyecto
3. Ejecuta:

```bash
python Tareas.py
```

4. Sigue las instrucciones del menú (elige una opción del 1 al 4)

## 📸 Ejemplo de uso

```text
----------------
Menu de opciones
----------------
Ver tareas (1), agregar (2), quitar (3) o salir (4)
Elije una opcion: 2
----------------
Que tarea quieres asignar: Estudiar Python
Tarea agregada ✔
----------------
```

## 📚 Lo que aprendí con este proyecto

- Manejo de **listas** en Python (`append`, `pop`, `len`)
- **Bucles** `while` y **condicionales** `if / elif / else`
- **Funciones** para organizar el código
- **Persistencia** con `json` y `os` (guardar/cargar datos)
- **Validación** de entradas con `try / except`

## 🔜 Mejoras futuras

- [ ] Marcar tareas como completadas
- [ ] Editar una tarea existente
- [ ] Interfaz gráfica (Tkinter)

---

✍️ Hecho por **Holfkings Arenas** como parte de mi aprendizaje en Python.
