class Modelo:
    def __init__(self, id, nombre, precioDia, listaCoches):
        self.id = id
        self.nombre = nombre
        self.precioDia = precioDia
        self.listaCoches = listaCoches if listaCoches else []
    