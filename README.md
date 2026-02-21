# RentCar - Python Version

Plantilla inicial para la aplicación de alquiler de coches en Python.

## Descripción

Vamos a desarrollar una aplicación de Renting para una pequeña empresa.
Nos hemos reunido con el cliente y hemos recogido estos requisitos:

- Los clientes pueden alquilar los coches en la oficina física.
- Los clientes van a tener un id, dni, nombre y apellidos.
- Los coches van a tener una matrícula además de un modelo. A cada modelo se le aplicará un precio por día distinto.
- Los alquileres van a tener una fecha de inicio y una fecha de fin.
- Cada oficina tendrá una dirección y un cargo extra en caso de que la entrega no sea en la fecha indicada.

## Estructura del Proyecto

```
rent-car/
├── src/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada
│   ├── model/
│   │   ├── __init__.py
│   │   └── client.py           # Modelo Cliente
│   ├── controller/
│   │   ├── __init__.py
│   │   └── client_controller.py
│   ├── repository/
│   │   ├── __init__.py
│   │   ├── i_client_repository.py  # Interfaz del repositorio
│   │   └── client_repository.py    # Implementación (Singleton)
│   ├── service/
│   │   ├── __init__.py
│   │   ├── i_client_service.py     # Interfaz del servicio
│   │   └── client_service_impl.py  # Implementación
│   └── view/
│       ├── __init__.py
│       └── dialog.py           # Interfaz de consola
├── tests/
│   ├── __init__.py
│   └── test_client_repository.py
├── requirements.txt
└── README.md
```

## Arquitectura

El proyecto sigue una arquitectura en capas (MVC + Repository Pattern):

1. **Model**: Clases de dominio (Client)
2. **Repository**: Capa de acceso a datos con patrón Singleton
3. **Service**: Lógica de negocio
4. **Controller**: Intermediario entre la vista y el servicio
5. **View**: Interfaz de usuario por consola

## Requisitos

- Python 3.8 o superior

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd rent-car

# Crear entorno virtual (opcional pero recomendado)
python -m venv .venv
source .venv/bin/activate  # En macOS/Linux
# .venv\Scripts\activate  # En Windows

# Instalar dependencias
pip install -r requirements.txt
```

## Ejecución

```bash
python src/main.py
```

## Ejecutar Tests

```bash
# Ejecutar todos los tests
python -m pytest tests/ -v

# O usando unittest
python -m unittest discover tests -v
```

## ¿Qué debéis hacer?

Siguiendo con la arquitectura propuesta, desarrollar todas las funcionalidades obtenidas en los casos de uso.

Para ello, debéis:
1. Desarrollar las clases necesarias para cumplir con los casos de uso.
2. Refactorizar el código si es necesario.
3. Repetir los pasos anteriores hasta completar todas las funcionalidades.

### Clases pendientes de implementar:

- **Car** (Coche): matrícula, modelo
- **Model** (Modelo): nombre, precio por día
- **Office** (Oficina): dirección, cargo extra
- **Rent** (Alquiler): fecha inicio, fecha fin, cliente, coche, oficina

## Licencia

Este proyecto es para fines educativos.

