import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))
from TrabajoPractico_1.proyecto_1.modules.ListaDobleEnlazada import ListaDobleEnlazada

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self._mazo = ListaDobleEnlazada()
    def poner_carta_arriba(self, carta):
        self._mazo.agregar_al_inicio(carta)
    def poner_carta_abajo(self, carta):
        self._mazo.agregar_al_final(carta)
    def sacar_carta_arriba(self, mostrar=False):
        if len(self._mazo) == 0:
            raise DequeEmptyError("El mazo está vacío")
        carta = self._mazo.extraer(0)
        if mostrar:
            carta.visible = True
        return carta
    def __len__(self):
        return len(self._mazo)
    def __iter__(self):
        return iter(self._mazo)
    def __str__(self):
        salida = ''
        for idx, carta in enumerate(self._mazo):
            salida += str(carta) + ' '  # Agrega cada carta a la cadena de salida
            if idx % 10 == 9:
                salida += '\n'  # Agrega un salto de línea cada 10 cartas
        return salida  # Devuelve la representación en cadena del mazo
    