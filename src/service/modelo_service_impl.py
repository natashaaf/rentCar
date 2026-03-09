from typing import List, Optional
from src.model.Modelo import Modelo
from src.repository.i_modelo_repository import IModeloRepository
from src.repository.modelo_repository import ModeloRepository
from src.service.i_modelo_service import IModeloService


class ModeloServiceImpl(IModeloService):
    """
    Implementación del servicio de modelos.
    Actúa como intermediario entre el controlador y el repositorio.
    """
    
    def __init__(self):
        """Inicializa el servicio con el repositorio de modelos."""
        self._repository: IModeloRepository = ModeloRepository.get_modelo_repository()
    
    def add(self, modelo: Modelo) -> None:
        """
        Añade un nuevo modelo.
        
        Args:
            modelo: El modelo a añadir
        """
        self._repository.add(modelo)
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un modelo por su ID.
        
        Args:
            id: El ID del modelo a eliminar
        """
        self._repository.delete_by_id(id)
    
    def find_all(self) -> List[Modelo]:
        """
        Devuelve todos los modelos.
        
        Returns:
            Lista de todos los modelos
        """
        return self._repository.find_all()
    
    def find_by_id(self, id: int) -> Optional[Modelo]:
        """
        Busca un modelo por su ID.
        
        Args:
            id: El ID del modelo a buscar
            
        Returns:
            El modelo encontrado o None si no existe
        """
        return self._repository.find_by_id(id)
    
    def update(self, modelo: Modelo) -> None:
        """
        Actualiza los datos de un modelo.
        
        Args:
            modelo: El modelo con los datos actualizados
        """
        self._repository.update(modelo)

