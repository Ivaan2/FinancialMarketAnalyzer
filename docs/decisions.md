# Decisiones de Diseño

Este documento explica las decisiones técnicas y de diseño adoptadas a lo largo del desarrollo del proyecto, justificadas desde un enfoque profesional y pragmático.

## 1. Lenguaje y versión

- **Python 3.12.4** fue elegido por su madurez, compatibilidad con librerías modernas y mejoras en rendimiento y tipado.
- Se evitó el uso de frameworks innecesarios, favoreciendo un enfoque simple y controlado.

## 2. Librerías seleccionadas

- **yfinance**: Para obtener datos financieros históricos y en tiempo real de forma sencilla y gratuita.
- **pandas**: Estándar para la manipulación de datos tabulares.
- **requests**: Para posibles integraciones adicionales basadas en HTTP.
- **pytest**: Como base para el desarrollo de tests unitarios.

## 3. Gestión de logs

- Se configuró la librería `logging` para registrar únicamente mensajes a partir de nivel `INFO`, reduciendo así el ruido innecesario en consola.
- Se desactivaron los logs `DEBUG` provenientes de dependencias externas, como `yfinance`, que podían entorpecer la legibilidad.

## 4. Organización modular

- El sistema se organizó en tres grandes módulos (`market_loader`, `analyzer`, `display`) para reflejar un flujo de datos claro: entrada → procesamiento → salida.
- Esta decisión permite aislar errores y probar cada parte del flujo de forma más sencilla.

## 5. Control de errores y robustez

- Se integró control de excepciones en los puntos críticos de red para evitar caídas por errores externos (e.g., fallos SSL, red o datos corruptos).
- Se optó por continuar el análisis aunque ciertos tickers fallen, priorizando la robustez sobre la precisión absoluta.

## 6. Compatibilidad y mantenibilidad

- Se establecieron versiones específicas en `requirements.txt` para garantizar entornos reproducibles.
- Se evitó el uso de features o dependencias que no fueran compatibles con Python 3.12.

## 7. Reproducibilidad

- Se documentó claramente el proceso de instalación y ejecución en el `README.md`.
- Se prevé la futura integración de notebooks de validación y testeo.

## 8. Futuras decisiones

- Migración opcional a un enfoque OOP para los analizadores y displayers si se requiere mayor extensibilidad.
- Posible integración con bases de datos o almacenamiento local para cachear resultados y optimizar tiempos de análisis.
