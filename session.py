import streamlit as st

from config import (
    TEAM_NAMES,
    DEFAULT_ALLOCATION,
    INITIAL_CAPITAL,
    NUM_ITERATIONS
)


def initialize_session():

    # ---------------------------------------------------
    # Basic Settings
    # ---------------------------------------------------

    if "team_names" not in st.session_state:
        st.session_state.team_names = TEAM_NAMES

    if "initial_capital" not in st.session_state:
        st.session_state.initial_capital = INITIAL_CAPITAL

    if "max_iterations" not in st.session_state:
        st.session_state.max_iterations = NUM_ITERATIONS

    if "iteration" not in st.session_state:
        st.session_state.iteration = 1

    # ---------------------------------------------------
    # Portfolio Values
    # ---------------------------------------------------

    if "portfolio_value" not in st.session_state:

        st.session_state.portfolio_value = {
            team: INITIAL_CAPITAL
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Current Allocation
    # ---------------------------------------------------

    if "allocations" not in st.session_state:

        st.session_state.allocations = {
            team: DEFAULT_ALLOCATION.copy()
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Previous Allocation
    # ---------------------------------------------------

    if "previous_allocations" not in st.session_state:

        st.session_state.previous_allocations = {
            team: DEFAULT_ALLOCATION.copy()
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Returns History
    # ---------------------------------------------------

    if "returns_history" not in st.session_state:

        st.session_state.returns_history = {
            team: []
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Portfolio Value History
    # ---------------------------------------------------

    if "value_history" not in st.session_state:

        st.session_state.value_history = {
            team: [INITIAL_CAPITAL]
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Transaction Cost History
    # ---------------------------------------------------

    if "transaction_cost_history" not in st.session_state:

        st.session_state.transaction_cost_history = {
            team: []
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Turnover History
    # ---------------------------------------------------

    if "turnover_history" not in st.session_state:

        st.session_state.turnover_history = {
            team: []
            for team in TEAM_NAMES
        }

    # ---------------------------------------------------
    # Market History
    # ---------------------------------------------------

    if "market_history" not in st.session_state:

        st.session_state.market_history = []

    # ---------------------------------------------------
    # Current Market Scenario
    # ---------------------------------------------------

    if "current_market" not in st.session_state:

        st.session_state.current_market = None

    # ---------------------------------------------------
    # Teacher Controls
    # ---------------------------------------------------

    if "allocation_locked" not in st.session_state:
        st.session_state.allocation_locked = False

    if "market_locked" not in st.session_state:
        st.session_state.market_locked = False

    if "game_finished" not in st.session_state:
        st.session_state.game_finished = False

    # ---------------------------------------------------
    # Leaderboard Cache
    # ---------------------------------------------------

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = None
