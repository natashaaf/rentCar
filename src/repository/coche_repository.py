from typing import List, Optional
from src.model import client
from src.model.Coche import Coche
from src.model.client import Client
from src.repository.client_repository import ClientRepository
from src.repository.i_client_repository import IClientRepository


class CocheRepository(ICocheRepository):
    """
    Implementación del repositorio de coches usando el patrón Singleton.
    Almacena los coches en memoria.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._coches: List[Coche] = []
            cls._instance._add_initial_coches()
        return cls._instance
    
    @classmethod
    def get_coche_repository(cls) -> 'CocheRepository':
        """
        Obtiene la instancia única del repositorio (Singleton).
        
        Returns:
            La instancia del repositorio de coches
        """
        return cls()
    
    def add(self, coche: Coche) -> None:
        """
        Añade un nuevo cliente al repositorio.
        
        Args:
            coche: El coche a añadir
        """
        coche.id = self._next_id_available()
        self._coches.append(coche)
    
    def update(self, coche: Coche) -> None:
        """
        Actualiza los datos de un coche existente.
        
        Args:
            coche: El coche con los datos actualizados
        """
        existing_coche = self.find_by_id(coche.id)
        if existing_coche   :
            index = self._coches.index(existing_coche)
            self._coches[index] = coche                                     
    
    def find_all(self) -> List[Coche]:
        """
        Devuelve todos los coches del repositorio.
        
        Returns:
            Lista de todos los coches
        """
        return self._coches
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un coche por su ID.
        
        Args:
            id: El ID del coche a eliminar
        """
        for coche in self._coches:
            if coche.id == id:
                self._coches.remove(coche)
                break
    
    def _next_id_available(self) -> int:
        """
        Calcula el siguiente ID disponible.
        
        Returns:
            El siguiente ID disponible
        """
        if self._coches:
            return self._coches[-1].id + 1
        return 1
    
    def find_by_id(self, id: int) -> Optional[Coche]:
        """
        Busca un coche por su ID.
        
        Args:
            id: El ID del coche a buscar
            
        Returns:
            El coche encontrado o None si no existe
        """
        for coche in self._coches:
            if coche.id == id:
                return coche        
        return None
    
    def find_by_dni(self, dni: str) -> Optional[Coche]:
        """
        Busca un coche por su DNI.
        
        Args:
            dni: El DNI del coche a buscar
            
        Returns:
            El coche encontrado o None si no existe
        """
        for coche in self._coches:
            if coche.dni == dni:
                return coche
        return None
    
    def clean_up(self) -> None:
        """Limpia todos los coches del repositorio."""
        self._coches = []
    
    def _add_initial_coches(self) -> None:
        """Añade los coches iniciales al repositorio."""
        self.add(Coche("87896685P", "Sergio", "Rodríguez"))
        self.add(Coche("99687554K", "Aurelio", "Fernández"))
        self.add(Coche("12345678A", "María", "González"))
        self.add(Coche("56789012B", "Lucía", "López"))
        self.add(Coche("34567890C", "Carlos", "Martínez"))
        self.add(Coche("78901234D", "Ana", "Sánchez"))

