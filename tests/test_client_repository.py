"""
Tests unitarios para el ClientRepository.
Equivalente a ClientRepositoryTest.java
"""
import sys
import os
import unittest

# Añadir el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from model.client import Client
from repository.client_repository import ClientRepository


class ClientRepositoryTest(unittest.TestCase):
    """Tests para el repositorio de clientes."""
    
    def setUp(self):
        """Configuración inicial antes de cada test."""
        self.repository = ClientRepository.get_client_repository()
        
        # Añadir clientes de prueba
        client1 = Client("87896685P", "María", "Rodríguez")
        client2 = Client("99687554W", "Nora", "Fernández")
        self.repository.add(client1)
        self.repository.add(client2)
    
    def tearDown(self):
        """Limpieza después de cada test."""
        self.repository.clean_up()
        self.repository._add_initial_clients()
    
    def test_add(self):
        """Test para añadir clientes."""
        client3 = Client("39887554G", "Pedro", "Fernández")
        self.repository.add(client3)
        self.assertEqual(client3, self.repository.find_by_id(9))
        
        client4 = Client("59887995L", "Juan", "Pérez")
        self.repository.add(client4)
        self.assertEqual(client4.dni, self.repository.find_by_id(10).dni)
    
    def test_find_all(self):
        """Test para obtener todos los clientes."""
        self.assertEqual(8, len(self.repository.find_all()))
        
        client = Client("48572039G", "Tamara", "Sánchez")
        self.repository.add(client)
        self.assertEqual(9, len(self.repository.find_all()))
        
        self.repository.delete_by_id(2)
        self.assertEqual(8, len(self.repository.find_all()))
    
    def test_delete_by_id(self):
        """Test para eliminar clientes por ID."""
        self.assertEqual(8, len(self.repository.find_all()))
        
        self.repository.delete_by_id(11)  # No existe
        self.assertEqual(8, len(self.repository.find_all()))
        
        self.repository.delete_by_id(2)
        self.assertEqual(7, len(self.repository.find_all()))
        
        self.repository.delete_by_id(1)
        self.assertEqual(6, len(self.repository.find_all()))
    
    def test_next_id_available(self):
        """Test para obtener el siguiente ID disponible."""
        self.assertEqual(9, self.repository._next_id_available())
        
        client = Client("48572039G", "Tamara", "Sánchez")
        self.repository.add(client)
        self.assertEqual(10, self.repository._next_id_available())
        
        self.repository.delete_by_id(1)
        self.assertEqual(10, self.repository._next_id_available())
    
    def test_find_by_id(self):
        """Test para buscar cliente por ID."""
        self.assertEqual("87896685P", self.repository.find_by_id(7).dni)
        self.assertEqual("Nora", self.repository.find_by_id(8).name)
    
    def test_find_by_dni(self):
        """Test para buscar cliente por DNI."""
        self.assertEqual(1, self.repository.find_by_dni("87896685P").id)
        self.assertEqual("Nora", self.repository.find_by_dni("99687554W").name)
    
    def test_update(self):
        """Test para actualizar un cliente."""
        self.assertEqual("87896685P", self.repository.find_by_id(7).dni)
        
        client = Client("4453366OT", "Ignacio", "Pérez", 3)
        self.repository.update(client)
        self.assertEqual("4453366OT", self.repository.find_by_id(3).dni)


if __name__ == '__main__':
    unittest.main()

