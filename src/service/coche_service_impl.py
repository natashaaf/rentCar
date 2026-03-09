from typing import List, Optional
from src.model.Coche import Coche
from src.repository.coche_repository import CocheRepository
from src.repository.i_coche_repository import ICocheRepository
from src.service.i_coche_service import ICocheService
from src.service.modelo_service_impl import ModeloServiceImpl
from src.service.office_service_impl import OfficeServiceImpl

class CocheServiceImpl(ICocheService):
    """
    Implementación del servicio de coches.
    Actúa como intermediario entre el controlador y el repositorio.
    """
    
    def __init__(self):
        """Inicializa el servicio con el repositorio de coches."""
        self._repository = CocheRepository.get_coche_repository()
        self._modelo_service = ModeloServiceImpl()
        self._office_service = OfficeServiceImpl()
    
    def add(self, matricula, modelo, office):
        modelo = self._modelo_service.find_by_id(modelo)
        office = self._office_service.find_by_id(office)
        coche = Coche(matricula, modelo, office)
        self._repository.add(coche)
        """
        Añade un nuevo coche.
        
        Args:
            coche: El coche a añadir
        """
        self._repository.add(coche)
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un coche por su ID.
        
        Args:
            id: El ID del coche a eliminar
        """
        self._repository.delete_by_id(id)
    
    def find_all(self) -> List[Coche]:
        """
        Devuelve todos los coches.
        
        Returns:
            Lista de todos los coches
        """
        return self._repository.find_all()
    
    def find_by_matricula(self, matricula: str) -> Optional[Coche]:
        """
        Busca un coche por su matrícula.
        
        Args:
            matricula: La matrícula del coche a buscar
            
        Returns:
            El coche encontrado o None si no existe
        """
        return self._repository.find_by_matricula(matricula)
    
    def update(self, coche: Coche) -> None:
        """
        Actualiza los datos de un coche.
        
        Args:
            coche: El coche con los datos actualizados
        """
        self._repository.update(coche)

