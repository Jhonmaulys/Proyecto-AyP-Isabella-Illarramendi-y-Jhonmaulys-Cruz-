import random 

class SimulacionDia:
    """Clase encargada de la simulación de un día de ventas."""
    def __init__(self, menu, inventario):
        self.menu = menu
        self.inventario = inventario
        
        self.clientes = 0 
        self.ventas = []  
        self.resultados = {
            'clientes_simulados': 0,
            'clientes_cambiaron_opinion': 0,
            'clientes_sin_servicio': 0,
            'hotdogs_comprados_total': 0,
            'total_acompanantes_vendidos': 0,
            'ventas_por_hotdog': {},
            'ingredientes_agotados': set(),
            'hotdogs_que_causaron_marcha': set(),
            'ingredientes_que_causaron_marcha': set()
        }

    def simular(self, num_clientes):
        """Simula la atención de num_clientes en el día. (None)"""
        self.clientes = num_clientes
        self.resultados['clientes_simulados'] = num_clientes
        
        for i in range(1, num_clientes + 1):
            # Cliente compra entre 0 y 5 hot dogs (Requerimiento)
            num_hotdogs_a_comprar = random.randint(0, 5)
            
            if num_hotdogs_a_comprar == 0:
                self.resultados['clientes_cambiaron_opinion'] = self.resultados['clientes_cambiaron_opinion'] + 1
                continue

            orden_exitosa = True
            hotdog_causante = None
            ingrediente_faltante = None
            orden_del_cliente = []

            # 1. Crear la orden del cliente
            for _ in range(num_hotdogs_a_comprar):
                hotdog_receta = self.menu.elegir_hotdog_random()
                if hotdog_receta is not None:
                    orden_del_cliente.append(hotdog_receta)

            if len(orden_del_cliente) == 0:
                 # Si no hay recetas en el menú, nadie puede comprar
                 continue

            # 2. Verificar inventario para toda la orden (Si falla uno, el cliente se marcha - Requerimiento)
            for hotdog in orden_del_cliente:
                for ing_nombre in hotdog.ingredientes_totales():
                    if self.inventario.validar_disponibilidad(ing_nombre, 1) == False:
                        orden_exitosa = False
                        hotdog_causante = hotdog
                        ingrediente_faltante = ing_nombre
                        break
                if orden_exitosa == False:
                    break
            
            if orden_exitosa == False:
                # 3. Cliente se marcha
                self.resultados['clientes_sin_servicio'] = self.resultados['clientes_sin_servicio'] + 1
                if hotdog_causante is not None:
                    self.resultados['hotdogs_que_causaron_marcha'].add(hotdog_causante.nombre)
                if ingrediente_faltante is not None:
                    self.resultados['ingredientes_que_causaron_marcha'].add(ingrediente_faltante)
                continue

            # 4. Procesar venta exitosa
            for hotdog in orden_del_cliente:
                for ing_nombre in hotdog.ingredientes_totales():
                    self.inventario.consumir_ingrediente(ing_nombre, 1)
                    
                    # Contar acompañantes
                    # Se asume que el acompañante es el ingrediente final si existe
                    if hotdog.acompanante is not None and ing_nombre == hotdog.acompanante:
                        self.resultados['total_acompanantes_vendidos'] = self.resultados['total_acompanantes_vendidos'] + 1
                        
                    # Registrar agotamiento
                    if self.inventario.buscar_ingrediente(ing_nombre) == 0:
                        self.resultados['ingredientes_agotados'].add(ing_nombre)
                        
                # Registrar venta
                hotdog_nombre = hotdog.nombre
                if hotdog_nombre in self.resultados['ventas_por_hotdog']:
                    self.resultados['ventas_por_hotdog'][hotdog_nombre] = self.resultados['ventas_por_hotdog'][hotdog_nombre] + 1
                else:
                    self.resultados['ventas_por_hotdog'][hotdog_nombre] = 1
                
                self.resultados['hotdogs_comprados_total'] = self.resultados['hotdogs_comprados_total'] + 1
    
    def reporte(self):
        """Muestra el reporte detallado con todos los datos requeridos. (None)"""
        print("\n--- REPORTE DE SIMULACIÓN DEL DÍA ---")
        
        total_clientes = self.resultados['clientes_simulados']
        ventas_totales = self.resultados['hotdogs_comprados_total']
        clientes_reales = total_clientes - self.resultados['clientes_cambiaron_opinion']
        
        # 4. Promedio de hot dogs por cliente (excluyendo los que cambiaron de opinión)
        promedio = 0.0
        if clientes_reales > 0:
            promedio = ventas_totales / clientes_reales
        
        print(f"1. Total de clientes simulados: {total_clientes}")
        print(f"2. Clientes que cambiaron de opinión: {self.resultados['clientes_cambiaron_opinion']}")
        print(f"3. Clientes no atendidos (por falta de stock): {self.resultados['clientes_sin_servicio']}")
        print(f"4. Promedio de hot dogs comprados por cliente: {promedio:.2f}")

        # 5. Hot dog más vendido (Búsqueda simple con loop)
        hotdog_mas_vendido = "N/A"
        max_ventas = -1
        for hd, cantidad in self.resultados['ventas_por_hotdog'].items():
            if cantidad > max_ventas:
                max_ventas = cantidad
                hotdog_mas_vendido = hd
        print(f"5. Hot dog más vendido: {hotdog_mas_vendido} ({max_ventas} unidades)")
        
        # 6. Hot dogs que causaron que el cliente se marchara
        hotdogs_marcha_str = ", ".join(self.resultados['hotdogs_que_causaron_marcha'])
        print(f"6. Hot dogs que causaron que el cliente se marchara: {hotdogs_marcha_str}")
        
        # 7. Ingredientes que causaron que el cliente se marchara
        ing_marcha_str = ", ".join(self.resultados['ingredientes_que_causaron_marcha'])
        print(f"7. Ingredientes que causaron que el cliente se marchara: {ing_marcha_str}")

        # 8. Total de acompañantes vendidos
        print(f"8. Total de acompañantes vendidos: {self.resultados['total_acompanantes_vendidos']}")