# Arquitectura del Proyecto

Este proyecto sigue una arquitectura modular y desacoplada, orientada a la escalabilidad y al mantenimiento a largo plazo. La estructura de directorios refleja una clara separación de responsabilidades, lo que facilita su comprensión y evolución.

## Estructura de Carpetas

FinancialMarketAnalyzer/
│
├── analyzer/
│ └── stock_analyzer.py
│
├── display/
│ └── output_displayer.py
│
├── market_loader/
│ └── ticker_searcher.py
|
├── main.py
├── launch.py
└── requirements.txt


# El primer módulo, analyzer persigue la lógica principal de análisis y cálculo de indicador de buen precio

# El segundo módulo, display: conserva la responsabilidad exclusiva de la presentación de resultados

# El tercer módulo, market_loader: es el responsable de la obtención y preprocesamiento de los tickers

## Principios y Patrones Seguidos

- **Single Responsibility Principle (SRP)**: Cada módulo cumple una única función claramente delimitada.
- **Separation of Concerns (SoC)**: Separamos claramente la adquisición de datos, el análisis y la presentación.
- **Open/Closed Principle**: El diseño favorece la extensión (por ejemplo, añadir nuevos mercados o métricas) sin modificar los módulos existentes.
- **Inversión de dependencias ligera**: Las dependencias se mantienen mínimas y gestionadas, priorizando la inyección de funciones y uso explícito de importaciones.

## Ventajas de la arquitectura elegida

- **Escalabilidad**: Fácil de extender con nuevos analizadores, mercados o estrategias.
- **Mantenibilidad**: Cada módulo puede desarrollarse y probarse de forma independiente.