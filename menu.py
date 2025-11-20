import random
from hotdog import Hotdog

class Menu:
    """Administra los hot dogs del menú."""
    def __init__(self):
        self.hotdogs = []  

    def ver_menu(self):
        """Retorna la lista de HotDogs. (list)"""
        return self.hotdogs

    def agregar_hotdog(self, hotdog):
        """Agrega un nuevo hot dog al menú. (None)"""
        self.hotdogs.append(hotdog)

    def eliminar_hotdog(self, nombre):
        """Elimina un hot dog del menú. (None)"""
        nueva_lista = []
        for hd in self.hotdogs:
            if hd.nombre != nombre:
                nueva_lista.append(hd)
        self.hotdogs = nueva_lista

    def elegir_hotdog_random(self):
        """Selecciona un HotDog al azar para la simulación."""
        if len(self.hotdogs) == 0:
            return None
        return random.choice(self.hotdogs)
        
    def ingredientes_en_uso(self):
        """Devuelve un conjunto con todos los ingredientes usados en el menú."""
        usados = set()
        for hd in self.hotdogs:
            for ing_nombre in hd.ingredientes_totales():
                usados.add(ing_nombre)
        return usados

    def eliminar_hotdogs_con_ingrediente(self, nombre_ingrediente):
        """Elimina todos los hot dogs que usan un ingrediente específico."""
        nueva_lista = []
        for hd in self.hotdogs:
            is_used = False
            for ing_nombre in hd.ingredientes_totales():
                if ing_nombre == nombre_ingrediente:
                    is_used = True
                    break
            if is_used == False:
                nueva_lista.append(hd)
        self.hotdogs = nueva_lista
        print(f"Se eliminaron hot dogs que usaban '{nombre_ingrediente}'.")


