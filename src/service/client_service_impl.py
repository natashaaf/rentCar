from typing import List, Optional
from model.client import Client
from repository.client_repository import ClientRepository
from repository.i_client_repository import IClientRepository
from service.i_client_service import IClientService


class ClientServiceImpl(IClientService):
    """
    Implementación del servicio de clientes.
    Actúa como intermediario entre el controlador y el repositorio.
    """
    
    def __init__(self):
        """Inicializa el servicio con el repositorio de clientes."""
        self._repository: IClientRepository = ClientRepository.get_client_repository()
    
    def add(self, client: Client) -> None:
        """
        Añade un nuevo cliente.
        
        Args:
            client: El cliente a añadir
        """
        self._repository.add(client)
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un cliente por su ID.
        
        Args:
            id: El ID del cliente a eliminar
        """
        self._repository.delete_by_id(id)
    
    def find_all(self) -> List[Client]:
        """
        Devuelve todos los clientes.
        
        Returns:
            Lista de todos los clientes
        """
        return self._repository.find_all()
    
    def find_by_dni(self, dni: str) -> Optional[Client]:
        """
        Busca un cliente por su DNI.
        
        Args:
            dni: El DNI del cliente a buscar
            
        Returns:
            El cliente encontrado o None si no existe
        """
        return self._repository.find_by_dni(dni)
    
    def update(self, client: Client) -> None:
        """
        Actualiza los datos de un cliente.
        
        Args:
            client: El cliente con los datos actualizados
        """
        self._repository.update(client)

