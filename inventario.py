class Inventario:
    """Clase gestora del Inventario. Mantiene el stock (cantidad) de cada ingrediente."""
    def __init__(self):
        self.stock = {} 

    def ver_inventario(self):
        """Retorna el diccionario completo del stock. (dict)"""
        return self.stock

    def buscar_ingrediente(self, nombre):
        """Retorna la cantidad disponible de un ingrediente. (int)"""
        if nombre in self.stock:
            return self.stock[nombre]
        else:
            return 0 # Si no existe, la cantidad es 0

    def actualizar(self, nombre, cantidad):
        """Actualiza la cantidad de un ingrediente. (None)"""
        if nombre in self.stock:
            self.stock[nombre] = cantidad
        else:
            print(f"El ingrediente '{nombre}' no está en el inventario.")

    def registrar_compra(self, nombre, cantidad):
        """Registra una nueva compra (suma al stock). (None)"""
        if nombre in self.stock:
            self.stock[nombre] = self.stock[nombre] + cantidad
        else:
            # Inicializa el ingrediente si es la primera compra
            self.stock[nombre] = cantidad 
        print(f"Compra registrada: {cantidad} unidades de '{nombre}'.")

    def validar_disponibilidad(self, nombre, cantidad_requerida):
        """Valida si hay suficiente stock de un ingrediente. (bool)"""
        if nombre in self.stock:
            return self.stock[nombre] >= cantidad_requerida
        else:
            return False
    
    def consumir_ingrediente(self, nombre, cantidad=1):
        """Reduce el stock después de una venta."""
        if self.validar_disponibilidad(nombre, cantidad):
            self.stock[nombre] = self.stock[nombre] - cantidad
            return True
        return False
