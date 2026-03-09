from typing import List, Optional
from src.model.Office import Office
from src.repository.i_office_repository import IOfficeRepository
from src.repository.office_repository import OfficeRepository
from src.service.i_office_service import IOfficeService


class OfficeServiceImpl(IOfficeService):
    """
    Implementación del servicio de oficinas.
    Actúa como intermediario entre el controlador y el repositorio.
    """
    
    def __init__(self):
        """Inicializa el servicio con el repositorio de oficinas."""
        self._repository: IOfficeRepository = OfficeRepository.get_office_repository()
    
    def add(self, office: Office) -> None:
        """
        Añade una nueva oficina.
        
        Args:
            office: La oficina a añadir
        """
        self._repository.add(office)
    
    def delete_by_direccion(self, direccion: str) -> None:
        """
        Elimina una oficina por su dirección.
        
        Args:
            direccion: La dirección de la oficina a eliminar
        """
        self._repository.delete_by_direccion(direccion)
    
    def find_all(self) -> List[Office]:
        """
        Devuelve todas las oficinas.
        
        Returns:
            Lista de todas las oficinas
        """
        return self._repository.find_all()
    
    def find_by_direccion(self, direccion: str) -> Optional[Office]:
        """
        Busca una oficina por su dirección.
        
        Args:
            direccion: La dirección de la oficina a buscar
            
        Returns:
            La oficina encontrada o None si no existe
        """
        return self._repository.find_by_direccion(direccion )
    
    def update(self, office: Office) -> None:
        """
        Actualiza los datos de una oficina.
        
        Args:
            office: La oficina con los datos actualizados
        """
        self._repository.update(office)

