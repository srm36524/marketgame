import streamlit as st

from config import (
    PAGE_TITLE,
    PAGE_ICON,
    LAYOUT
)

from session import initialize_session
from allocation import allocation_page
from market import market_page
from dashboard import dashboard_page
from teacher import teacher_page


# ----------------------------------------------------
# Streamlit Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# ----------------------------------------------------
# Initialize Session
# ----------------------------------------------------

initialize_session()

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("📈 Portfolio Management Classroom Simulator")

st.markdown("""
Simulate portfolio management across multiple market conditions.

**Features**
- 5 Teams
- 10 Market Iterations
- Equity, Bonds, Gold & Cash
- Dividends & Interest Income
- Transaction Costs
- CAGR, Risk & Sharpe Ratio
- Teacher Controls
""")

st.divider()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.header("Simulation Status")

    st.metric(
        "Current Iteration",
        st.session_state.iteration
    )

    st.metric(
        "Maximum Iterations",
        st.session_state.max_iterations
    )

    st.metric(
        "Initial Capital",
        f"₹{st.session_state.initial_capital:,.0f}"
    )

    st.metric(
        "Teams",
        len(st.session_state.team_names)
    )

    if st.session_state.current_market is not None:
        st.info(
            f"Last Market Event\n\n{st.session_state.current_market}"
        )

# ----------------------------------------------------
# Tabs
# ----------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📂 Portfolio Allocation",
        "📈 Market Simulation",
        "📊 Dashboard",
        "👨‍🏫 Teacher Controls"
    ]
)

with tab1:
    allocation_page()

with tab2:
    market_page()

with tab3:
    dashboard_page()

with tab4:
    teacher_page()

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.divider()

st.caption(
    "Portfolio Management Classroom Simulator | Version 2.0"
)
