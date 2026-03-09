from typing import List, Optional
from src.model.Client import Client
from src.service.client_service_impl import ClientServiceImpl
from src.service.i_client_service import IClientService


class ClientController:
    """
    Controlador para gestionar las operaciones de clientes.
    Recibe las peticiones de la vista y las delega al servicio.
    """
    
    def __init__(self):
        """Inicializa el controlador con el servicio de clientes."""
        self._service: IClientService = ClientServiceImpl()
    
    def add(self, dni: str, name: str, surname: str) -> None:
        """
        Añade un nuevo cliente.
        
        Args:
            dni: DNI del cliente
            name: Nombre del cliente
            surname: Apellidos del cliente
        """
        client = Client(dni, name, surname)
        
        self._service.add(client)
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un cliente por su ID.
        
        Args:
            id: El ID del cliente a eliminar
        """
        self._service.delete_by_id(id)
    
    def find_all(self) -> List[Client]:
        """
        Devuelve todos los clientes.
        
        Returns:
            Lista de todos los clientes
        """
        return self._service.find_all()
    
    def find_by_dni(self, dni: str) -> Optional[Client]:
        """
        Busca un cliente por su DNI.
        
        Args:
            dni: El DNI del cliente a buscar
            
        Returns:
            El cliente encontrado o None si no existe
        """
        return self._service.find_by_dni(dni)
    
    def update(self, id: int, dni: str, name: str, surname: str) -> None:
        """
        Actualiza los datos de un cliente.
        
        Args:
            id: El ID del cliente a actualizar
            dni: Nuevo DNI
            name: Nuevo nombre
            surname: Nuevos apellidos
        """
        client = Client(dni, name, surname, id)
        self._service.update(client)

