import numpy as np


# ==========================================================
# PORTFOLIO RETURN
# ==========================================================

def portfolio_return(allocation, market):

    capital_return = 0.0
    income_return = 0.0

    for asset, weight in allocation.items():

        w = weight / 100

        capital_return += (
            w * market[asset]["price"]
        )

        income_return += (
            w * market[asset]["income"]
        )

    total_return = (
        capital_return +
        income_return
    )

    return (
        capital_return,
        income_return,
        total_return
    )


# ==========================================================
# PORTFOLIO TURNOVER
# ==========================================================

def portfolio_turnover(
        previous,
        current):

    turnover = 0

    for asset in previous:

        turnover += abs(
            current[asset] -
            previous[asset]
        )

    return turnover / 2


# ==========================================================
# TRANSACTION COST
# ==========================================================

def transaction_cost(
        portfolio_value,
        turnover,
        rate):

    traded_amount = (
        portfolio_value *
        turnover / 100
    )

    return traded_amount * rate


# ==========================================================
# TOTAL RETURN
# ==========================================================

def total_return(
        initial,
        current):

    return (
        current -
        initial
    ) / initial


# ==========================================================
# CAGR
# ==========================================================

def cagr(
        initial,
        current,
        periods):

    if periods <= 0:

        return 0

    return (
        (current / initial)
        ** (1 / periods)
    ) - 1


# ==========================================================
# VOLATILITY
# ==========================================================

def volatility(returns):

    if len(returns) < 2:

        return 0

    return np.std(
        returns,
        ddof=1
    )


# ==========================================================
# SHARPE RATIO
# ==========================================================

def sharpe_ratio(
        returns,
        risk_free_rate):

    if len(returns) < 2:

        return 0

    avg = np.mean(returns)

    risk = volatility(returns)

    if risk == 0:

        return 0

    return (
        avg -
        risk_free_rate
    ) / risk


# ==========================================================
# MAXIMUM DRAWDOWN
# ==========================================================

def max_drawdown(values):

    peak = values[0]

    max_dd = 0

    for value in values:

        if value > peak:

            peak = value

        dd = (
            peak -
            value
        ) / peak

        if dd > max_dd:

            max_dd = dd

    return max_dd


# ==========================================================
# PORTFOLIO STATISTICS
# ==========================================================

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

    stats["Sharpe"] = sharpe_ratio(
        returns,
        risk_free_rate
    )

    stats["Max Drawdown"] = max_drawdown(
        value_history
    )

    return stats


# ==========================================================
# WINNING TEAM
# ==========================================================

def winner(portfolio_values):

    return max(
        portfolio_values,
        key=portfolio_values.get
    )


# ==========================================================
# AVERAGE RETURN
# ==========================================================

def average_return(returns):

    if len(returns) == 0:

        return 0

    return np.mean(returns)


# ==========================================================
# TOTAL TRANSACTION COST
# ==========================================================

def total_transaction_cost(costs):

    return sum(costs)


# ==========================================================
# TOTAL INVESTMENT INCOME
# ==========================================================

def total_income(returns, capital):

    income = 0

    for r in returns:

        income += capital * r

    return income
