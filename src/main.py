import sys
import os
import logging

# Agregar el directorio src al path para importaciones absolutas
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from market_loader.ticker_searcher import get_tickers_by_market
from analysis.stock_analyzer import analyze_stocks
from display.output_displayer import display_classification_report

# Configura solo tus logs a INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Silencia DEBUG de librerías de terceros
for lib in ['yfinance', 'urllib3', 'requests']:
    logging.getLogger(lib).setLevel(logging.WARNING)


if __name__ == "__main__":
    market_name: str = "SP500"
    symbols = get_tickers_by_market(market_name)
    top_stocks = analyze_stocks(symbols)
    for idx, (symbol, index_value) in enumerate(top_stocks.items(), start=1):
        print(f"{idx}. {symbol:8} -> cheap_value_index: {index_value}")
    display_classification_report(top_stocks)
