import streamlit as st
import pandas as pd
import numpy as np

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

    # --------------------------------------------------
    # Check Simulation Status
    # --------------------------------------------------

    if st.session_state.game_finished:

        st.success("Simulation has already finished.")

        return

    if st.session_state.market_locked:

        st.warning(
            "The teacher has locked the market."
        )

        return

    if st.session_state.iteration > NUM_ITERATIONS:

        st.success(
            "All iterations have been completed."
        )

        st.session_state.game_finished = True

        return

    st.subheader(
        f"Iteration {st.session_state.iteration} of {NUM_ITERATIONS}"
    )

    # --------------------------------------------------
    # Run Market Button
    # --------------------------------------------------

    if not st.button(
        "🎲 Run Market"
    ):

        return

    # --------------------------------------------------
    # Select Random Scenario
    # --------------------------------------------------

    scenario = np.random.choice(
        list(MARKET_SCENARIOS.keys())
    )

    market = MARKET_SCENARIOS[scenario]

    st.session_state.current_market = scenario

    st.success(
        f"Market Scenario: {scenario}"
    )

    # --------------------------------------------------
    # Display Market Returns
    # --------------------------------------------------

    market_rows = []

    for asset, values in market.items():

        price = values["price"]

        income = values["income"]

        total = price + income

        market_rows.append({

            "Asset": asset,

            "Capital Return %":
                round(price * 100, 2),

            "Income Return %":
                round(income * 100, 2),

            "Total Return %":
                round(total * 100, 2)

        })

    market_df = pd.DataFrame(market_rows)

    st.subheader("Market Returns")

    st.dataframe(
        market_df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # Store Team Results
    # --------------------------------------------------

    results = []

    # --------------------------------------------------
    # Process Each Team
    # --------------------------------------------------

    for team in st.session_state.team_names:

        allocation = st.session_state.allocations[team]

        previous_allocation = (
            st.session_state.previous_allocations[team]
        )

        current_value = (
            st.session_state.portfolio_value[team]
        )

        # ----------------------------------------------
        # Portfolio Returns
        # ----------------------------------------------

        capital_return, income_return, total_return = (
            portfolio_return(
                allocation,
                market
            )
        )

        # ----------------------------------------------
        # Turnover
        # ----------------------------------------------

        turnover = portfolio_turnover(
            previous_allocation,
            allocation
        )

        # ----------------------------------------------
        # Transaction Cost
        # ----------------------------------------------

        cost = transaction_cost(
            current_value,
            turnover,
            TRANSACTION_COST
        )

        # ----------------------------------------------
        # Capital Gain
        # ----------------------------------------------

        capital_gain = (
            current_value *
            capital_return
        )

        # ----------------------------------------------
        # Dividend / Interest Income
        # ----------------------------------------------

        investment_income = (
            current_value *
            income_return
        )

        # ----------------------------------------------
        # Update Portfolio Value
        # ----------------------------------------------

        new_value = (
            current_value
            + capital_gain
            + investment_income
            - cost
        )

        # ----------------------------------------------
        # Save Updated Portfolio
        # ----------------------------------------------

        st.session_state.portfolio_value[
            team
        ] = new_value

        st.session_state.value_history[
            team
        ].append(new_value)

        st.session_state.returns_history[
            team
        ].append(total_return)

        st.session_state.capital_return_history[
            team
        ].append(capital_return)

        st.session_state.income_return_history[
            team
        ].append(income_return)

        st.session_state.transaction_cost_history[
            team
        ].append(cost)

        st.session_state.turnover_history[
            team
        ].append(turnover)

        st.session_state.previous_allocations[
            team
        ] = allocation.copy()

        # ----------------------------------------------
        # Store Team Result
        # ----------------------------------------------

        results.append({

            "Team": team,

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

    # --------------------------------------------------
    # Display Iteration Results
    # --------------------------------------------------

    st.subheader(
        "📊 Iteration Performance"
    )

    result_df = pd.DataFrame(results)

    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # Portfolio Ranking
    # --------------------------------------------------

    st.subheader(
        "🏆 Current Ranking"
    )

    ranking = []

    for team in st.session_state.team_names:

        ranking.append({

            "Team": team,

            "Portfolio Value (₹)":
                st.session_state.portfolio_value[team]

        })


    ranking_df = pd.DataFrame(ranking)


    ranking_df = ranking_df.sort_values(
        by="Portfolio Value (₹)",
        ascending=False
    )


    ranking_df.insert(
        0,
        "Rank",
        range(
            1,
            len(ranking_df) + 1
        )
    )


    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # Current Leader
    # --------------------------------------------------

    leader = ranking_df.iloc[0]


    st.success(
        f"""
🏆 Current Leader

Team: {leader['Team']}

Portfolio Value:
₹{leader['Portfolio Value (₹)']:,.2f}
"""
    )


    # --------------------------------------------------
    # Save Market History
    # --------------------------------------------------

    st.session_state.market_history.append({

        "Iteration":
            st.session_state.iteration,

        "Scenario":
            scenario,

        "Market Data":
            market

    })


    # --------------------------------------------------
    # Increase Iteration
    # --------------------------------------------------

    st.session_state.iteration += 1

    # --------------------------------------------------
    # Final Summary
    # --------------------------------------------------

    st.subheader(
        "📈 Simulation Summary"
    )


    summary = []


    for team in st.session_state.team_names:

        values = (
            st.session_state.value_history[team]
        )

        total_cost = sum(
            st.session_state.transaction_cost_history[team]
        )

        total_income = sum(
            st.session_state.income_return_history[team]
        )


        summary.append({

            "Team": team,

            "Final Portfolio Value (₹)":
                round(
                    st.session_state.portfolio_value[team],
                    2
                ),

            "Total Income Return %":
                round(
                    total_income * 100,
                    2
                ),

            "Total Transaction Cost (₹)":
                round(
                    total_cost,
                    2
                )

        })


    summary_df = pd.DataFrame(summary)


    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # Download Report
    # --------------------------------------------------

    csv = summary_df.to_csv(
        index=False
    )


    st.download_button(

        label="📥 Download Simulation Report",

        data=csv,

        file_name="portfolio_simulation_report.csv",

        mime="text/csv"

    )


    # --------------------------------------------------
    # Simulation Completed
    # --------------------------------------------------

    if st.session_state.iteration > NUM_ITERATIONS:


        st.session_state.game_finished = True


        st.balloons()


        winner = summary_df.sort_values(

            by="Final Portfolio Value (₹)",

            ascending=False

        ).iloc[0]


        st.success(
            f"""
🎉 Simulation Completed!

🏆 Winner: {winner['Team']}

Final Portfolio Value:
₹{winner['Final Portfolio Value (₹)']:,.2f}
"""
        )

