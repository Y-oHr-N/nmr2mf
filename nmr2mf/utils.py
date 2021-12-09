"""Utilities."""

import ccxt
import numerapi


def _convert_btc_to_jpy(btc: float) -> float:
    bitflyer = ccxt.bitflyer()
    ticker = bitflyer.fetch_ticker("BTC/JPY")

    return btc * float(ticker["bid"])


def _convert_nmr_to_btc(nmr: float) -> float:
    binance = ccxt.binance()
    ticker = binance.fetch_ticker("NMR/BTC")

    return nmr * float(ticker["bid"])


def get_stake() -> float:
    """Get the current total stake amount."""
    api = numerapi.NumerAPI()
    models = api.get_models()
    stake = 0.0

    for model in models:
        try:
            stake += float(api.stake_get(model))
        except IndexError:
            pass

    stake = _convert_nmr_to_btc(stake)

    return _convert_btc_to_jpy(stake)
