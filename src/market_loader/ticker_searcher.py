import pandas as pd

def get_tickers_by_market(market: str) -> list:
    """
    Retorna una lista de símbolos bursátiles según el mercado indicado.
    :param market: "SP500"
    """
    market = market.strip().upper()

    if market == "SP500":
        return _get_sp500_tickers()
    else:
        raise ValueError("Mercado no reconocido. Usa: 'SP500'.")

def _get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    return tables[0]["Symbol"].str.replace(".", "-", regex=False).tolist()

