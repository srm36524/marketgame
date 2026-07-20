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

    st.header("Market Simulation")

    # ------------------------------
    # Stop if game finished
    # ------------------------------

    if st.session_state.game_finished:

        st.success("Simulation Finished")

        return

    # ------------------------------
    # Maximum iterations reached
    # ------------------------------

    if st.session_state.iteration > NUM_ITERATIONS:

        st.success("Maximum Iterations Completed")

        return

    # ------------------------------
    # Market Locked
    # ------------------------------

    if st.session_state.market_locked:

        st.warning(
            "Market is currently paused by the teacher."
        )

        return

    st.write(
        f"### Iteration {st.session_state.iteration}"
    )

    # ------------------------------
    # Generate Market
    # ------------------------------

    if st.button("Run Market"):

        scenario = np.random.choice(
            list(MARKET_SCENARIOS.keys())
        )

        market = MARKET_SCENARIOS[scenario]

        st.session_state.current_market = scenario

        st.subheader(
            f"Scenario : {scenario}"
        )

market_rows = []

for asset, values in market.items():

    price = values["price"]

    income = values["income"]

    total = price + income

    market_rows.append({

        "Asset": asset,

        "Price Return %": round(price * 100, 2),

        "Income %": round(income * 100, 2),

        "Total Return %": round(total * 100, 2)

    })

market_df = pd.DataFrame(market_rows)

        st.dataframe(
            market_df,
            use_container_width=True,
            hide_index=True
        )

        results=[]

        # ------------------------------
        # Process each Team
        # ------------------------------

        for team in st.session_state.team_names:

            allocation = st.session_state.allocations[team]

            previous = st.session_state.previous_allocations[team]

            current_value = st.session_state.portfolio_value[team]

            # Portfolio Return

            p_return = portfolio_return(
                allocation,
                market
            )

            # Turnover

            turnover = portfolio_turnover(
                previous,
                allocation
            )

            # Transaction Cost

            cost = transaction_cost(
                current_value,
                turnover,
                TRANSACTION_COST
            )

            # New Portfolio Value

            new_value = (
                current_value *
                (1+p_return)
            ) - cost

            # Save Values

            st.session_state.portfolio_value[
                team
            ] = new_value

            st.session_state.value_history[
                team
            ].append(new_value)

            st.session_state.returns_history[
                team
            ].append(p_return)

            st.session_state.transaction_cost_history[
                team
            ].append(cost)

            st.session_state.turnover_history[
                team
            ].append(turnover)

            st.session_state.previous_allocations[
                team
            ] = allocation.copy()

            results.append({

                "Team":team,

                "Portfolio Return %":
                round(
                    p_return*100,
                    2
                ),

                "Turnover %":
                round(
                    turnover,
                    2
                ),

                "Transaction Cost":
                round(
                    cost,
                    2
                ),

                "Portfolio Value":
                round(
                    new_value,
                    2
                )

            })

        # ------------------------------
        # Save Market History
        # ------------------------------

        st.session_state.market_history.append({

            "Iteration":
            st.session_state.iteration,

            "Scenario":
            scenario,

            "Returns":
            market

        })

        # ------------------------------
        # Increase Iteration
        # ------------------------------

        st.session_state.iteration += 1

        # ------------------------------
        # Display Results
        # ------------------------------

        st.subheader("Iteration Results")

        result_df = pd.DataFrame(results)

        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )

        st.success(
            "Iteration Completed Successfully"
        )
