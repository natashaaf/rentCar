from typing import List, Optional
from src.model.Office import Office
from src.repository.i_office_repository import IOfficeRepository


class OfficeRepository(IOfficeRepository):
    """
    Implementación del repositorio de oficinas usando el patrón Singleton.
    Almacena las oficinas en memoria.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._oficinas: List[Office] = []
            cls._instance._add_initial_oficinas()
        return cls._instance
    
    @classmethod
    def get_office_repository(cls) -> 'OfficeRepository':
        """
        Obtiene la instancia única del repositorio (Singleton).
        
        Returns:
            La instancia del repositorio de oficinas
        """
        return cls()
    
    def add(self, office: Office) -> None:
        """
        Añade una nueva oficina al repositorio.
        
        Args:
            office: La oficina a añadir
        """
        self._oficinas.append(office)
    
    def update(self, office: Office) -> None:
        """
        Actualiza los datos de una oficina existente.
        
        Args:
            office: La oficina con los datos actualizados
        """
        existing_office = self.find_by_direccion(office.direccion)
        if existing_office:
            index = self._oficinas.index(existing_office)
            self._oficinas[index] = office                                     
    
    def find_all(self) -> List[Office]:
        """
        Devuelve todas las oficinas del repositorio.
        
        Returns:
            Lista de todas las oficinas
        """
        return self._oficinas
    
    def delete_by_direccion(self, direccion: str) -> None:
        """
        Elimina una oficina por su dirección.
        
        Args:
            direccion: La dirección de la oficina a eliminar
        """
        for office in self._oficinas:
            if office.direccion == direccion:
                self._oficinas.remove(office)
                break
    
    def find_by_direccion(self, direccion: str) -> Optional[Office]:
        """
        Busca una oficina por su dirección.
        
        Args:
            direccion: La dirección de la oficina a buscar
            
        Returns:
            La oficina encontrada o None si no existe
        """
        for office in self._oficinas:
            if office.direccion == direccion:
                return office
        return None
    
    def clean_up(self) -> None:
        """Limpia todas las oficinas del repositorio."""
        self._oficinas = []
    
    def _add_initial_oficinas(self) -> None:
        """Añade las oficinas iniciales al repositorio."""
        self.add(Office("Calle Gran Vía 15, Madrid", 10.0))
        self.add(Office("Avinguda Diagonal 123, Barcelona", 15.0))
        self.add(Office("Calle Colón 45, Valencia", 5.0))
        self.add(Office("Plaza España 8, Sevilla", 8.0))
        self.add(Office("Calle Larios 22, Málaga", 12.0))
        self.add(Office("Aeropuerto Madrid-Barajas T4", 25.0))

