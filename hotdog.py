class HotDog:
    """Representa una receta específica de Hot Dog en el menú."""
    def __init__(self, nombre, pan, salchicha, toppings, salsas, acompanante=None):
        self.nombre = nombre
        self.pan = pan
        self.salchicha = salchicha
        self.toppings = toppings  
        self.salsas = salsas      
        self.acompanante = acompanante

    def validar_longitud(self, lista_ingredientes):
        """Verifica si el pan y la salchicha son compatibles usando sus 'tipos' (bool).
        Busca los objetos Ingrediente usando un bucle for."""
        pan = None
        salchicha = None
        
        # Bucle explícito para encontrar el pan y la salchicha
        for i in lista_ingredientes:
            if i.nombre == self.pan:
                pan = i
            if i.nombre == self.salchicha:
                salchicha = i
        
        if pan is not None and salchicha is not None:
            if pan.tipo == salchicha.tipo:
                return True
            else:
                return False
        
        # Falla si no se encuentran los ingredientes registrados (debería ser validado por Tienda antes)
        return False

    def mostrar_info(self):
        """Muestra los detalles completos de la receta. (None)"""
        print(f"*** Receta: {self.nombre} ***")
        print(f"  Pan: {self.pan}")
        print(f"  Salchicha: {self.salchicha}")
        print(f"  Toppings: {', '.join(self.toppings)}")
        print(f"  Salsas: {', '.join(self.salsas)}")
        if self.acompanante is not None:
            print(f"  Acompañante: {self.acompanante}")
    
    def ingredientes_totales(self):
        """Devuelve una lista con todos los nombres de ingredientes."""
        ingredientes = [self.pan, self.salchicha] + self.toppings + self.salsas
        if self.acompanante is not None:
            ingredientes.append(self.acompanante)
        return ingredientes
