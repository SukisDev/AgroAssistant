__version__ = "2.0"
__author__ = "Sistema Agrícola AI"

# Importaciones de los módulos
from .datos import DatosManager
from .graficos import GraficosManager
from .clima import ClimaManager
from .interfaz import InterfazManager

__all__ = [
    'DatosManager',
    'GraficosManager', 
    'ClimaManager',
    'InterfazManager'
]