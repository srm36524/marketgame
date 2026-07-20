import numpy as np


# =========================================================
# Portfolio Return
# Returns:
#   capital_return
#   income_return
#   total_return
# =========================================================

def portfolio_return(allocation, market_return):

    capital_return = 0
    income_return = 0

    for asset in allocation:

        weight = allocation[asset] / 100

        capital_return += (
            weight *
            market_return[asset]["price"]
        )

        income_return += (
            weight *
            market_return[asset]["income"]
        )

    total_return = capital_return + income_return

    return capital_return, income_return, total_return


# =========================================================
# Portfolio Turnover
# =========================================================

def portfolio_turnover(old_alloc, new_alloc):

    turnover = 0

    for asset in old_alloc:

        turnover += abs(
            new_alloc[asset] -
            old_alloc[asset]
        )

    return turnover / 2


# =========================================================
# Transaction Cost
# =========================================================

def transaction_cost(
        portfolio_value,
        turnover,
        transaction_rate):

    traded_amount = (
        portfolio_value *
        turnover / 100
    )

    return traded_amount * transaction_rate


# =========================================================
# CAGR
# =========================================================

def cagr(initial, final, periods):

    if periods <= 0:
        return 0

    return (
        (final / initial) ** (1 / periods)
    ) - 1


# =========================================================
# Total Return
# =========================================================

def total_return(initial, final):

    return (
        final / initial
    ) - 1


# =========================================================
# Volatility
# =========================================================

def volatility(returns):

    if len(returns) < 2:
        return 0

    return np.std(
        returns,
        ddof=1
    ) * np.sqrt(len(returns))


# =========================================================
# Average Return
# =========================================================

def average_return(returns):

    if len(returns) == 0:
        return 0

    return np.mean(returns)


# =========================================================
# Sharpe Ratio
# =========================================================

def sharpe_ratio(
        returns,
        risk_free_rate):

    if len(returns) < 2:
        return 0

    vol = volatility(returns)

    if vol == 0:
        return 0

    avg = average_return(returns)

    return (
        avg -
        risk_free_rate / len(returns)
    ) / vol


# =========================================================
# Maximum Drawdown
# =========================================================

def max_drawdown(values):

    if len(values) == 0:
        return 0

    peak = values[0]
    max_dd = 0

    for value in values:

        if value > peak:
            peak = value

        dd = (peak - value) / peak

        if dd > max_dd:
            max_dd = dd

    return max_dd


# =========================================================
# Portfolio Statistics
# =========================================================

def portfolio_statistics(
        initial_value,
        current_value,
        returns,
        risk_free_rate,
        periods,
        value_history):

    stats = {}

    stats["Current Value"] = current_value

    stats["Total Return"] = total_return(
        initial_value,
        current_value
    )

    stats["CAGR"] = cagr(
        initial_value,
        current_value,
        periods
    )

    stats["Risk"] = volatility(
        returns
    )

    stats["Average Return"] = average_return(
        returns
    )

    stats["Sharpe"] = sharpe_ratio(
        returns,
        risk_free_rate
    )

    stats["Max Drawdown"] = max_drawdown(
        value_history
    )

    return stats
