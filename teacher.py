import streamlit as st

from config import (
    NUM_ITERATIONS,
    INITIAL_CAPITAL,
    DEFAULT_ALLOCATION
)


def teacher_page():

    st.header("👨‍🏫 Teacher Controls")


    # --------------------------------------------------
    # Simulation Controls
    # --------------------------------------------------

    st.subheader(
        "Simulation Controls"
    )


    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "🔒 Lock Allocations"
        ):

            st.session_state.allocation_locked = True

            st.success(
                "Student allocations locked."
            )


    with col2:

        if st.button(
            "🔓 Unlock Allocations"
        ):

            st.session_state.allocation_locked = False

            st.success(
                "Student allocations unlocked."
            )


    col3, col4 = st.columns(2)


    with col3:

        if st.button(
            "⏸ Pause Market"
        ):

            st.session_state.market_locked = True

            st.warning(
                "Market simulation paused."
            )


    with col4:

        if st.button(
            "▶ Resume Market"
        ):

            st.session_state.market_locked = False

            st.success(
                "Market simulation resumed."
            )


    st.divider()


    # --------------------------------------------------
    # Difficulty Settings
    # --------------------------------------------------

    st.subheader(
        "Market Difficulty"
    )


    difficulty = st.selectbox(

        "Choose Difficulty",

        [
            "Easy",
            "Medium",
            "Hard"
        ]

    )


    if difficulty == "Easy":

        st.info(
            """
Easy Mode:
- More stable markets
- Lower volatility
- Less extreme events
"""
        )


    elif difficulty == "Medium":

        st.info(
            """
Medium Mode:
- Balanced bull and bear markets
- Normal volatility
"""
        )


    else:

        st.warning(
            """
Hard Mode:
- More crises
- Higher volatility
- Larger drawdowns
"""
        )


    st.divider()


    # --------------------------------------------------
    # Class Status
    # --------------------------------------------------

    st.subheader(
        "Class Status"
    )


    c1, c2, c3 = st.columns(3)


    c1.metric(

        "Iteration",

        st.session_state.iteration

    )


    c2.metric(

        "Teams",

        len(st.session_state.team_names)

    )


    c3.metric(

        "Market",

        st.session_state.current_market
        if st.session_state.current_market
        else "Not Started"

    )


    st.divider()


    # --------------------------------------------------
    # Reset Simulation
    # --------------------------------------------------

    st.subheader(
        "Reset"
    )


    if st.button(
        "🔄 Reset Complete Simulation"
    ):

        reset_simulation()

        st.success(
            "Simulation reset successfully."
        )

        st.rerun()



def reset_simulation():


    st.session_state.iteration = 1


    st.session_state.game_finished = False


    st.session_state.current_market = None


    st.session_state.market_history = []


    st.session_state.market_locked = False


    st.session_state.allocation_locked = False


    for team in st.session_state.team_names:


        st.session_state.portfolio_value[team] = (
            INITIAL_CAPITAL
        )


        st.session_state.allocations[team] = (
            DEFAULT_ALLOCATION.copy()
        )


        st.session_state.previous_allocations[team] = (
            DEFAULT_ALLOCATION.copy()
        )


        st.session_state.value_history[team] = [
            INITIAL_CAPITAL
        ]


        st.session_state.returns_history[team] = []


        st.session_state.capital_return_history[team] = []


        st.session_state.income_return_history[team] = []


        st.session_state.transaction_cost_history[team] = []


        st.session_state.turnover_history[team] = []
