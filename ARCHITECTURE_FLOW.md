# Flujo de la Arquitectura - RentCar

## Visión General

El proyecto sigue una arquitectura en capas (**MVC + Repository Pattern**). Cada capa tiene una responsabilidad concreta y solo se comunica con la capa inmediatamente inferior.

```
Usuario
  │
  ▼
View (Dialog)
  │
  ▼
Controller (ClientController)
  │
  ▼
Service (ClientServiceImpl)
  │
  ▼
Repository (ClientRepository)
  │
  ▼
Model (Client, Coche, Modelo, Alquiler, Office)
```

---

## Flujo Detallado por Capas

### 1. Punto de Entrada — `main.py`

```
main()
  └──> crea instancia de Dialog()
         └──> llama a dialog.get_started()
```

`main.py` únicamente instancia la vista y arranca el bucle de menú. No contiene lógica de negocio.

---

### 2. View — `dialog.py`

**Responsabilidad:** Mostrar menús, recoger input del usuario, mostrar resultados.

```
Dialog.__init__()
  └──> instancia ClientController()   ← única dependencia de la vista

get_started()   ← bucle principal del menú
  ├── opción 1 → _client_manager()
  ├── opción 2 → Coche_manager()      (pendiente)
  ├── opción 3 → Oficina_manager()    (pendiente)
  ├── opción 4 → Modelo_manager()     (pendiente)
  └── opción 5 → Alquiler_manager()   (pendiente)

_client_manager()   ← submenú de clientes
  ├── opción 1 (Crear)   → recoge dni, name, surname
  │                        └──> client_controller.add(dni, name, surname)
  ├── opción 2 (Eliminar) → recoge id
  │                        └──> client_controller.delete_by_id(id)
  ├── opción 3 (Actualizar) → recoge id, dni, name, surname
  │                        └──> client_controller.update(id, dni, name, surname)
  ├── opción 4 (Buscar)  → recoge dni
  │                        └──> client_controller.find_by_dni(dni)
  └── opción 5 (Listar)  → client_controller.find_all()
```

> La vista **no** conoce el Service ni el Repository. Solo habla con el Controller.

---

### 3. Controller — `client_controller.py`

**Responsabilidad:** Recibir peticiones de la vista, construir objetos de modelo y delegarlos al servicio.

```
ClientController.__init__()
  └──> instancia ClientServiceImpl()   ← tipado como IClientService

add(dni, name, surname)
  └──> crea Client(dni, name, surname)
       └──> service.add(client)

delete_by_id(id)
  └──> service.delete_by_id(id)

find_all()
  └──> service.find_all()

find_by_dni(dni)
  └──> service.find_by_dni(dni)

update(id, dni, name, surname)
  └──> crea Client(dni, name, surname)
       └──> service.update(id, client)
```

> El Controller **transforma** los datos primitivos de la vista en objetos de dominio antes de pasarlos al Service.

---

### 4. Service — `client_service_impl.py`

**Responsabilidad:** Contener la lógica de negocio (validaciones, reglas). Delega el acceso a datos al Repository.

```
ClientServiceImpl.__init__()
  └──> obtiene instancia de ClientRepository (Singleton)   ← tipado como IClientRepository

add(client: Client)
  ├── [validación de negocio si aplica]
  └──> repository.save(client)

delete_by_id(id: int)
  └──> repository.delete_by_id(id)

find_all() → List[Client]
  └──> repository.find_all()

find_by_dni(dni: str) → Optional[Client]
  └──> repository.find_by_dni(dni)

update(id: int, client: Client)
  └──> repository.update(id, client)
```

> El Service usa la **interfaz** `IClientRepository`, no la implementación concreta. Eso permite cambiar la fuente de datos sin tocar la lógica de negocio.

---

### 5. Repository — `client_repository.py`

**Responsabilidad:** Acceso y persistencia de datos. Implementa el patrón **Singleton** para garantizar una única instancia en memoria.

```
ClientRepository (Singleton)
  └──> _clients: List[Client] = []   ← almacenamiento en memoria
  └──> _id_counter: int = 1

save(client: Client)
  └──> asigna id autoincremental al cliente
       └──> añade a _clients

delete_by_id(id: int)
  └──> elimina el cliente con ese id de _clients

find_all() → List[Client]
  └──> devuelve copia de _clients

find_by_dni(dni: str) → Optional[Client]
  └──> busca en _clients por DNI

update(id: int, client: Client)
  └──> localiza el cliente por id y reemplaza sus datos
```

> Al ser **Singleton**, todos los controladores y servicios comparten el mismo repositorio durante la ejecución.

---

### 6. Model — `model/`

Clases de dominio puras. No contienen lógica de negocio ni acceso a datos.

| Clase     | Atributos principales                                      |
|-----------|------------------------------------------------------------|
| `Client`  | `id`, `dni`, `name`, `surname`                             |
| `Coche`   | `matricula`, `modelo` (referencia a `Modelo`)              |
| `Modelo`  | `nombre`, `precio_por_dia`                                 |
| `Office`  | `direccion`, `cargo_extra`                                 |
| `Alquiler`| `fecha_inicio`, `fecha_fin`, `cliente`, `coche`, `oficina` |

---

## Flujo Completo — Ejemplo: Crear un Cliente

```
Usuario escribe dni, name, surname en la consola
        │
        ▼
Dialog._client_manager()
  └──> client_controller.add(dni, name, surname)
              │
              ▼
       ClientController.add()
         └──> crea Client(dni, name, surname)
              └──> service.add(client)
                        │
                        ▼
               ClientServiceImpl.add()
                 └──> [validaciones]
                      └──> repository.save(client)
                                  │
                                  ▼
                         ClientRepository.save()
                           └──> asigna id
                                └──> _clients.append(client)
```

---

## Interfaces y Contratos

Las interfaces garantizan el desacoplamiento entre capas:

| Interfaz              | Implementación          | Usada por              |
|-----------------------|-------------------------|------------------------|
| `IClientService`      | `ClientServiceImpl`     | `ClientController`     |
| `IClientRepository`   | `ClientRepository`      | `ClientServiceImpl`    |

Cambiar la implementación de `IClientRepository` (p.ej. pasar de memoria a base de datos) **no requiere modificar** ni el Service ni el Controller.

---

## Regla de Dependencias

```
View  →  Controller  →  Service  →  Repository  →  Model
```

- Cada capa **solo conoce** la capa inmediatamente inferior.
- Las capas inferiores **nunca importan** capas superiores.
- Las dependencias siempre apuntan **hacia abajo**.
