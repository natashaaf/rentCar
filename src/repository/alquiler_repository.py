from typing import List, Optional
from src.model.Alquiler import Alquiler
from src.model.client import Client
from src.model.Coche import Coche
from src.model.Office import Office
from src.repository.i_alquiler_repository import IAlquilerRepository


class AlquilerRepository(IAlquilerRepository):
    """
    Implementación del repositorio de alquileres usando el patrón Singleton.
    Almacena los alquileres en memoria.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._alquileres: List[Alquiler] = []
            cls._instance._add_initial_alquileres()
        return cls._instance
    
    @classmethod
    def get_alquiler_repository(cls) -> 'AlquilerRepository':
        """
        Obtiene la instancia única del repositorio (Singleton).
        
        Returns:
            La instancia del repositorio de alquileres
        """
        return cls()
    
    def add(self, alquiler: Alquiler) -> None:
        """
        Añade un nuevo alquiler al repositorio.
        
        Args:
            alquiler: El alquiler a añadir
        """
        alquiler.id = self._next_id_available()
        self._alquileres.append(alquiler)
    
    def update(self, alquiler: Alquiler) -> None:
        """
        Actualiza los datos de un alquiler existente.
        
        Args:
            alquiler: El alquiler con los datos actualizados
        """
        existing_alquiler = self.find_by_id(alquiler.id)
        if existing_alquiler:
            index = self._alquileres.index(existing_alquiler)
            self._alquileres[index] = alquiler
    
    def find_all(self) -> List[Alquiler]:
        """
        Devuelve todos los alquileres del repositorio.
        
        Returns:
            Lista de todos los alquileres
        """
        return self._alquileres
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un alquiler por su ID.
        
        Args:
            id: El ID del alquiler a eliminar
        """
        for alquiler in self._alquileres:
            if alquiler.id == id:
                self._alquileres.remove(alquiler)
                break
    
    def _next_id_available(self) -> int:
        """
        Calcula el siguiente ID disponible.
        
        Returns:
            El siguiente ID disponible
        """
        if self._alquileres:
            return self._alquileres[-1].id + 1
        return 1
    
    def find_by_id(self, id: int) -> Optional[Alquiler]:
        """
        Busca un alquiler por su ID.
        
        Args:
            id: El ID del alquiler a buscar
            
        Returns:
            El alquiler encontrado o None si no existe
        """
        for alquiler in self._alquileres:
            if alquiler.id == id:
                return alquiler
        return None
    
    def clean_up(self) -> None:
        """Limpia todos los alquileres del repositorio."""
        self._alquileres = []
    
    def _add_initial_alquileres(self) -> None:
        """Añade los alquileres iniciales al repositorio."""
        # Crear objetos de ejemplo
        cliente1 = Client("87896685P", "Sergio", "Rodríguez")
        cliente2 = Client("99687554K", "Aurelio", "Fernández")
        
        coche1 = Coche("ABC123", "Toyota Corolla", "Madrid Centro")
        coche2 = Coche("DEF456", "BMW X3", "Barcelona Plaza")
        
        oficina1 = Office("Calle Gran Vía 15, Madrid", 10.0)
        oficina2 = Office("Avinguda Diagonal 123, Barcelona", 15.0)
        
        # Crear alquileres de ejemplo
        self.add(Alquiler(None, "2024-03-01", "2024-03-05", cliente1, coche1, oficina1))
        self.add(Alquiler(None, "2024-03-10", "2024-03-15", cliente2, coche2, oficina2))
        self.add(Alquiler(None, "2024-02-20", "2024-02-25", cliente1, coche2, oficina1))

