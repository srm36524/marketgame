import streamlit as st
import pandas as pd
import plotly.express as px

from config import (
    INITIAL_CAPITAL,
    RISK_FREE_RATE
)

from calculations import (
    portfolio_statistics
)


def dashboard_page():

    st.header("📊 Portfolio Dashboard")

    dashboard = []

    # ----------------------------------------
    # Calculate Statistics
    # ----------------------------------------

    periods = max(
        st.session_state.iteration - 1,
        1
    )

    for team in st.session_state.team_names:

        stats = portfolio_statistics(
            INITIAL_CAPITAL,
            current_value,
            returns,
            RISK_FREE_RATE,
            periods,
           st.session_state.value_history[team]
        )

        dashboard.append({

            "Team":team,

            "Portfolio Value":
            round(stats["Current Value"],2),

            "Total Return %":
            round(stats["Total Return"]*100,2),

            "CAGR %":
            round(stats["CAGR"]*100,2),

            "Risk %":
            round(stats["Risk"]*100,2),

            "Sharpe":
            round(stats["Sharpe"],2),

            "Max Drawdown %":
            round(stats["Max Drawdown"]*100,2)

        })

    dashboard_df = pd.DataFrame(dashboard)

    dashboard_df = dashboard_df.sort_values(
        "Portfolio Value",
        ascending=False
    )

    dashboard_df.insert(
        0,
        "Rank",
        range(
            1,
            len(dashboard_df)+1
        )
    )

    st.subheader("Leaderboard")

    st.dataframe(
        dashboard_df,
        use_container_width=True,
        hide_index=True
    )

    # ----------------------------------------
    # Portfolio Growth Chart
    # ----------------------------------------

    st.subheader("Portfolio Growth")

    growth = []

    for team in st.session_state.team_names:

        values = st.session_state.value_history[team]

        for i,v in enumerate(values):

            growth.append({

                "Iteration":i,

                "Team":team,

                "Portfolio":v

            })

    growth_df = pd.DataFrame(growth)

    fig = px.line(

        growth_df,

        x="Iteration",

        y="Portfolio",

        color="Team",

        markers=True

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ----------------------------------------
    # Risk vs Return
    # ----------------------------------------

    st.subheader("Risk vs Return")

    fig2 = px.scatter(

        dashboard_df,

        x="Risk %",

        y="CAGR %",

        text="Team",

        size="Portfolio Value",

        color="Sharpe"

    )

    fig2.update_traces(
        textposition="top center"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ----------------------------------------
    # Transaction Costs
    # ----------------------------------------

    st.subheader(
        "Transaction Cost Summary"
    )

    costs=[]

    for team in st.session_state.team_names:

        costs.append({

            "Team":team,

            "Transaction Cost":
            round(

                sum(
                    st.session_state.transaction_cost_history[
                        team
                    ]
                ),

                2

            )

        })

    cost_df = pd.DataFrame(costs)

    st.dataframe(

        cost_df,

        use_container_width=True,

        hide_index=True

    )

    # ----------------------------------------
    # Current Allocation
    # ----------------------------------------

    st.subheader("Current Allocation")

    team = st.selectbox(

        "Select Team",

        st.session_state.team_names

    )

    alloc = st.session_state.allocations[team]

    alloc_df = pd.DataFrame({

        "Asset":list(
            alloc.keys()
        ),

        "Allocation":
        list(
            alloc.values()
        )

    })

    fig3 = px.pie(

        alloc_df,

        names="Asset",

        values="Allocation"

    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # ----------------------------------------
    # Winner
    # ----------------------------------------

    winner = dashboard_df.iloc[0]

    st.success(

        f"""
🏆 Current Leader

Team : {winner['Team']}

Portfolio : ₹{winner['Portfolio Value']:,.0f}

Sharpe Ratio : {winner['Sharpe']}

CAGR : {winner['CAGR %']}%
"""

    )
