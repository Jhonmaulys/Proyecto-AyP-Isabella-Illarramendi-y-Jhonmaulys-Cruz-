# estadisticas.py
# Módulo de Estadísticas (Bono - Requiere 'pip install matplotlib')

class Estadisticas:
    """
    Clase para el módulo de Estadísticas. Grafica los resultados de SimulacionDia
    cuando hay al menos 2 días simulados.
    """
    def __init__(self, historial_simulaciones):
        self.dias_simulados = len(historial_simulaciones)
        self.historial = historial_simulaciones
        self.datos = self._compilar_datos()

    def _compilar_datos(self):
        """Compila los datos numéricos esenciales de cada día simulado."""
        datos_compilados = {}
        i = 1
        for sim in self.historial:
            datos_dia = {}
            datos_dia['clientes_simulados'] = sim.clientes
            datos_dia['clientes_sin_servicio'] = sim.resultados['clientes_sin_servicio']
            datos_dia['total_hotdogs_vendidos'] = sim.resultados['hotdogs_comprados_total']
            datos_compilados[i] = datos_dia
            i = i + 1
        return datos_compilados

    def graficar(self):
        """Grafica los valores numéricos de cada día simulado. (None)"""
        if self.dias_simulados < 2:
            print("Se necesitan al menos 2 días de simulación para graficar las estadísticas (Bono).")
            return

        try:
            import matplotlib.pyplot as plt
            
            dias = []
            clientes = []
            no_atendidos = []
            vendidos = []
            
            for dia, datos in self.datos.items():
                dias.append(dia)
                clientes.append(datos['clientes_simulados'])
                no_atendidos.append(datos['clientes_sin_servicio'])
                vendidos.append(datos['total_hotdogs_vendidos'])

            fig, ax = plt.subplots(3, 1, figsize=(8, 7), sharex=True)
            
            ax[0].bar(dias, clientes, color='blue')
            ax[0].set_title('Clientes Simulados por Día')
            
            ax[1].bar(dias, no_atendidos, color='red')
            ax[1].set_title('Clientes No Atendidos por Día')
            
            ax[2].bar(dias, vendidos, color='green')
            ax[2].set_title('Hot Dogs Vendidos por Día')
            ax[2].set_xlabel('Día de Simulación')
            
            plt.tight_layout()
            plt.show()

        except ImportError:
            print("Error: La librería 'matplotlib' no está instalada.")
            print("Instale con: pip install matplotlib")

    def resumen(self):
        """Genera un resumen de los datos estadísticos. (None)"""
        print("\n--- RESUMEN ESTADÍSTICO HISTÓRICO ---")
        if self.dias_simulados == 0:
            print("No hay días simulados registrados.")
            return

        for dia, datos in self.datos.items():
            print(f"\nDía {dia}: Clientes Totales: {datos['clientes_simulados']}, Perdidos: {datos['clientes_sin_servicio']}, Vendidos: {datos['total_hotdogs_vendidos']}")
