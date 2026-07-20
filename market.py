import streamlit as st
import numpy as np
import pandas as pd

from config import (
    MARKET_SCENARIOS,
    TRANSACTION_COST,
    NUM_ITERATIONS
)

from calculations import (
    portfolio_return,
    portfolio_turnover,
    transaction_cost
)


def market_page():

    st.header("📈 Market Simulation")

    # ----------------------------------
    # Stop if game is over
    # ----------------------------------

    if st.session_state.game_finished:

        st.success("Simulation Finished")

        return

    # ----------------------------------
    # Check iteration limit
    # ----------------------------------

    if st.session_state.iteration > NUM_ITERATIONS:

        st.success("Maximum iterations completed.")

        return

    # ----------------------------------
    # Check teacher lock
    # ----------------------------------

    if st.session_state.market_locked:

        st.warning(
            "Market is paused by the teacher."
        )

        return

    st.subheader(
        f"Iteration {st.session_state.iteration}"
    )

    if not st.button("🎲 Run Market"):

        return

    # ----------------------------------
    # Select random market scenario
    # ----------------------------------

    scenario = np.random.choice(
        list(MARKET_SCENARIOS.keys())
    )

    market = MARKET_SCENARIOS[scenario]

    st.session_state.current_market = scenario

    st.success(
        f"Market Scenario : {scenario}"
    )

    # ----------------------------------
    # Display Market Returns
    # ----------------------------------

    market_rows = []

    for asset, values in market.items():

        price = values["price"]

        income = values["income"]

        total = price + income

        market_rows.append({

            "Asset": asset,

            "Price Return %":
            round(price * 100, 2),

            "Income Return %":
            round(income * 100, 2),

            "Total Return %":
            round(total * 100, 2)

        })

    market_df = pd.DataFrame(market_rows)

    st.dataframe(
        market_df,
        use_container_width=True,
        hide_index=True
    )

        # ----------------------------------
    # Process Each Team
    # ----------------------------------

    for team in st.session_state.team_names:

        allocation = st.session_state.allocations[team]

        previous = st.session_state.previous_allocations[team]

        current_value = st.session_state.portfolio_value[team]

        # ----------------------------------
        # Portfolio Returns
        # ----------------------------------

        capital_return, income_return, total_return = portfolio_return(
            allocation,
            market
        )

        # ----------------------------------
        # Portfolio Turnover
        # ----------------------------------

        turnover = portfolio_turnover(
            previous,
            allocation
        )

        # ----------------------------------
        # Transaction Cost
        # ----------------------------------

        cost = transaction_cost(
            current_value,
            turnover,
            TRANSACTION_COST
        )

        # ----------------------------------
        # Capital Gain
        # ----------------------------------

        capital_gain = current_value * capital_return

        # ----------------------------------
        # Dividend / Interest Income
        # ----------------------------------

        investment_income = current_value * income_return

        # ----------------------------------
        # New Portfolio Value
        # ----------------------------------

        new_value = (
            current_value
            + capital_gain
            + investment_income
            - cost
        )

        # ----------------------------------
        # Update Session State
        # ----------------------------------

        st.session_state.portfolio_value[team] = new_value

        st.session_state.value_history[team].append(
            new_value
        )

        st.session_state.returns_history[team].append(
            total_return
        )

        st.session_state.transaction_cost_history[team].append(
            cost
        )

        st.session_state.turnover_history[team].append(
            turnover
        )

        st.session_state.previous_allocations[team] = allocation.copy()

        # ----------------------------------
        # Store Results
        # ----------------------------------

        results.append({

            "Team": team,

            "Capital Gain (₹)":
                round(capital_gain, 2),

            "Investment Income (₹)":
                round(investment_income, 2),

            "Capital Return %":
                round(capital_return * 100, 2),

            "Income Return %":
                round(income_return * 100, 2),

            "Total Return %":
                round(total_return * 100, 2),

            "Turnover %":
                round(turnover, 2),

            "Transaction Cost (₹)":
                round(cost, 2),

            "Portfolio Value (₹)":
                round(new_value, 2)

        })

        # ----------------------------------
    # Save Market History
    # ----------------------------------

    st.session_state.market_history.append({

        "Iteration": st.session_state.iteration,

        "Scenario": scenario,

        "Market Returns": market

    })

    # ----------------------------------
    # Results DataFrame
    # ----------------------------------

    result_df = pd.DataFrame(results)

    st.subheader("📋 Iteration Results")

    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True
    )

    # ----------------------------------
    # Portfolio Ranking
    # ----------------------------------

    ranking_df = result_df[
        ["Team", "Portfolio Value (₹)"]
    ].copy()

    ranking_df = ranking_df.sort_values(
        by="Portfolio Value (₹)",
        ascending=False
    )

    ranking_df.insert(
        0,
        "Rank",
        range(1, len(ranking_df) + 1)
    )

    st.subheader("🏆 Current Ranking")

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

    # ----------------------------------
    # Show Current Leader
    # ----------------------------------

    leader = ranking_df.iloc[0]

    st.success(

        f"""
🏆 Current Leader

Team : {leader['Team']}

Portfolio Value : ₹{leader['Portfolio Value (₹)']:,.2f}
"""

    )

    # ----------------------------------
    # Move to Next Iteration
    # ----------------------------------

    st.session_state.iteration += 1

    # ----------------------------------
    # Class Summary
    # ----------------------------------

    st.subheader("📊 Portfolio Summary")

    summary = []

    for team in st.session_state.team_names:

        summary.append({

            "Team": team,

            "Portfolio Value (₹)":
                round(
                    st.session_state.portfolio_value[team],
                    2
                ),

            "Total Transaction Cost (₹)":
                round(
                    sum(
                        st.session_state.transaction_cost_history[team]
                    ),
                    2
                ),

            "Average Return %":
                round(
                    np.mean(
                        st.session_state.returns_history[team]
                    ) * 100,
                    2
                ) if len(
                    st.session_state.returns_history[team]
                ) > 0 else 0

        })

    summary_df = pd.DataFrame(summary)

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

    # ----------------------------------
    # Download Results
    # ----------------------------------

    csv = summary_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Portfolio Summary",
        data=csv,
        file_name="portfolio_summary.csv",
        mime="text/csv"
    )

    # ----------------------------------
    # Simulation Complete
    # ----------------------------------

    if st.session_state.iteration > NUM_ITERATIONS:

        st.balloons()

        st.success(
            "🎉 Portfolio Simulation Completed!"
        )

        winner = summary_df.sort_values(
            by="Portfolio Value (₹)",
            ascending=False
        ).iloc[0]

        st.markdown("## 🏆 Final Winner")

        st.metric(
            label=winner["Team"],
            value=f"₹{winner['Portfolio Value (₹)']:,.2f}"
        )

        st.info(
            "Go to the Dashboard tab to analyse CAGR, Risk, Sharpe Ratio, and performance charts."
        )

    results = []
