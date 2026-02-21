#!/usr/bin/env python3
"""
Punto de entrada principal de la aplicación Rent A Car.
"""
import sys
import os

# Añadir el directorio src al path para poder importar los módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from view.dialog import Dialog


def main():
    """Función principal que inicia la aplicación."""
    dialog = Dialog()
    dialog.get_started()


if __name__ == "__main__":
    main()

