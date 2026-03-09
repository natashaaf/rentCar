from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.Office import Office


class IOfficeService(ABC):
    """
    Interfaz que define las operaciones del servicio de oficinas.
    """
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Office]:
        """Busca una oficina por su ID."""
        pass
    
    @abstractmethod
    def add(self, office: Office) -> None:
        """Añade un nueva oficina."""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        """Elimina una oficina por su ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Office]:
        """Devuelve todas las oficinas."""
        pass
    
    @abstractmethod
    def update(self, office: Office) -> None:
        """Actualiza los datos de una oficina."""
        pass

