if __name__ == "__main__":
    # Lista de símbolos EuroStoxx50 de ejemplo, reemplaza con tu lista real
    market_name: str = "ASIA"
    get_tickers_by_market(market_name)
    eurostoxx50_symbols = get_tickers_by_market(market_name)
    top_stocks = analyze_stocks(eurostoxx50_symbols)
    for idx, (symbol, index_value) in enumerate(top_stocks.items(), start=1):
        print(f"{idx}. {symbol:8} -> cheap_value_index: {index_value}")
    display_classification_report(top_stocks)