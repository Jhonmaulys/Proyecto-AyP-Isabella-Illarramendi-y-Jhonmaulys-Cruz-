# ingrediente.py

class Ingrediente:
    """Clase base para todos los ingredientes del sistema."""
    def __init__(self, id, nombre, categoria, tipo):
        self.id = id 
        self.nombre = nombre
        self.categoria = categoria
        self.tipo = tipo

    # Métodos del diagrama: Son métodos vacíos (placeholders) ya que
    # la gestión (agregar/eliminar) la realiza la clase Tienda.
    def agregar(self): pass 
    def validar(self): return True
    def eliminar(self): pass 
    
    def __str__(self):
        return f"ID: {self.id}, {self.categoria}, {self.nombre}, Tipo: {self.tipo}"
    
    def to_dict(self):
        """Convierte el ingrediente a un diccionario para guardar (Formato simple)."""
        data = {}
        data['id'] = self.id
        data['nombre'] = self.nombre
        data['categoria'] = self.categoria
        data['tipo'] = self.tipo
        return data

class Ingrediente_longitud(Ingrediente):
    """Clase para Panes y Salchichas."""
    pass

class Acompanante(Ingrediente):
    """Clase para acompañantes (papas, bebidas, etc.)."""
    pass