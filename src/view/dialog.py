import sys
from controller.client_controller import ClientController


class Dialog:
    """
    Clase que gestiona la interfaz de usuario por consola. 
    Presenta los menús y recoge la entrada del usuario.
    """
    
    def __init__(self):
        """Inicializa el diálogo con el controlador de clientes."""
        self._client_controller = ClientController()
    
    def get_started(self) -> None:
        """Muestra el menú principal y gestiona la navegación."""
        while True:
            print("\n********************** Welcome to Rent A Car *****************************")
            print("\n\t1. Manage Clients.\t\t\t\t4. Manage Models.")
            print("\n\t2. Manage Cars.\t\t\t\t\t5. Manage Rents.")
            print("\n\t3. Manage Offices.\t\t\t\t0. Exit.")
            print("\n**************************************************************************")
            
            try:
                choice = int(input("Seleccione una opción: "))
                
                if choice == 1:
                    self._client_manager()
                elif choice == 2:
                    self.Coche_manager()
                    print("Funcionalidad pendiente de implementar")
                elif choice == 3:
                    self.Oficina_manager()
                    print("Funcionalidad pendiente de implementar")
                elif choice == 4:
                    self.Modelo_manager()
                    print("Funcionalidad pendiente de implementar")
                elif choice == 5:
                    self.Alquiler_manager()
                    print("Funcionalidad pendiente de implementar")
                elif choice == 0:
                    print("Bye!!")
                    sys.exit(0)
                else:
                    print("[ERROR] Your option is incorrect!! Try again!!", file=sys.stderr)
                    
            except ValueError:
                print("[ERROR] You must type a number!!!", file=sys.stderr)
            except Exception as e:
                print(f"[ERROR] {str(e)}", file=sys.stderr)
    
    def _client_manager(self) -> None:
        """Gestiona el submenú de clientes."""
        while True:
            print("\n************************** Client Manager ********************************")
            print("\n\t1. Create Client.\t\t\t\t4. Search Client.")
            print("\n\t2. Remove Client.\t\t\t\t5. See All Clients.")
            print("\n\t3. Update Client.\t\t\t\t0. Back.")
            print("\n**************************************************************************")
            
            try:
                choice = int(input("Seleccione una opción: "))
                
                if choice == 1:
                    # Crear cliente
                    dni = input("Dni: ")
                    name = input("Name: ")
                    surname = input("Surname: ")
                    self._client_controller.add(dni, name, surname)
                    print("Cliente creado correctamente.")
                    
                elif choice == 2:
                    # Eliminar cliente
                    id = int(input("Client ID: "))
                    self._client_controller.delete_by_id(id)
                    print("Cliente eliminado correctamente.")
                    
                elif choice == 3:
                    # Actualizar cliente
                    print("Clientes actuales:")
                    for client in self._client_controller.find_all():
                        print(client)
                    id = int(input("Client ID: "))
                    dni = input("Dni: ")
                    name = input("Name: ")
                    surname = input("Surname: ")
                    self._client_controller.update(id, dni, name, surname)
                    print("Cliente actualizado correctamente.")
                    
                elif choice == 4:
                    # Buscar cliente por DNI
                    dni = input("Dni: ")
                    client = self._client_controller.find_by_dni(dni)
                    if client:
                        print(client)
                    else:
                        print("Cliente no encontrado.")
                        
                elif choice == 5:
                    # Ver todos los clientes
                    print("\nListado de clientes:")
                    for client in self._client_controller.find_all():
                        print(client)
                        
                elif choice == 0:
                    # Volver al menú principal
                    return
                else:
                    print("[ERROR] Your option is incorrect!! Try again!!", file=sys.stderr)
                    
            except ValueError:
                print("[ERROR] You must type a number!!!", file=sys.stderr)
            except Exception as e:
                print(f"[ERROR] {str(e)}", file=sys.stderr)




