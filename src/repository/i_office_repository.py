from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.Office import Office


class IOfficeRepository(ABC):
    """
    Interfaz que define las operaciones del repositorio de oficinas.
    """
    
    @abstractmethod
    def find_by_direccion(self, direccion: str) -> Optional[Office]:
        """Busca una oficina por su dirección."""
        pass
    
    @abstractmethod
    def add(self, office: Office) -> None:
        """Añade una nueva oficina al repositorio."""
        pass
    
    @abstractmethod
    def delete_by_direccion(self, direccion: str) -> None:
        """Elimina una oficina por su dirección."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Office]:
        """Devuelve todas las oficinas."""
        pass
    
    @abstractmethod
    def update(self, office: Office) -> None:
        """Actualiza los datos de una oficina."""
        pass

