import pandas as pd
import pandas_datareader.data as web
import datetime


def load_fred_series(series_dict, start, end):
    """
    Load multiple time series from FRED.

    Parameters:
    - series_dict: dict {name: FRED_code}
    - start: datetime
    - end: datetime

    Returns:
    - DataFrame with all series merged
    """

    data = []

    for name, code in series_dict.items():
        try:
            df = web.DataReader(code, "fred", start, end)
            df.columns = [name]
            data.append(df)
            print(f"Loaded: {name} - loaders_fred.py:26")
        except Exception as e:
            print(f"Error loading {name}: {e} - loaders_fred.py:28")

    df_final = pd.concat(data, axis=1)

    return df_final


def get_us_macro_data():
    """
    Load key US macro-financial indicators.
    """

    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2025, 1, 1)

    series = {
        # Macro
        "gdp": "GDP",
        "cpi": "CPIAUCSL",
        "unemployment": "UNRATE",

        # Monetary policy
        "fed_rate": "FEDFUNDS",

        # Market
        "sp500": "SP500",
        "vix": "VIXCLS",

        # Yield curve
        "rate_10y": "GS10",
        "rate_2y": "GS2"
    }

    df = load_fred_series(series, start, end)

    return df