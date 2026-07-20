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
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

st.title("📈 Portfolio Management Classroom Simulator")

st.markdown("---")


# ----------------------------------------------------
# Initialize Session State
# ----------------------------------------------------

initialize_session()


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("Simulation")

st.sidebar.success(
    f"Iteration : "
    f"{st.session_state.iteration}"
)

st.sidebar.info(
    f"Teams : "
    f"{len(st.session_state.team_names)}"
)

st.sidebar.info(
    f"Initial Capital : "
    f"₹{st.session_state.initial_capital:,.0f}"
)


# ----------------------------------------------------
# Tabs
# ----------------------------------------------------

tabs = st.tabs([
    "Portfolio Allocation",
    "Market",
    "Dashboard",
    "Teacher Controls"
])


# ----------------------------------------------------
# Allocation Page
# ----------------------------------------------------

with tabs[0]:

    allocation_page()


# ----------------------------------------------------
# Market Page
# ----------------------------------------------------

with tabs[1]:

    market_page()


# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

with tabs[2]:

    dashboard_page()


# ----------------------------------------------------
# Teacher
# ----------------------------------------------------

with tabs[3]:

    teacher_page()
