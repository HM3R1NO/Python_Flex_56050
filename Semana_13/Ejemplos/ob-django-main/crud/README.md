# Gestor personal
Hará las siguientes funciones:
* Acciones CRUD con contactos
* Buscar contactos en la agenda
* Registrar tareas

## Partes
1. Rutas
   1. Inicio
   2. Tareas
      1. Crear
      2. Listar
      3. Actualizar
      4. Borrar
   3. Contactos
      1. Tareas
      2. Crear
      3. Listar
      4. Actualizar
      5. Borrar
2. Plantillas
   1. Base (index)
      1. Nav
      2. Cuerpo
      3. Footer
   2. Crear
   3. Listar
   4. Actualizar
   5. Borrar
3. Modelos
   1. Tarea
   2. Contacto
4. Vistas
   1. Tareas
      1. Crear
      2. Listar
      3. Actualizar
      4. Borrar
   2. Contactos
      1. Tareas
      2. Crear
      3. Listar
      4. Actualizar
      5. Borrar
5. Formularios
   1. Crear
   2. Actualizar


## Pasos
1. Creo Base de datos en PostgreSQL y la conecto con el proyecto en settings.py.
2. Migro las tablas
```python manage.py migrate```
3. También en settings.py añado 'templates' a TEMPLATES > DIRS, donde albergaremos todas las plantillas.
4. Creo el directorio templates
5. Creo las aplicaciones contactos y tareas con ```python manage.py startapp [nombre]```
6. Añado las aplicaciones a la lista de aplicaciones instaladas en settings.py
7. Verifico que se han instalado correctamente con ```python manage.py check [nombre]```
8. Creo la carpeta static para guardar todos los archivos estáticos.
9. Añado la ruta a settings.py: 
```STATIC_DIRS = [
        BASE_DIR / "static",
        '/var/www/static'
    ]
```
10. Incluyo las urls de las aplicaciones al urls.py del proyecto
11. Añado una ruta '' para el index.html (la página principal del crud)
12. Creo urls.py en las aplicaciones
13. Diseño el html general del proyecto
14. Defino la vista de index.html
15. Empezaremos trabajando en los contactos:
    1.  Defino las rutas
    2.  Creo los modelos
    3.  Defino las vistas
    4.  Creo el formulario para crear y actualizar contactos
        1.  Creo forms.py
        2.  Defino el formulario
    5. Sigo creando las vistas
 16. Continúo con las tareas
     1.  Defino las rutas
     2.  Defino el modelo
     3.  Creo el formulario
     4.  Defino las vistas
     5.  Creo los html
  


