
from typing import List, Optional
from src.model.Modelo import Modelo
from src.repository.i_modelo_repository import IModeloRepository

class ModeloRepository(IModeloRepository):
    """
    Implementación del repositorio de modelos usando el patrón Singleton.
    Almacena los modelos en memoria.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._modelos: List[Modelo] = []
            cls._instance._add_initial_modelos()
        return cls._instance
    
    @classmethod
    def get_modelo_repository(cls) -> 'ModeloRepository':
        """
        Obtiene la instancia única del repositorio (Singleton).
        
        Returns:
            La instancia del repositorio de modelos
        """
        return cls()
    
    def add(self, modelo: Modelo) -> None:
        """
        Añade un nuevo modelo al repositorio.
        
        Args:
            modelo: El modelo a añadir
        """
        modelo.id = self._next_id_available()
        self._modelos.append(modelo)
    
    def update(self, modelo: Modelo) -> None:
        """
        Actualiza los datos de un modelo existente.
        
        Args:
            modelo: El modelo con los datos actualizados
        """
        existing_modelo = self.find_by_id(modelo.id)
        if existing_modelo:
            index = self._modelos.index(existing_modelo)
            self._modelos[index] = modelo
    
    def find_all(self) -> List[Modelo]:
        """
        Devuelve todos los modelos del repositorio.
        
        Returns:
            Lista de todos los modelos
        """
        return self._modelos
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un modelo por su ID.
        
        Args:
            id: El ID del modelo a eliminar
        """
        for modelo in self._modelos:
            if modelo.id == id:
                self._modelos.remove(modelo)
                break
    
    def _next_id_available(self) -> int:
        """
        Calcula el siguiente ID disponible.
        
        Returns:
            El siguiente ID disponible
        """ 
        if self._modelos:
            return self._modelos[-1].id + 1
        return 1
    
    def find_by_id(self, id: int) -> Optional[Modelo]:
        """
        Busca un modelo por su ID.
        
        Args:
            id: El ID del modelo a buscar
            
        Returns:
            El modelo encontrado o None si no existe
        """
        for modelo in self._modelos:
            if modelo.id == id:
                return modelo
        return None
    
    def find_by_nombre(self, nombre: str) -> Optional[Modelo]:
        """
        Busca un modelo por su nombre.
        
        Args:
            nombre: El nombre del modelo a buscar
            
        Returns:
            El modelo encontrado o None si no existe
        """
        for modelo in self._modelos:
            if modelo.nombre == nombre:
                return modelo
        return None
    
    def clean_up(self) -> None:
        """Limpia todos los modelos del repositorio."""
        self._modelos = []
    
    def _add_initial_modelos(self) -> None:
        """Añade los modelos iniciales al repositorio."""
        self.add(Modelo(None, "Toyota Corolla", 25.0, []))
        self.add(Modelo(None, "BMW X3", 45.0, []))
        self.add(Modelo(None, "Audi A4", 40.0, []))
        self.add(Modelo(None, "Mercedes C-Class", 50.0, []))
        self.add(Modelo(None, "Volkswagen Golf", 30.0, []))
        self.add(Modelo(None, "Seat León", 28.0, []))

