import numpy as np


# -----------------------------------------------------
# Portfolio Return
# -----------------------------------------------------

def portfolio_return(allocation, market_return):

    r = 0

    for asset in allocation:

        r += (
            allocation[asset] / 100
        ) * market_return[asset]

    return r


# -----------------------------------------------------
# Portfolio Turnover
# -----------------------------------------------------

def portfolio_turnover(old_alloc, new_alloc):

    turnover = 0

    for asset in old_alloc:

        turnover += abs(
            new_alloc[asset] -
            old_alloc[asset]
        )

    return turnover / 2


# -----------------------------------------------------
# Transaction Cost
# -----------------------------------------------------

def transaction_cost(
        portfolio_value,
        turnover,
        transaction_rate):

    traded_amount = (
        portfolio_value *
        turnover / 100
    )

    return traded_amount * transaction_rate


# -----------------------------------------------------
# CAGR
# -----------------------------------------------------

def cagr(
        initial_value,
        final_value,
        periods):

    if periods <= 0:
        return 0

    return (
        final_value / initial_value
    ) ** (1 / periods) - 1


# -----------------------------------------------------
# Annualized Volatility
# -----------------------------------------------------

def volatility(returns):

    if len(returns) < 2:
        return 0

    return np.std(
        returns,
        ddof=1
    ) * np.sqrt(len(returns))


# -----------------------------------------------------
# Average Return
# -----------------------------------------------------

def average_return(returns):

    if len(returns) == 0:
        return 0

    return np.mean(returns)


# -----------------------------------------------------
# Sharpe Ratio
# -----------------------------------------------------

def sharpe_ratio(
        returns,
        risk_free_rate):

    if len(returns) < 2:
        return 0

    avg = average_return(returns)

    vol = volatility(returns)

    if vol == 0:
        return 0

    return (
        avg -
        risk_free_rate / len(returns)
    ) / vol


# -----------------------------------------------------
# Maximum Drawdown
# -----------------------------------------------------

def max_drawdown(values):

    values = np.array(values)

    peak = values[0]

    drawdown = 0

    for v in values:

        if v > peak:
            peak = v

        dd = (peak - v) / peak

        if dd > drawdown:
            drawdown = dd

    return drawdown


# -----------------------------------------------------
# Total Return
# -----------------------------------------------------

def total_return(
        initial_value,
        final_value):

    return (
        final_value /
        initial_value
    ) - 1


# -----------------------------------------------------
# Portfolio Statistics
# -----------------------------------------------------

def portfolio_statistics(
        initial_value,
        current_value,
        returns,
        risk_free_rate,
        periods):

    return {

        "Current Value": current_value,

        "Total Return":
        total_return(
            initial_value,
            current_value
        ),

        "CAGR":
        cagr(
            initial_value,
            current_value,
            periods
        ),

        "Risk":
        volatility(
            returns
        ),

        "Average Return":
        average_return(
            returns
        ),

        "Sharpe":
        sharpe_ratio(
            returns,
            risk_free_rate
        ),

        "Max Drawdown":
        max_drawdown(
            [initial_value] +
            list(np.cumprod(
                np.array(returns) + 1
            ) * initial_value)
        )

    }
