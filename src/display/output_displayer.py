from typing import Dict

def display_classification_report(stock_data: Dict[str, float]) -> None:
    """
    Muestra en consola una lista con el símbolo, cheap_value_index y enlace a Yahoo Finance.

    Args:
        stock_data (Dict[str, float]): Diccionario con símbolos como claves y cheap_value_index como valores.
    """
    base_url = "https://finance.yahoo.com/quote/"

    print(f"{'Símbolo':<12} | {'Cheap Value Index':<18} | Enlace Yahoo Finance")
    print("-" * 75)

    for symbol, index_val in stock_data.items():
        url = f"{base_url}{symbol.replace('-', '.')}"
        print(f"{symbol:<12} | {index_val:<18.5f} | {url}")
