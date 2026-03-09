from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.Coche import Coche

class ICocheService(ABC):
    """
    Interfaz que define las operaciones del servicio de coches.
    """
    
    @abstractmethod
    def find_by_matricula(self, matricula: str) -> Optional[Coche]:
        """Busca un coche por su matrícula."""
        pass
    
    @abstractmethod
    def add(self, coche: Coche) -> None:
        """Añade un nuevo coche."""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        """Elimina un coche por su ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Coche]:
        """Devuelve todos los coches."""
        pass
    
    @abstractmethod
    def update(self, coche: Coche) -> None:
        """Actualiza los datos de un coche."""
        pass

