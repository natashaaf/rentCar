from abc import ABC, abstractmethod
from typing import List, Optional
from src.model.Modelo import Modelo


class IModeloService(ABC):
    """
    Interfaz que define las operaciones del servicio de modelos.
    """
    
    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Modelo]:
        """Busca un modelo por su ID."""
        pass
    
    @abstractmethod
    def add(self, modelo: Modelo) -> None:
        """Añade un nuevo modelo."""
        pass
    
    @abstractmethod
    def delete_by_id(self, id: int) -> None:
        """Elimina un modelo por su ID."""
        pass
    
    @abstractmethod
    def find_all(self) -> List[Modelo]:
        """Devuelve todos los modelos."""
        pass
    
    @abstractmethod
    def update(self, modelo: Modelo) -> None:
        """Actualiza los datos de un modelo."""
        pass

