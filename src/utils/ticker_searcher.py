import pandas as pd

def get_tickers_by_market(market: str) -> list:
    """
    Retorna una lista de símbolos bursátiles según el mercado indicado.
    :param market: uno de "SP500", "EuroStoxx50", "Asia"
    """
    market = market.strip().upper()

    if market == "SP500":
        return _get_sp500_tickers()
    elif market == "EUROSTOXX50":
        return _get_eurostoxx50_tickers()
    elif market == "ASIA":
        return _get_asia_ex_japan_tickers()
    else:
        raise ValueError("Mercado no reconocido. Usa: 'SP500', 'EuroStoxx50' o 'Asia'.")

def _get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    return tables[0]["Symbol"].str.replace(".", "-", regex=False).tolist()

def _get_eurostoxx50_tickers():
    """
    Extrae los 50 tickers del Euro Stoxx 50 desde su sección Composition en Wikipedia.
    """
    url = "https://en.wikipedia.org/wiki/EURO_STOXX_50"
    tables = pd.read_html(url)

    # Buscar tabla que contiene la columna "Ticker"
    ticker_table = None
    for df in tables:
        if "Ticker" in df.columns:
            ticker_table = df
            break

    if ticker_table is None:
        raise RuntimeError("No se encontró la tabla con columna 'Ticker' en Wikipedia.")

    # Extraer los tickers
    tickers = ticker_table["Ticker"].tolist()
    # Sustituir puntos por guion para compatibilidad con yfinance
    tickers = [t.replace(".", "-") for t in tickers]
    return tickers

def _get_asia_ex_japan_tickers():
    """
    Extrae los 50 tickers de las principales empresas de Asia (ex Japón)
    basadas en MSCI Asia APEX 50 desde Wikipedia francesa.
    """
    url = "https://fr.wikipedia.org/wiki/MSCI_Asie_APEX_50"
    tables = pd.read_html(url)

    # La tabla que nos interesa contiene columnas 'Code' y 'Société'
    df = None
    for table in tables:
        if 'Code' in table.columns and 'Société' in table.columns:
            df = table
            break

    if df is None:
        raise RuntimeError("No se encontró la tabla 'MSCI Asie APEX 50' con columna 'Code'.")

    # Extraer los códigos, limpiando espacios
    codes = df['Code'].astype(str).str.strip().tolist()
    # Sustituir espacios y normalizar (ej. '1299 HK' → '1299.HK')
    tickers = [c.replace(' ', '.') for c in codes]
    return tickers