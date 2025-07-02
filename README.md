# ScrapingFinancialMarket
Recoge las empresas a mejor precio según el mercado de valores mediante scraping web

Este proyecto solo sigue fines educativos y surge de la curiosidad de generar una herramienta que combine el mundo de las finanzas con el scraping web. En ningun caso es una recomendación de inversión. De igual modo, los datos son fiables y recogidos en tiempo real cuando se ejecute el script que contiene el core del proyecto.

## Métricas a considerar
* Indicador |  Descripción  |  Interpretación
* Market Cap |  Valor de capitalización busátil | Mide el tamaño de la empresa
* Enterprise Value  |  Valor total de la empresa (Incluyendo deuda)  |  La deuda se calcula con la diferencia de EV con respecto al market cap
* Profit Margin  |  Margen de beneficios generados  |  Mide la solvencia de la empresa en términos monetarios
* EBITDA  |  Beneficio bruto operativo  |  A mayor EBITDA, mayor potencial en la acción

## Entorno técnico empleado para este proyecto
* Python 3.11
* Librerías scraping, financias y cálculos mat.: requests, BeatifulSoup, yfinance, pandas

## Estructura del proyecto
FinancialMarketsAnalysis/
├── README.md
├── requirements.txt
├── main.py
├── scraper/
│   └── yahoo_scraper.py
├── analysis/
│   └── analyzer.py
└── data/
    └── tickers_sp500.csv
    └── tickers_euroStock50.csv
    └── tickers_ICEAsia.csv
