# Django PostgreSQL Data Manager

## Descripción

Aplicación local realizada con Django que permite realizar operaciones CRUD en una base de datos PostgreSQL. La comunicación entre la aplicación y la base de datos se realiza mediante Psycopg2. 
La interfaz web está diseñada para facilitar la interacción del usuario con la base de datos, permitiendo gestionar al menos una tabla.

## Funcionalidades

- Crear (Insertar nuevos registros)
- Leer (Consultar todos los registros y un registro específico por su identificador)
- Actualizar (Modificar registros existentes)
- Eliminar (Borrar registros)

## Tecnologías Utilizadas

- **Django**: Framework web para el backend.
- **PostgreSQL**: Sistema de gestión de bases de datos.
- **Psycopg2**: Biblioteca para conectar y ejecutar consultas SQL en PostgreSQL desde Python.

## Requisitos

- Python 3.x
- PostgreSQL
- Django (`pip install django`)
- Psycopg2 (`pip install psycopg2`)
