class Client:
    """
    Modelo que representa un cliente del sistema de alquiler de coches.
    
    Attributes:
        id (int): Identificador único del cliente
        dni (str): Documento Nacional de Identidad
        name (str): Nombre del cliente
        surname (str): Apellidos del cliente
    """
    
    def __init__(self, dni: str, name: str, surname: str, id: int = None):
        """
        Inicializa un nuevo cliente.
        
        Args:
            dni: Documento Nacional de Identidad
            name: Nombre del cliente
            surname: Apellidos del cliente
            id: Identificador único (opcional, se asigna automáticamente)
        """
        self._id = id
        self._dni = dni
        self._name = name
        self._surname = surname
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value
    
    @property
    def dni(self) -> str:
        return self._dni
    
    @dni.setter
    def dni(self, value: str):
        self._dni = value
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
    
    @property
    def surname(self) -> str:
        return self._surname
    
    @surname.setter
    def surname(self, value: str):
        self._surname = value
    
    def __str__(self) -> str:
        return f"{self._id} {self._name} {self._surname}"
    
    def __repr__(self) -> str:
        return f"Client(id={self._id}, dni='{self._dni}', name='{self._name}', surname='{self._surname}')"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Client):
            return False
        return self._id == other._id and self._dni == other._dni

