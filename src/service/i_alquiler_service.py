from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.Alquiler import Alquiler


class IAlquilerService(ABC):
    """
    Interfaz que define las operaciones del servicio de alquileres.
    """
    
    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Alquiler]:
        """Busca un alquiler por su ID."""
        pass
    
    @abstractmethod
    def add(self, alquiler: Alquiler) -> None:
        """Añade un nuevo alquiler."""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        """Elimina un alquiler por su ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Alquiler]:
        """Devuelve todos los alquileres."""
        pass
    
    @abstractmethod
    def update(self, alquiler: Alquiler) -> None:
        """Actualiza los datos de un alquiler."""
        pass

