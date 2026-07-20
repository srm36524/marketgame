import streamlit as st

from config import (
    TEAM_NAMES,
    DEFAULT_ALLOCATION,
    INITIAL_CAPITAL,
    NUM_ITERATIONS
)


def initialize_session():

    # =====================================================
    # BASIC SETTINGS
    # =====================================================

    if "team_names" not in st.session_state:
        st.session_state.team_names = TEAM_NAMES.copy()

    if "initial_capital" not in st.session_state:
        st.session_state.initial_capital = INITIAL_CAPITAL

    if "max_iterations" not in st.session_state:
        st.session_state.max_iterations = NUM_ITERATIONS

    if "iteration" not in st.session_state:
        st.session_state.iteration = 1

    # =====================================================
    # CURRENT PORTFOLIO VALUE
    # =====================================================

    if "portfolio_value" not in st.session_state:

        st.session_state.portfolio_value = {
            team: INITIAL_CAPITAL
            for team in TEAM_NAMES
        }

    # =====================================================
    # CURRENT ALLOCATION
    # =====================================================

    if "allocations" not in st.session_state:

        st.session_state.allocations = {
            team: DEFAULT_ALLOCATION.copy()
            for team in TEAM_NAMES
        }

    # =====================================================
    # PREVIOUS ALLOCATION
    # Used for transaction cost calculation
    # =====================================================

    if "previous_allocations" not in st.session_state:

        st.session_state.previous_allocations = {
            team: DEFAULT_ALLOCATION.copy()
            for team in TEAM_NAMES
        }

    # =====================================================
    # VALUE HISTORY
    # =====================================================

    if "value_history" not in st.session_state:

        st.session_state.value_history = {
            team: [INITIAL_CAPITAL]
            for team in TEAM_NAMES
        }

    # =====================================================
    # RETURN HISTORY
    # =====================================================

    if "returns_history" not in st.session_state:

        st.session_state.returns_history = {
            team: []
            for team in TEAM_NAMES
        }

    # =====================================================
    # CAPITAL RETURN HISTORY
    # =====================================================

    if "capital_return_history" not in st.session_state:

        st.session_state.capital_return_history = {
            team: []
            for team in TEAM_NAMES
        }

    # =====================================================
    # INCOME RETURN HISTORY
    # =====================================================

    if "income_return_history" not in st.session_state:

        st.session_state.income_return_history = {
            team: []
            for team in TEAM_NAMES
        }

    # =====================================================
    # TRANSACTION COST HISTORY
    # =====================================================

    if "transaction_cost_history" not in st.session_state:

        st.session_state.transaction_cost_history = {
            team: []
            for team in TEAM_NAMES
        }

    # =====================================================
    # TURNOVER HISTORY
    # =====================================================

    if "turnover_history" not in st.session_state:

        st.session_state.turnover_history = {
            team: []
            for team in TEAM_NAMES
        }

    # =====================================================
    # MARKET HISTORY
    # =====================================================

    if "market_history" not in st.session_state:
        st.session_state.market_history = []

    if "current_market" not in st.session_state:
        st.session_state.current_market = None

    # =====================================================
    # TEACHER CONTROLS
    # =====================================================

    if "allocation_locked" not in st.session_state:
        st.session_state.allocation_locked = False

    if "market_locked" not in st.session_state:
        st.session_state.market_locked = False

    if "game_finished" not in st.session_state:
        st.session_state.game_finished = False

    # =====================================================
    # CLASS LEADERBOARD
    # =====================================================

    if "leaderboard" not in st.session_state:
        st.session_state.leaderboard = None
