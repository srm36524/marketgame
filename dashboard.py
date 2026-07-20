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


    # --------------------------------------------------
    # Check Data
    # --------------------------------------------------

    if len(st.session_state.market_history) == 0:

        st.info(
            "Run at least one market iteration to view dashboard."
        )

        return


    # --------------------------------------------------
    # Team Selection
    # --------------------------------------------------

    selected_team = st.selectbox(

        "Select Team",

        st.session_state.team_names

    )


    # --------------------------------------------------
    # Get Team Data
    # --------------------------------------------------

    values = (
        st.session_state.value_history[selected_team]
    )

    returns = (
        st.session_state.returns_history[selected_team]
    )


    # --------------------------------------------------
    # Portfolio Statistics
    # --------------------------------------------------

    stats = portfolio_statistics(

        INITIAL_CAPITAL,

        st.session_state.portfolio_value[selected_team],

        returns,

        RISK_FREE_RATE,

        len(returns),

        values

    )


    # --------------------------------------------------
    # KPI Cards
    # --------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)


    c1.metric(

        "Portfolio Value",

        f"₹{stats['Current Value']:,.0f}"

    )


    c2.metric(

        "CAGR",

        f"{stats['CAGR']*100:.2f}%"

    )


    c3.metric(

        "Risk",

        f"{stats['Risk']*100:.2f}%"

    )


    c4.metric(

        "Sharpe Ratio",

        f"{stats['Sharpe']:.2f}"

    )


    st.divider()


    # --------------------------------------------------
    # Portfolio Growth Chart
    # --------------------------------------------------

    st.subheader(
        "Portfolio Growth"
    )


    growth_df = pd.DataFrame({

        "Iteration":
            range(len(values)),

        "Value":
            values

    })


    fig = px.line(

        growth_df,

        x="Iteration",

        y="Value",

        markers=True,

        title="Portfolio Value Over Time"

    )


    st.plotly_chart(

        fig,

        use_container_width=True

    )


    # --------------------------------------------------
    # Return Analysis
    # --------------------------------------------------

    st.subheader(
        "Return Analysis"
    )


    return_df = pd.DataFrame({

        "Iteration":
            range(1, len(returns)+1),

        "Return %":
            [r*100 for r in returns]

    })


    fig2 = px.bar(

        return_df,

        x="Iteration",

        y="Return %",

        title="Iteration-wise Returns"

    )


    st.plotly_chart(

        fig2,

        use_container_width=True

    )


    # --------------------------------------------------
    # All Teams Comparison
    # --------------------------------------------------

    st.subheader(
        "🏆 Team Comparison"
    )


    comparison = []


    for team in st.session_state.team_names:

        comparison.append({

            "Team": team,

            "Final Value":
                st.session_state.portfolio_value[team],

            "Total Transaction Cost":
                sum(
                    st.session_state.transaction_cost_history[team]
                )

        })


    comparison_df = pd.DataFrame(comparison)


    fig3 = px.bar(

        comparison_df,

        x="Team",

        y="Final Value",

        title="Final Portfolio Value Comparison"

    )


    st.plotly_chart(

        fig3,

        use_container_width=True

    )


    st.dataframe(

        comparison_df,

        use_container_width=True,

        hide_index=True

    )
