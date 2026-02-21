from abc import ABC, abstractmethod
from typing import List, Optional
from model.client import Client


class IClientRepository(ABC):
    """
    Interfaz que define las operaciones del repositorio de clientes.
    """
    
    @abstractmethod
    def find_by_dni(self, dni: str) -> Optional[Client]:
        """Busca un cliente por su DNI."""
        pass
    
    @abstractmethod
    def add(self, client: Client) -> None:
        """Añade un nuevo cliente al repositorio."""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        """Elimina un cliente por su ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Client]:
        """Devuelve todos los clientes."""
        pass
    
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Client]:
        """Busca un cliente por su ID."""
        pass
    
    @abstractmethod
    def update(self, client: Client) -> None:
        """Actualiza los datos de un cliente."""
        pass

