# Asistente para Agricultores - Panamá

## Descripción General

El Asistente para Agricultores es un sistema especializado diseñado para apoyar a los productores agrícolas panameños en la toma de decisiones informadas sobre sus cultivos. La aplicación proporciona acceso a información técnica detallada de 25 cultivos principales del país, análisis climáticos y herramientas de visualización de datos.

## Características Principales

### Base de Datos de Cultivos
El sistema contiene información completa sobre los cultivos más importantes de Panamá, incluyendo datos sobre temporadas de siembra, tiempos de cosecha, rendimientos esperados y requerimientos climáticos específicos para cada variedad.

### Análisis de Datos Agrícolas
Permite realizar análisis estadísticos comparativos entre diferentes cultivos, generar reportes de rendimiento y obtener recomendaciones basadas en datos históricos y condiciones actuales.

### Visualización Gráfica
Genera gráficos especializados que muestran comparaciones de rendimientos, distribuciones climáticas, tiempos de cosecha y análisis de cultivos similares para facilitar la interpretación de la información.

### Integración Climática
Conecta con servicios meteorológicos para proporcionar información climática actualizada y evaluar la compatibilidad entre las condiciones actuales y los requerimientos de cada cultivo.

### Herramientas de Cálculo
Incluye calculadoras para estimar rendimientos por hectárea, planificar siembras y evaluar la viabilidad económica de diferentes opciones de cultivo.

## Cultivos Disponibles

El sistema incluye información de 25 cultivos organizados por categorías:

**Granos Básicos:** Arroz, Maíz, Frijol, Sorgo  
**Tubérculos:** Yuca, Ñame, Ñampí, Papa  
**Plátanos:** Plátano, Banano  
**Frutas:** Naranja, Limón, Mango, Papaya, Piña, Aguacate, Coco  
**Hortalizas:** Tomate, Cebolla, Pimiento, Lechuga, Repollo  
**Cultivos Especiales:** Café, Cacao, Caña de Azúcar

## Instalación 

```bash
pip install -r requirements.txt
python asistente_agricola_modular.py
```

## Requisitos del Sistema

- Python 3.8 o superior
- Librerías: pandas, matplotlib, tkinter, requests