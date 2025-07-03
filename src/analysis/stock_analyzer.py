import logging
from typing import List, Dict
import yfinance as yf
import numpy as np
import logging
from typing import List, Dict

def analyze_stocks(symbols: List[str]) -> Dict[str, float]:

    results = []
    logging.info(f"Iniciando análisis de {len(symbols)} acciones del SP500...")

    for i, symbol in enumerate(symbols, start=1):
        logging.debug(f"Analizando acción {i}/{len(symbols)}: {symbol}")
        index_value = calculate_cheap_value_price_stock(symbol)
        logging.debug(f"Resultado cheap_value_index para {symbol}: {index_value}")
        results.append((symbol, index_value))  # usamos tupla

    # Ordenar por valor, de mayor a menor
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

    # Limitar a top 50 y construir diccionario final
    dict_top_50 = dict(sorted_results[:50])

    logging.info(f"Retornando top {len(dict_top_50)} acciones según cheap_value_index.")
    return dict_top_50

def calculate_cheap_value_price_stock(symbol: str) -> float:
    """
    Calcula un índice compuesto de valoración para una acción dado su símbolo de mercado.
    Este índice estima si una acción está 'barata' usando múltiplos financieros y rentabilidad.

    Parámetros:
        symbol (str): Ticker de la acción (ej. 'AAPL', 'TSL', 'MSFT')

    Retorna:
        float: cheap_value_index (mayor es mejor, >1 idealmente atractivo)
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        # Métricas clave
        pe_ratio = info.get("trailingPE", np.nan)
        forward_pe = info.get("forwardPE", np.nan)
        ev_to_ebitda = info.get("enterpriseToEbitda", np.nan)
        profit_margin = info.get("profitMargins", np.nan)
        debt_to_equity = info.get("debtToEquity", np.nan)
        market_cap = info.get("marketCap", np.nan)

        # Validar valores
        if np.isnan(pe_ratio) or pe_ratio <= 0: pe_ratio = 30
        if np.isnan(forward_pe) or forward_pe <= 0: forward_pe = 25
        if np.isnan(ev_to_ebitda) or ev_to_ebitda <= 0: ev_to_ebitda = 15
        if np.isnan(profit_margin): profit_margin = 0.05
        if np.isnan(debt_to_equity) or debt_to_equity <= 0: debt_to_equity = 100
        if np.isnan(market_cap): market_cap = 1e9  # 1B default

        # Ponderación de criterios (puedes ajustar)
        normalized_pe = 1 / pe_ratio
        normalized_forward_pe = 1 / forward_pe
        normalized_ev_ebitda = 1 / ev_to_ebitda
        normalized_profit_margin = profit_margin
        normalized_debt_ratio = 1 / (1 + debt_to_equity / 100)  # penaliza deuda

        # Índice compuesto (ponderación arbitraria basada en importancia)
        cheap_value_index = (
            0.25 * normalized_pe +
            0.20 * normalized_forward_pe +
            0.20 * normalized_ev_ebitda +
            0.25 * normalized_profit_margin +
            0.10 * normalized_debt_ratio
        )

        return round(cheap_value_index, 5)

    except Exception as e:
        print(f"Ha ocurrido un error analizando {symbol}: {e}")
        return 0.0
