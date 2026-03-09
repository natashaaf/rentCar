from typing import List, Optional
from src.model.Client import Client
from src.repository.i_client_repository import IClientRepository


class ClientRepository(IClientRepository):
    """
    Implementación del repositorio de clientes usando el patrón Singleton.
    Almacena los clientes en memoria.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._clients = []
            cls._instance._add_initial_clients()
        return cls._instance
    
    @classmethod
    def get_client_repository(cls) -> 'ClientRepository':
        """
        Obtiene la instancia única del repositorio (Singleton).
        
        Returns:
            La instancia del repositorio de clientes
        """
        return cls()
    
    def add(self, client: Client) -> None:
        """
        Añade un nuevo cliente al repositorio.
        
        Args:
            client: El cliente a añadir
        """
        client.id = self._next_id_available()
        self._clients.append(client)
    
    def update(self, client: Client) -> None:
        """
        Actualiza los datos de un cliente existente.
        
        Args:
            client: El cliente con los datos actualizados
        """
        existing_client = self.find_by_id(client.id)
        if existing_client:
            index = self._clients.index(existing_client)
            self._clients[index] = client
    
    def find_all(self) -> List[Client]:
        """
        Devuelve todos los clientes del repositorio.
        
        Returns:
            Lista de todos los clientes
        """
        return self._clients
    
    def delete_by_id(self, id: int) -> None:
        """
        Elimina un cliente por su ID.
        
        Args:
            id: El ID del cliente a eliminar
        """
        for client in self._clients:
            if client.id == id:
                self._clients.remove(client)
                break
    
    def _next_id_available(self) -> int:
        """
        Calcula el siguiente ID disponible.
        
        Returns:
            El siguiente ID disponible
        """
        if self._clients:
            return self._clients[-1].id + 1
        return 1
    
    def find_by_id(self, id: int) -> Optional[Client]:
        """
        Busca un cliente por su ID.
        
        Args:
            id: El ID del cliente a buscar
            
        Returns:
            El cliente encontrado o None si no existe
        """
        for client in self._clients:
            if client.id == id:
                return client
        return None
    
    def find_by_dni(self, dni: str) -> Optional[Client]:
        """
        Busca un cliente por su DNI.
        
        Args:
            dni: El DNI del cliente a buscar
            
        Returns:
            El cliente encontrado o None si no existe
        """
        for client in self._clients:
            if client.dni == dni:
                return client
        return None
    
    def clean_up(self) -> None:
        """Limpia todos los clientes del repositorio."""
        self._clients = []

    def _add_initial_clients(self) -> None:
        """Añade los clientes iniciales al repositorio."""
        self.add(Client("87896685P", "Sergio", "Rodríguez"))
        self.add(Client("99687554K", "Aurelio", "Fernández"))
        self.add(Client("12345678A", "María", "González"))
        self.add(Client("56789012B", "Lucía", "López"))
        self.add(Client("34567890C", "Carlos", "Martínez"))
        self.add(Client("78901234D", "Ana", "Sánchez"))


