from typing import List, Optional
from src.model.Alquiler import Alquiler
from src.repository.alquiler_repository import AlquilerRepository
from src.repository.i_alquiler_repository import IAlquilerRepository
from src.service.i_alquiler_service import IAlquilerService


class AlquilerServiceImpl(IAlquilerService):
    """
    Implementación del servicio de alquileres.
    Actúa como intermediario entre el controlador y el repositorio.
    """
    
    def __init__(self):
        """Inicializa el servicio con el repositorio de alquileres."""
        self._repository: IAlquilerRepository = AlquilerRepository.get_alquiler_repository()
    
    def add(self, alquiler: Alquiler) -> None:
        """
        Añade un nuevo alquiler.
        
        Args:
            alquiler: El alquiler a añadir
        """
        self._repository.add(alquiler)
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un alquiler por su ID.
        
        Args:
            id: El ID del alquiler a eliminar
        """
        self._repository.delete_by_id(id)
    
    def find_all(self) -> List[Alquiler]:
        """
        Devuelve todos los alquileres.
        
        Returns:
            Lista de todos los alquileres
        """
        return self._repository.find_all()
    
    def find_by_id(self, id: int) -> Optional[Alquiler]:
        """
        Busca un alquiler por su ID.
        
        Args:
            id: El ID del alquiler a buscar
            
        Returns:
            El alquiler encontrado o None si no existe
        """
        return self._repository.find_by_id(id)
    
    def update(self, alquiler: Alquiler) -> None:
        """
        Actualiza los datos de un alquiler.
        
        Args:
            alquiler: El alquiler con los datos actualizados
        """
        self._repository.update(alquiler)

